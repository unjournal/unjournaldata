
# calibrate journal statistics against different "tier lists"
# This creates data/jql-enriched.csv

# == libraries ====
library(conflicted)
conflict_prefer_all("dplyr", quiet = TRUE)
library(dplyr)
library(here)
library(MASS)
library(readr)
library(sinkr) # marchtaylor/sinkr

source(here("code/lookup-publication-outcomes.R"))

set.seed(10271975)

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


jql_matrix <- jql %>% 
  select(ends_with("_n") & !c(Scopus_n, Meta_n, Hceres_n)) %>% 
  as.matrix() 

# Reconstructs missing values
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

# Look up journal stats from Openalex
openalex_results <- map(jql$Journal, lookup_stats_openalex, .progress = TRUE)

# For now, we simply discard the (quite common) journals which get multiple
# answers in openalex:
jql$h_index <- map_dbl(openalex_results, 
  function (x) if (length(x) == 1) x[[1]]$h_index else NA_real_
)
jql$citedness <- map_dbl(openalex_results, 
  function (x) if (length(x) == 1) x[[1]]$"2yr_mean_citedness" else NA_real_
)

# Den doesn't predict citedness beyond the first principal component:
summary(lm(citedness ~ princomp1 + Den_n, data = jql))
# Den doesn't predict h-index beyond the first principal component:
summary(lm(h_index ~ princomp1 + Den_n, data = jql))

# So, we feel justified in using the first principal component alone

# Most of the "top" categories are about -6.5 with the exception of ABDC
# JourQual is 5-tier with some A/B, B/C, C/D
# Cnrs, ABS and Fnege are 5-tier
# ABDC is 4 tier and the top tier is lower than the others

#' Estimate category boundaries for princomp1
#' 
#' We do this by estimating an ordinal logit of the category on
#' princomp1, then dividing the category boundaries by the coefficient
#' for princomp1
#'
#' @param ranking Name of a ranking in the jql data
#'
#' @return A list of categories
#' @export
#'
#' @examples
get_cat_boundaries <- function (ranking) {
  fml <- as.formula(sprintf("%s ~ princomp1", ranking))
  mod <- MASS::polr(fml, data = jql)
  coef <- coef(mod)[["princomp1"]]
  boundaries <- mod$zeta
  boundaries <- boundaries/coef
  return(boundaries)
}

# Reduce JourQual to a 5-category ranking:
jql$JourQual2 <- dplyr::case_match(jql$JourQual,
                                "A/B" ~ "B",
                                "B/C" ~ "C",
                                "C/D" ~ "D",
                               .default = jql$JourQual
                               )
jql$JourQual2 <- ordered(jql$JourQual2, levels = c("A+", "A", "B", "C", "D"))


cat_bounds <- map(c("JourQual2", "Cnrs", "ABS", "Fnege"), get_cat_boundaries)
cat_bounds <- map(cat_bounds, unname)
# This transposes the list so the 1st element is the top category boundary,
# 2nd element is the second boundary, etc.
cat_bounds <- list_transpose(cat_bounds)
cat_bounds <- map_dbl(cat_bounds, mean)
cat_bounds <- round(cat_bounds, 1)

jql$unjournal_tier <- cut(jql$princomp1, c(-Inf, cat_bounds, Inf),
                          labels = c("1", "2", "3", "4", "5"))

jql %>% 
  select(! ends_with("_n")) %>% 
  readr::write_csv(here("data/jql-enriched.csv"))
