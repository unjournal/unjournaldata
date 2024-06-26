# unjournaldata

This is the repository for
[Unjournal](https://www.unjournal.org) evaluations, meta-analysis, and meta-science.

Outputs and reports from here are published at <https://unjournal.github.io/unjournaldata>.


# How it works

Data is currently imported from Airtable. 

The github site is created as a [Quarto](https://quarto.org) book. There are also [Shiny](https://shiny.posit.co) apps at
<https://unjournal.shinyapps.io/DataExplorer/> and <https://unjournal.shinyapps.io/uj-dashboard>.

The github site and dashboard are automatically rendered on github when you push to the `main` branch.

Publicly available data is inside the `/data` folder. This is also auto-updated
via github actions.


# Data

The files in the `/data` folder are:

* `jql70a.csv`: a list of journal quality rankings, maintained by 
  [Prof. Anne-Wil Harzing](https://harzing.com/resources/journal-quality-list)
  and converted to CSV format. We thank Prof. Harzing for creating this valuable
  resource.
* `jql-enriched.csv`: the same data, enriched with h-index and 
  citedness information from [Openalex](https://openalex.org), and
  our own meta-ranking of journals, via `code/calibrate-journal-stats.R`.
* `evals.csv`: paper evaluations, imported from Airtable.
* `all_papers_p.csv`: evaluated papers, imported from Airtable.

# TODO

[TODO.md](TODO.md) has a list of planned changes.
