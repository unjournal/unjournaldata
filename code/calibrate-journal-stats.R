
# calibrate journal statistics against different "tier lists"

# == libraries ====
library(conflicted)
conflict_prefer_all("dplyr", quiet = TRUE)
library(dplyr)
library(here)
library(MASS)
library(readr)
library(openxlsx2)

source(here("code/lookup-publication-outcomes.R"))

# == ABDC models ====

# == Use the ABDC journal quality list and correlate it with h-index and
# impact factor
# From https://abdc.edu.au/abdc-journal-quality-list/
abdc_jql <- openxlsx2::read_xlsx(here("data/ABDC-JQL-2022-v3-100523.xlsx"), 
                                 sheet = 1, start_row = 9)
abdc_jql <- abdc_jql %>% 
  mutate(
    # Absolutely inevitably, the business school geniuses could not use Excel:
    rating = gsub(" +$", "", `2022 rating`),
    rating = ordered(rating, levels = c("C", "B", "A", "A*"))
  )

openalex_results <- map(abdc_jql$`Journal Title`, lookup_stats_openalex,
                        .progress = TRUE)
abdc_jql$h_index <- map_dbl(openalex_results, "h_index")
abdc_jql$impact_factor <- map_dbl(openalex_results, "2yr_mean_citedness")

readr::write_csv(abdc_jql, here("data/abdc-jql-enriched.csv"))

model1 <- MASS::polr(rating ~ h_index, data = abdc_jql)
model2 <- MASS::polr(rating ~ impact_factor, data = abdc_jql)
model3 <- MASS::polr(rating ~ h_index + impact_factor, data = abdc_jql)

saveRDS(model3, here("data/abdc-jql-model.rds"))

coefs_h <- broom::tidy(model1)
# This gives the cutpoint for a predicted A* journal in terms of the h index.
# It's almost exactly 240
cutpoint_a_star <- coefs_h$estimate[4] / coefs_h$estimate[1]


# == Multiple ratings from Prof Harzing's list ====

jql <- readr::read_csv("data/jql70a.csv") %>% 
  # Remove page headings:
  filter(! is.na(ISSN), ISSN != "ISSN") %>% 
  rename(Subject = "Subject area [Range highest to lowest]") %>% 
  # Excel misrecognized these numbers as dates. We convert them back:
  mutate(
    Scopus_date = as.Date(Scopus, format = "%d-%b"),
    Scopus_date = format(Scopus_date, format = "%d.%m"),
    Scopus_date = sub("\\.0([1-9])", ".\\1", Scopus_date),
    Scopus = ifelse(is.na(Scopus_date), Scopus, as.numeric(Scopus_date)),
    Scopus_date = NULL
  ) %>% 
  mutate(
    # Blanks mean the FT did not use the journal. We recode this so as to
    # match the others (higher = worse)
    FT     = ifelse(is.na(FT), 2, 1), 
    # Some random n/a values instead of blanks. No explanation given:
    ABS    = ifelse(ABS == "n/a", NA, ABS),
    Scopus = ifelse(Scopus == "n/a", NA, Scopus),
    # EJL counts M* as 'top management journal' and P* as 'top journal in its 
    # field'. We treat these as the same. M is not mentioned, even at
    # https://www.erim.eur.nl/about-erim/erim-journals-list-ejl/provisions/;
    # we treat it as equivalent to P.
    EJL      = ifelse(EJL == "M*", "P*", EJL),
    EJL      = ifelse(EJL == "M", "P", EJL)
  ) %>% 
  filter(
    # This removes one duplicate entry: Journal of Behavioral and Experimental
    # Economics. Below, we add in one piece of information from the deleted
    # entry.
    ! duplicated(Journal)
  ) %>% 
  mutate(
    JourQual = ifelse(
      Journal == "Journal of Behavioral and Experimental Economics",
      "B", JourQual)
  ) %>% 
  # We order rankings using the info given in the original PDF, from highest
  # to lowest:
  mutate(
    JourQual = ordered(JourQual, 
                       levels = c("A+", "A", "A/B", "B", "B/C", "C", "C/D", "D")),
    Cnrs     = ordered(Cnrs, levels = c("1*", "1", "2", "3", "4")),
    EJL      = ordered(EJL,    levels = c("P*", "P", "PA", "S")),
    ABS      = ordered(ABS,    levels = c("4*", "4", "3", "2", "1")), 
    Den      = ordered(Den,    levels = c("3", "2", "1")),
    Hceres   = ordered(Hceres, levels = c("A", "B", "C")),
    ABDC     = ordered(ABDC,   levels = c("A*", "A", "B", "C")),
    Fnege    = ordered(Fnege,  levels = c("1*", "1", "2", "3", "4")),
    # The PDF documentation says:
    # "The scores in this ranking (A+ to B) equate to the top-3 scores in other 
    # ranking that have four or five categories. Hence, any journal ranked on 
    # this list will be highly selective/regarded journals."
    # So, we treat an NA here as equivalent to a low ranking.
    Meta     = ordered(Meta,   levels = c("A+", "A", "B"), exclude = NULL)
  ) %>% 
  # We create numeric versions of the rankings, with the suffix "_n":
  mutate(
    across( ! c(ISSN,Journal, Subject),
            as.numeric,
            .names = "{.col}_n")
  )

# Notes about the rankings
# ========================
#
# For more info see https://harzing.com/download/jql70a-title.pdf
# or the original websites.
#
# * "Meta" is itself a meta-analysis. See http://meta-rating-bwl.org.
# * "Scopus" is the Scopus CiteScore 2020. It's not a true ranking
#   and is not normalized across fields.
# * "Hceres" is a combination of "CNRS" and "Fnege" with no extra info
#   of its own.

library(sinkr)
jql_matrix <- jql %>% 
  select(ends_with("_n") & !c(Scopus_n, Meta_n, Hceres_n)) %>% 
  as.matrix() 

jql_recon <- sinkr::dineof(jql_matrix)
# Xa is the reconstructed data with no missing values:
prc <- prcomp(jql_recon$Xa, scale. = TRUE)
# Really there's only one dimension here:
plot(prc) 
# So we just take the first principal component
jql$princomp1 <- predict(prc)[, 1] 


# Only "Den" is less correlated with the others, and only Den is correlated at
# less than 0.75 with the first principal component.
jql_matrix <- cbind(jql_matrix, jql$princomp1)
library(huxtable)
cor(jql_matrix, use = "compl") %>% round(3) %>% 
  as_hux() %>% 
  set_text_color("black") %>% 
  map_background_color(by_colorspace("darkred", "yellow"))

# Look up journal title states from Openalex
openalex_results <- map(jql$Journal, lookup_stats_openalex, .progress = TRUE)
jql$h_index <- map_dbl(openalex_results, "h_index")
jql$impact_factor <- map_dbl(openalex_results, "2yr_mean_citedness")
