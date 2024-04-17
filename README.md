# unjournaldata

This is the repository for 
[Unjournal](https://www.unjournal.org) evaluations, meta-analysis, and meta-science. 

Our current reports are available at <https://unjournal.github.io>.

# How it works

Data is currently imported manually from airtable. We hope to automate this soon.

The github site is created as a [Quarto](https://quarto.org) book. There is also
a [Shiny](https://shiny.posit.co) app at
<https://unjournal.shinyapps.io/DataExplorer/>. 

The site can be re-rendered by running `quarto render` from the command line,
or `quarto::quarto_render()` from within R, and pushing changes to the `main` branch.

The shiny app can be deployed by running 
`rsconnect::deployApp("shinyapp/DataExplorer")`, or from within RStudio by
opening `shinyapp/DataExplorer/app.R` and clicking the 'publish' button.
