This is a place for planned or desirable technical changes.

Higher-level plans are discussed on
the [Unjournal coda.io project management website](https://coda.io/d/Project-Management-UJ_dOyXJoZ6imx/Projects_subw9#Projects_tuA9I/r30&view=full).

# General

[ ] Rewrite import-unjournal-data to use Coda.io (once the database schema is
    nailed down)
    - rework scripts currently using the R version to read the csv file
    - wait for column names etc. to settle down, then rewrite scripts using
      the csv
    - import for all_papers_p.csv
[ ] Maybe consider splitting the deploy action up
[x] Add field descriptions to data folder, or point to documentation elsewhere.
[x] Put the DataExplorer app deployment into deploy.yml and not in 
    the quarto!


# Descriptive work

[x] What are we evaluating? How many papers in total? In what subfields? What does our “funnel” (selection process of candidate papers) look like?
[ ] How’s our process? How many papers per month? Turnaround times?
  Numbers of evaluators per paper?
[x] Basic averages e.g. ratings for each question; or averages per subfield.


# Inter-rater reliability, 'modeling ratings'

[ ] Measures of rating consistency across evaluators (e.g., IRR)
    - by paper
    - by rating category
    - by other aggregations (field/cause, etc.)

[  ] Model/decompose variance in rating
    - Systematic correlates of high/low ratings
    - Look for factors suggesting 'biases', e.g.,  ...
    - ... are evaluators who sign their names more positive
    - ... do people in British-style academic institutions give lower ratings 
      (perhaps because "a 70 is a first")
    - ... higher for some fields/causes

Do these analyses in a ~quarto 'ask and answer questions' format

# Evaluating publication predictions

[x] Find out how to check publication automatically (ish?)
[ ] Build functions to create predictions from pairs of indiv. predictions
  - simple average
  - weighted by interval width
  - extremized average
  - for CIs, a Bayesian CI combining both?
  - see Hanea et al.
    "Mathematically aggregating experts’ predictions of possible futures"
  - see aggreCATS package for some examples, but don't use it, unmaintained
    - DR: Note that Julia did some of this in the Quarto already, but we are not sure it's correct

[ ] Test predictions against reality:
  - both for our "aggregate predictions", and for preds from individual raters
  - MSE or MAE for mean/medians
  - coverage for confidence intervals

[ ] Make a .qmd document or Shiny app reporting results overall, or for specific subcategories of evaluations.
