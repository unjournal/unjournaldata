
# functions to calculate inter-rater reliability for slices of the data

library(dplyr)
loadNamespace("irr")
loadNamespace("tidyr")

library(conflicted)
conflicts_prefer(dplyr::filter, dplyr::select)

# Notes on choice of stat: 
# * Hallgren, "Computing Inter-Rater Reliability for Observational Data:An Overview and Tutorial" is a useful introduction.
# * kappa2 is for nominal/ordinal data, fully crossed designs, [each rater evaluates all the same items).]
# and biased by prevalence/bias effects

# prevalence --  "when the distribution of ratings is skewed, with one or more categories having a much higher or lower frequency than others"

# bias effects:  something like 'where $X_{A_i} = (X_{B_i})/2 + 50 + e$ ...  A's uses the 50-100 scale while B uses the whole range"

# DR -- for our purposes, if raters are using the scale like this, this would be a weakness of our measures that we would *want* to detect. 

# DR -- also note that we have a 0-100 percentile scale; I don't think this is 'nominal'


# * iota() is for "multivariate observations" [DR: So don't we want to use that instead?]

# * Hallgren: "Fleiss (1971) provides formulas for a kappa-like coefficient that is suitable for studies where any constant number of m coders is randomly sampled from a larger population of coders..." 

#   DHJ:  that sounds like us [DR: why? I agree we are multivariate, but I'm not sure about the 'random sample' assumption]

# * ICC is for ordinal/interval data, i.e. it takes account of distance between different guesses. [DR: I guess we have ordinal data]

#As we have many different  coders (evaluators) we need a "one-way" estimate of ICC i.e. one which doesn't try to estimate any individual coder's bias [DR: Why?]

# * Krippendorff and Hayes make the claim that only Krippendorff's alpha is the "gold standard" for IRR 


#' Estimates intraclass correlation from a subset of Unjournal data
#'
#' At present, only papers with exactly two evaluations are used.
#' Otherwise we'll have to deal with missing data, see the {irrNA} package.
#'
#' @param data A subset of `evals_pub`
#' @param rating An unquoted column name, e.g. `overall`, `methods`,
#'   corresponding to a quantitative rating given by evaluators
#'
#' @return An object of class irrlist, as returned by [irr::icc].
#'
#' @examples
#' 
#' estimate_icc(evals_pub, overall)
#'
#' conservation_icc_methods <- evals_pub |>
#'   filter(cat_1 == "conservation") |> 
#'   estimate_icc(rating = methods)
#'   
estimate_icc <- function (data, rating) {
  evals <- pivot_evals(data, enquo(rating), exactly_two = TRUE)
  irr::icc(evals, model = "oneway")
}


#' @rdname estimate_icc
#' @param method Passed to [irr::kripp.alpha()]. One of "nominal", 
#'   "ordinal", "interval" or "ratio". 
estimate_kripp_alpha <- function (data, rating, method = "interval") {
  evals <- pivot_evals(data, enquo(rating), exactly_two = FALSE)
  
  # kripp.alpha uses a different interface to the rest of the irr package :-/
  evals <- as.matrix(evals)
  evals <- t(evals)
  
  irr::kripp.alpha(evals, method = method)
}


#' Prepare data for use by {irr} functions, via [tidyr::pivot_wider()]
#'
#' Private function, not part of the API!
#' 
#' @param data A subset of `evals_pub`
#' @param rating An unquoted column name, e.g. `overall`, `methods`,
#'   corresponding to a quantitative rating given by evaluators
#' @param exactly_two Logical. Include only papers with exactly two
#'   raters? Necessary to avoid listwise deletion for many methods.
#'   If FALSE, includes all papers with two raters or more.
#'
#' @return A wider dataset of ratings per paper
#' @noRd
#'
#' @examples
pivot_evals <- function (data, rating, exactly_two = FALSE) {
  data <- data %>% 
    select(id, crucial_rsx, !!rating) %>% 
    mutate(
      .by = crucial_rsx,
      eval_number = seq_len(n())
    ) 
  
  if (exactly_two) {
    data <- filter(data, .by = crucial_rsx,
                   n() == 2L)
  } else {
    data <- filter(data, .by = crucial_rsx,
                   n() >= 2L)
  }
     
  data <- data %>%
    tidyr::pivot_wider(
      id_cols = crucial_rsx,
      names_prefix = "eval_", 
      names_from = eval_number, 
      values_from = !!rating
    ) %>% 
    select(starts_with("eval_"))
  
  data
}
