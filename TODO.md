
TODO

This is a place for planned or desirable technical changes.
Higher-level plans are discussed on
the [Unjournal coda.io project management website](https://coda.io/d/Project-Management-UJ_dOyXJoZ6imx/Projects_subw9#Projects_tuA9I/r30&view=full).

# General

[ ] Rewrite import-unjournal-data to use pubpub API
  - probably wait until v7 is usable
[x] Deploy shiny app using a github action, for consistency

# Descriptive work

[x] What are we evaluating? How many papers in total? In what subfields? What 
  does our “funnel” (selection process of candidate papers) look like?
[ ] How’s our process? How many papers per month? Turnaround times? 
  Numbers of evaluators per paper?
[x] Basic averages e.g. ratings for each question; or averages per subfield.

# Evaluating publication predictions

[ ] Find out how to check publication automatically (ish?)
  - get DOI; match it against databases; fall back to title and authors?
  - map publications to "tiers"
[ ] Build functions to create predictions from pairs of indiv. predictions
  - simple average
  - weighted by interval width
  - extremized average
  - for CIs, a Bayesian CI combining both?
  - see Hanea et al.
    "Mathematically aggregating experts’ predictions of possible futures"
  - see aggreCATS package for some examples, but don't use it, unmaintained
[ ] Test predictions against reality:
  - both for our "aggregate predictions", and for preds from individual raters
  - MSE or MAE for mean/medians
  - coverage for confidence intervals
[ ] Make a .qmd document or Shiny app reporting results overall, or for
  specific subcategories of evaluations.