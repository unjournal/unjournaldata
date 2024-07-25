# unjournaldata

This is the repository for
[Unjournal](https://www.unjournal.org) evaluations, meta-analysis, and meta-science.

Outputs and reports from here are published at <https://unjournal.github.io/unjournaldata>.


## How it works

A single GitHub Action:

* Exports data from Coda to csv files in the `/data` folder, via
  `code/import-unjournal-data.py`.
* Creates <https://unjournal.github.io/unjournaldata> from a
  [Quarto](https://quarto.org) book. 
* Creates [Shiny](https://shiny.posit.co) apps at 
  <https://unjournal.shinyapps.io/DataExplorer/> and 
  <https://unjournal.shinyapps.io/uj-dashboard>.

This action is automatically run 

* when the "main" branch is pushed to;
* once daily in any case.


## Blog

Unjournal blog posts are in the `/blog` folder. These aren't 
created on GitHub, but directly on developer machines. 

* To add a blog post, create a new folder inside `blog/posts`, and an 
  `index.qmd` file inside the folder. 
* Render the quarto file as normal, add it to the `gh-pages` branch, 
  and push to GitHub.
* See <https://quarto.org/docs/websites/website-blog.html> for more details.


## Data

The files in the `/data` folder are imported from Coda:

* `paper_authors.csv`: Lists of authors per paper.
* `research.csv`: evaluated papers.
* `rsx_evalr_rating.csv`: quantitative ratings given by each evaluator for each
  paper.

There's also some data from other sources:

* `jql70a.csv`: a list of journal quality rankings, maintained by 
  [Prof. Anne-Wil Harzing](https://harzing.com/resources/journal-quality-list)
  and converted to CSV format. We thank Prof. Harzing for creating this valuable
  resource.
* `jql-enriched.csv`: the same data, enriched with h-index and 
  citedness information from [Openalex](https://openalex.org), and
  our own meta-ranking of journals, via `code/calibrate-journal-stats.R`.

