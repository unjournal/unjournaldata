# unjournaldata

This is the repository for
[Unjournal](https://www.unjournal.org) evaluations, meta-analysis, and meta-science.

Outputs and reports from here are published at <https://unjournal.github.io/unjournaldata> (as well as embedded and independently hosted 'Shiny' dashboards).


# How it works

Data is currently imported from Airtable. 16 May 2024: We hope to directly import from our Coda database soon, which in turn, we hope to feed from our PubPub page content (either V6 or V7).

The github site is created as a [Quarto](https://quarto.org) book. There is also
a [Shiny](https://shiny.posit.co) app at
<https://unjournal.shinyapps.io/DataExplorer/> as well as another one David HJ built (see `uj-dashboard.qmd`) hosted [here](https://unjournal.shinyapps.io/uj-dashboard)

The github site is automatically rendered on github when you push to the `main` branch (this is done by Github Actions; see [.github/workflows
/deploy.yml](https://github.com/unjournal/unjournaldata/blob/main/.github/workflows/deploy.yml)

The shiny app can be deployed by running
`rsconnect::deployApp("shinyapp/DataExplorer")`, or from within RStudio by
opening `shinyapp/DataExplorer/app.R` and clicking the 'publish' button.


# TODO


[TODO.md](TODO.md) has a list of planned changes.
