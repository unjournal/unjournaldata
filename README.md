# unjournaldata

This is the repository for 
[Unjournal](https://www.unjournal.org) evaluations, meta-analysis, and meta-science. 

Outputs and reports from here are published at <https://unjournal.github.io/unjournaldata>.


# How it works

Data is currently imported from airtable. We hope to directly import from
<https://unjournal.pubpub.org> soon.

The github site is created as a [Quarto](https://quarto.org) book. There is also
a [Shiny](https://shiny.posit.co) app at
<https://unjournal.shinyapps.io/DataExplorer/>. 

The github site is automatically rendered on github when you push to the 
`main` branch.

The shiny app can be deployed by running 
`rsconnect::deployApp("shinyapp/DataExplorer")`, or from within RStudio by
opening `shinyapp/DataExplorer/app.R` and clicking the 'publish' button.


# TODO

TODO.md has a list of planned changes. 
