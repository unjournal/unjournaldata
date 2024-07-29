
# aggreCAT::DistributionWAgg modified to also include 90% upper and lower bounds 
# of the aggregated distribution.
# preprocess_judgements() is taken from aggreCAT with some modifications

preprocess_judgements <- function(expert_judgements,
  round_2_filter = TRUE,
  three_point_filter = TRUE,
  percent_toggle = FALSE){

  if(any(is.na(expert_judgements$value))) stop("NAs Found in Values")

  # Variables of focus
  expert_judgements <- expert_judgements |>
    dplyr::select(round,
      paper_id,
      user_name,
      element,
      value)

  filter_round <- function(expert_judgements, round_2_filter){
    output_df <-  if(isTRUE(round_2_filter)){
      expert_judgements |>
        dplyr::filter(round %in% "round_2")
    } else {
      expert_judgements
    }
  }

  filter_element <- function(expert_judgements, three_point_filter){
    output_df <- if(isTRUE(three_point_filter)){
      expert_judgements |>
        dplyr::group_by(round, paper_id, user_name) |>
        dplyr::filter(element %in% c("three_point_best",
          "three_point_lower",
          "three_point_upper"))
    } else {
      expert_judgements |>
        dplyr::filter(element != "binary_question")
    }
  }

  change_value <- function(expert_judgements, percent_toggle){
    # Converts values to 0,1
    output_df <- if(isTRUE(percent_toggle)){
      expert_judgements |>
        dplyr::mutate(value =
            dplyr::case_when(
              element %in% c("three_point_best",
                "three_point_lower",
                "three_point_upper") ~ value / 100,
              TRUE ~ value
            ))
    } else {
      expert_judgements
    }

  }

  check_values <- function(expert_judgements, round_2_filter, three_point_filter, percent_toggle){
    if(isTRUE(percent_toggle)){
      if(isTRUE(max(expert_judgements$value) > 1)) {
        warning("Non probability value outside 0,1 ")
      }
    }

    return(expert_judgements)
  }

  method_out <-  expert_judgements |>
    filter_round(round_2_filter) |>
    filter_element(three_point_filter) |>
    change_value(percent_toggle) |>
    dplyr::bind_rows() |>
    check_values(round_2_filter, three_point_filter, percent_toggle) |>
    dplyr::ungroup()

  return(method_out)
}

DistributionWAggMOD <- function(expert_judgements,
         name = NULL,
         placeholder = FALSE,
         percent_toggle = FALSE,
         round_2_filter = TRUE) {

  ## Set name argument
  
  name <- ifelse(is.null(name),
                 "DistributionWAggMOD",
                 name)

    df <- expert_judgements |>
      preprocess_judgements(percent_toggle = percent_toggle,
                            round_2_filter = round_2_filter) |>
      dplyr::group_by(paper_id)
    
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
      claim_input |>
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
        ))  |>
        purrr::pluck("Fx") |>
        purrr::map_dbl(
          .f = function(Fx_fun) {
            Fx_fun(dq)
          }
        ) |>
        mean()
    }
    agg_judge_df <- df  |>
      tidyr::pivot_wider(names_from = element, values_from = value) |>
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
      ) |>
      dplyr::group_by(paper_id) |>
      tidyr::nest() |>
      dplyr::mutate(avdist = purrr::map(
        data,
        .f = function(data) {
          function(x) {
            avdist_fun(x, claim_input = data)
          }
        }
      )) |> dplyr::ungroup()
    
    quantiles <- agg_judge_df |>
      dplyr::mutate(avdist_preimage = purrr::map(
        avdist,
        .f = function(f) {
          GoFKernel::inverse(f, lower = 0, upper = 1)
        }
      )) |> 
      dplyr::mutate(aggregated_judgement =
                      purrr::map_dbl(
                        avdist_preimage,
                        .f = function(f) {
                          # suppressing warnings on preimage
                          f(0.5) #gets the midpoint?
                        }
                      )) |> 
      dplyr::mutate(aggregated_judgement_90ci_lb =
                      purrr::map_dbl(
                        avdist_preimage,
                        .f = function(f) {
                          # suppressing warnings on preimage
                          f(0.05) # gets the lower bound for the 90% interval
                        }
                      )) |> 
      dplyr::mutate(aggregated_judgement_90ci_ub =
                      purrr::map_dbl(
                        avdist_preimage,
                        .f = function(f) {
                          # suppressing warnings on preimage
                          f(0.95) # gets the upper bound for the 90th percentile
                        }
                      ))
    
    
    # figure out how many experts there are in the data?
    n_experts <- df |>
      dplyr::group_by(paper_id, user_name) |>
      dplyr::summarise(n_experts = dplyr::n(), .groups = "drop_last") |>
      dplyr::count() |>
      dplyr::rename("n_experts" = "n") |>
      dplyr::ungroup()
    
    x <-  quantiles |>
      dplyr::left_join(n_experts, by = "paper_id") |>
      dplyr::select(paper_id, aggregated_judgement, 
                    aggregated_judgement_90ci_lb, aggregated_judgement_90ci_ub, 
                    n_experts) |>
      dplyr::ungroup()
    
    x |>
      dplyr::group_by(paper_id) |>
      dplyr::mutate(method = name) |>
      dplyr::ungroup()  |>
      dplyr::select(method,
                    paper_id,
                    aggregated_judgement,
                    aggregated_judgement_90ci_lb, 
                    aggregated_judgement_90ci_ub,
                    n_experts) |>
      dplyr::rename(
        agg_est = aggregated_judgement,
        agg_90ci_lb = aggregated_judgement_90ci_lb,
        agg_90ci_ub = aggregated_judgement_90ci_ub
      )
}
