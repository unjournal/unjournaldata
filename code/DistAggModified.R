# aggreCAT::DistributionWAgg Modified to also include 90% upper and lower bounds of the aggregated distribution

DistributionWAggMOD <- function(expert_judgements,
         type = "DistribArMean",
         name = NULL,
         placeholder = FALSE,
         percent_toggle = FALSE,
         round_2_filter = TRUE) {
  
  if(!(type %in% c("DistribArMean",
                   "TriDistribArMean"))){
    
    stop('`type` must be one of "DistribArMean" or "TriDistribArMean"')
    
  }
  
  ## Set name argument
  
  name <- ifelse(is.null(name),
                 type,
                 name)
  
  cli::cli_h1(sprintf("DistributionWAgg: %s",
                      name))
  
  if(isTRUE(placeholder)){
    
    method_placeholder(expert_judgements,
                       name)
    
  } else {
    
    df <- expert_judgements %>%
      preprocess_judgements(percent_toggle = {{percent_toggle}},
                            round_2_filter = {{round_2_filter}}) %>%
      dplyr::group_by(paper_id)
    
    # create different Fx_fun and avdist_fun based on "type"
    switch(type,
           "DistribArMean" = {
             
             Fx_fun <- function(x, lower, best, upper) {
               dplyr::case_when(
                 x < 0 ~ 0,
                 x >= 0 & x < lower ~ 0.05 / lower * x,
                 x >= lower &
                   x < best ~ 0.45 / (best - lower) * (x - lower) + 0.05,
                 x >= best &
                   x < upper ~ 0.45 / (upper - best) * (x - best) + 0.5,
                 x >= upper &
                   x < 1 ~ 0.05 / (1 - upper) * (x - upper) + 0.95,
                 x > 1 ~ 1
               )
             }
             
             avdist_fun <- function(dq, claim_input) {
               claim_input %>%
                 dplyr::mutate(Fx = purrr::pmap(
                   list(three_point_lower,
                        three_point_best,
                        three_point_upper),
                   .f = function(l, b, u) {
                     function(x) {
                       Fx_fun(x,
                              
                              lower = l,
                              best = b,
                              upper = u)
                     }
                   }
                 ))  %>%
                 purrr::pluck("Fx") %>%
                 purrr::map_dbl(
                   .f = function(Fx_fun) {
                     Fx_fun(dq)
                   }
                 ) %>%
                 mean()
             }
             
           },
           "TriDistribArMean" = {
             
             Fx_fun <- function(x, lower, best, upper) {
               dplyr::case_when(
                 x < lower ~ 0,
                 x >= lower &
                   x < best ~ ((x-lower) ^ 2) / ((upper - lower) * (best - lower)),
                 x >= best &
                   x < upper ~ 1 - (((upper - x) ^ 2) / ((upper - lower) * (upper - best))),
                 x >= upper ~ 1
               )
             }
             
             avdist_fun <- function(dq, claim_input) {
               claim_input %>%
                 dplyr::mutate(Fx = purrr::pmap(
                   list(three_point_lower,
                        three_point_best,
                        three_point_upper),
                   .f = function(l, b, u) {
                     function(x) {
                       Fx_fun(x,
                              
                              lower = l,
                              best = b,
                              upper = u)
                     }
                   }
                 ))  %>%
                 purrr::pluck("Fx") %>%
                 purrr::map_dbl(
                   .f = function(Fx_fun) {
                     Fx_fun(dq)
                   }
                 ) %>%
                 mean()
             }
             
           })

    agg_judge_df <- df  %>%
      tidyr::pivot_wider(names_from = element, values_from = value) %>%
      dplyr::mutate(
        three_point_upper = dplyr::if_else(
          three_point_upper == 1,
          three_point_upper - .Machine$double.eps,
          three_point_upper
        ),
        three_point_lower = dplyr::if_else(
          three_point_lower == 0,
          three_point_lower + .Machine$double.eps,
          three_point_lower
        ),
        three_point_best = dplyr::if_else(
          three_point_best == 1,
          three_point_best - 2*.Machine$double.eps,
          three_point_best
        ),
        three_point_best = dplyr::if_else(
          three_point_best == 0,
          three_point_best + 2*.Machine$double.eps,
          three_point_best
        ),
        # ensure the values are in order
        three_point_upper = dplyr::if_else(
          three_point_upper < three_point_best,
          three_point_best,
          three_point_upper
        ),
        three_point_lower = dplyr::if_else(
          three_point_lower > three_point_best,
          three_point_best,
          three_point_lower
        ),
      ) %>%
      dplyr::group_by(paper_id) %>%
      tidyr::nest() %>%
      dplyr::mutate(avdist = purrr::map(
        data,
        .f = function(data) {
          function(x) {
            avdist_fun(x, claim_input = data)
          }
        }
      )) %>% dplyr::ungroup()
    
    quantiles <- agg_judge_df %>%
      dplyr::mutate(avdist_preimage = purrr::map(
        avdist,
        .f = function(f) {
          GoFKernel::inverse(f, lower = 0, upper = 1)
        }
      )) %>% 
      dplyr::mutate(aggregated_judgement =
                      purrr::map_dbl(
                        avdist_preimage,
                        .f = function(f) {
                          # suppressing warnings on preimage
                          f(0.5) #gets the midpoint?
                        }
                      )) %>% 
      dplyr::mutate(aggregated_judgement_90ci_lb =
                      purrr::map_dbl(
                        avdist_preimage,
                        .f = function(f) {
                          # suppressing warnings on preimage
                          f(0.05) # gets the lower bound for the 90% interval
                        }
                      )) %>% 
      dplyr::mutate(aggregated_judgement_90ci_ub =
                      purrr::map_dbl(
                        avdist_preimage,
                        .f = function(f) {
                          # suppressing warnings on preimage
                          f(0.95) # gets the upper bound for the 90th percentile
                        }
                      ))
    
    
    # figure out how many experts there are in the data?
    n_experts <- df %>%
      dplyr::group_by(paper_id, user_name) %>%
      dplyr::summarise(n_experts = dplyr::n(), .groups = "drop_last") %>%
      dplyr::count() %>%
      dplyr::rename("n_experts" = "n") %>%
      dplyr::ungroup()
    
    x <-  quantiles %>%
      dplyr::left_join(n_experts, by = "paper_id") %>%
      dplyr::select(paper_id, aggregated_judgement, aggregated_judgement_90ci_lb, aggregated_judgement_90ci_ub, n_experts) %>%
      dplyr::ungroup()
    
    x %>%
      dplyr::group_by(paper_id) %>%
      dplyr::mutate(method = name) %>%
      dplyr::ungroup()  %>%
      dplyr::select(method,
                    paper_id,
                    aggregated_judgement,
                    aggregated_judgement_90ci_lb, 
                    aggregated_judgement_90ci_ub,
                    n_experts) %>%
      dplyr::rename(
        agg_est = aggregated_judgement,
        agg_90ci_lb = aggregated_judgement_90ci_lb,
        agg_90ci_ub = aggregated_judgement_90ci_ub
      )
  }
}
