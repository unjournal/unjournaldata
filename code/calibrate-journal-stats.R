
# calibrate journal statistics against different "tier lists"
library(conflicted)
conflict_prefer_all("dplyr", quiet = TRUE)
library(dplyr)
library(here)
library(MASS)
library(readr)
library(openxlsx2)

source(here("code/lookup-publication-outcomes.R"))

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
