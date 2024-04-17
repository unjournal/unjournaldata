# unjournaldata

This is the repository for 
[Unjournal](https://www.unjournal.org) evaluations, meta-analysis, and meta-science. 

Outputs and reports from here are published at <https://unjournal.github.io>.


# How it works

Data is currently imported manually from airtable. We hope to automate this soon.

The github site is created as a [Quarto](https://quarto.org) book. There is also
a [Shiny](https://shiny.posit.co) app at
<https://unjournal.shinyapps.io/DataExplorer/>. 

The site can be re-rendered by running `quarto render` from the command line,
or `quarto::quarto_render()` from within R, and pushing changes to the `main` branch.
The rendered HTML is then automatically deployed via github pages.

The shiny app can be deployed by running 
`rsconnect::deployApp("shinyapp/DataExplorer")`, or from within RStudio by
opening `shinyapp/DataExplorer/app.R` and clicking the 'publish' button.


# TODO

TODO.md has a list of planned changes. 