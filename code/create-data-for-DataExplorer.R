
# This creates data in the "long" form used by the shiny data explorer app
# and writes it to shinyapp/DataExplorer/shiny_explorer.rds.
# It's called automatically by the deploy.yml Github Actions workflow,
# which then uploads the data and app to shinyapps.io

library(tidyverse) 
library(knitr)
library(bookdown)
library(quarto)
library(formattable)
library(readr)
library(here)
library(DescTools)
select <- dplyr::select 

source(here("code", "DistAggModified.R"))


evals_pub <- readr::read_csv(here("data/evals.csv"))
all_papers_p <- readr::read_csv(here("data/all_papers_p.csv"))

evals_pub_long <- evals_pub |> 
  pivot_longer(cols = -c(id, crucial_rsx, crucial_rsx_id, 
                         paper_abbrev, eval_name, 
                         cat_1,cat_2, cat_3, source_main, author_agreement),
               names_pattern = "(lb_|ub_|conf_)?(.+)",
               names_to = c("value_type", "rating_type")) |> # one line per rating type
  mutate(value_type = if_else(value_type == "", "est_", value_type)) |> #add main rating id
  pivot_wider(names_from = value_type, 
              values_from = value)

rating_cats <- c("overall", "adv_knowledge", "methods", "logic_comms", "real_world", "gp_relevance", "open_sci")

pred_cats <- c("journal_predict", "merits_journal")

# calculate the lower and upper bounds, 
# rating: given a rating, 
# conf: a confidence (1-5) score,
# type: a bound type (lower, upper),
# scale: a scale (100 is 0-100, 5 is 1-5)
# This function is not vectorized
calc_bounds <- function(rating, conf, type, scale) {
  
  if(scale == 5){ #for the 'journal tier prediction case'
    baseline_width = case_match(conf, 
                                5 ~ .2, #4*5/100
                                4 ~ .4, #8*5/100
                                3 ~ .75, #15*5/100
                                2 ~ 1.25, #25*5/100
                                1 ~ 1.875, #37.5*5/100
                                .default = NA_real_) 

    upper = min(rating + baseline_width, 5)
    lower = max(rating - baseline_width, 1)
  }#/if(scale == 5)
  
  if(scale == 100){ #for the 'ratings case'
    
    baseline_width = case_match(conf, 
                                5 ~ 4, 
                                4 ~ 8, 
                                3 ~ 15, 
                                2 ~ 25, 
                                1 ~ 37.5,
                                .default = NA_real_)
    
    upper = min(rating + baseline_width, 100)
    lower = max(rating - baseline_width, 0)
  } #/if(scale == 100)
  
  if(type == "lower") return(lower)
  if(type == "upper") return(upper)
}


# calculate or find correct lower or upper bound
# based on rating type, and lb, ub, and conf values
impute_bounds <- function(var_name, est, lb, ub, conf, bound_type) {
  
  # get scale of each variable
  scale = if_else(var_name %in% c("journal_predict", "merits_journal"), # if variable is a prediction
                  5, 100) #scale is 5, else scale is 100
  # if calculating lower bound variable
  if(bound_type == "lower") { #we are calculating a lower bound imputation
    # 
    calculated_bound = map_dbl(.x = est, .f = calc_bounds, conf = conf, type = bound_type, scale = scale)
    
    imp_bound = if_else(is.na(lb), calculated_bound, lb)
  }
  
  # if calculating upper bound variable
  if(bound_type == "upper") { #we are calculating an upper bound imputation
    # 
    calculated_bound = map_dbl(.x = est, .f = calc_bounds, conf = conf, type = bound_type, scale = scale)
    imp_bound = if_else(is.na(ub), calculated_bound, ub)
  }
  
  return(imp_bound)
}

# apply functions to evals_pub_long
# where each row is one type of rating
# so each evaluation is 9 rows long
evals_pub_long <- evals_pub_long |> 
  rowwise() |> # apply function to each row
  mutate(lb_imp_ = impute_bounds(var_name = rating_type,
                                   est = est_,
                                   lb = lb_, ub = ub_, conf = conf_,
                                   bound_type = "lower")) |> 
  mutate(ub_imp_ = impute_bounds(var_name = rating_type,
                                   est = est_,
                                   lb = lb_, ub = ub_, conf = conf_,
                                   bound_type = "upper"))



# Clean evals_pub_long names (remove _ at end)
evals_pub_long <- evals_pub_long |> 
  rename_with(.cols = ends_with("_"),
              .fn = str_remove,
              pattern = "_$")

# paper_ratings: even longer dataframe (ie tidy)
# renamed to conform to aggreCAT nomenclature

paper_ratings <- evals_pub_long |> 
  select(id, eval_name, paper_abbrev, rating_type, est, lb_imp, ub_imp) |> 
  filter(rating_type %in% rating_cats) |>
  rename(paper_id = paper_abbrev,
         user_name = eval_name,
         three_point_lower = lb_imp,
         three_point_upper = ub_imp,
         three_point_best = est) |>
  mutate(round = "round_1") |> 
  pivot_longer(cols = starts_with("three_point"),
               names_to = "element",
               values_to = "value")

# calculate aggregated upper and lower bounds using modified
# aggreCAT function DistributionWAggMOD
paper_agg_ratings <- paper_ratings |> 
  group_by(rating_type, user_name, paper_id) |> 
  filter(sum(is.na(value))==0) |> #remove ratings (best, ub, lb) that have NA values
  group_by(rating_type) |> 
  nest() |> 
  mutate(results = map(.x = data, .f = DistributionWAggMOD, 
                       round_2_filter = FALSE, percent_toggle = T)) |> 
  unnest(results) |> 
  select(-data) |> 
  select(paper_id, rating_type, everything()) |>   
  arrange(paper_id) |> 
  mutate(across(.cols = c("agg_est", "agg_90ci_lb", "agg_90ci_ub"), .fns = ~.x*100)) |> 
  rename(agg_method = method)


evals_pub_long <- evals_pub_long |> 
  left_join(paper_agg_ratings, by = c("paper_abbrev" = "paper_id", "rating_type"="rating_type"))

evals_pub_long <- evals_pub_long |> 
  mutate(rating_type = factor(rating_type, 
                              levels = c(rating_cats, pred_cats),
                              labels = c("Overall assessment",
                                         "Advances our knowledge & practice",  
                                         "Methods: justification, reasonableness, validity, robustness", 
                                         "Logic and communication", 
                                         "Engages with real-world, impact quantification",
                                         "Relevance to global priorities",
                                         "Open, collaborative, replicable science and methods",
                                         "Predicted Journal", "Merits Journal")))

write_rds(evals_pub_long, file = here("shinyapp/DataExplorer/shiny_explorer.rds"))


