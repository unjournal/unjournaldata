# Development Dashboard

This is a development version of the Unjournal dashboard for testing new features before deploying to production.

## Key Differences from Production

- **Interactive plots with plotly**: Hover over data points to see paper names
- Title shows "(Development)" to distinguish from production

## Deploying to shinyapps.io

Deploy this dashboard as a separate app (e.g., `uj-dashboard-dev`):

```r
# From R console in this directory
rsconnect::setAccountInfo(
  name = Sys.getenv("RSCONNECT_USER"),
  token = Sys.getenv("RSCONNECT_TOKEN"),
  secret = Sys.getenv("RSCONNECT_SECRET")
)

quarto::quarto_publish_app(
  input = ".",
  name = "uj-dashboard-dev",
  account = Sys.getenv("RSCONNECT_USER"),
  server = "shinyapps.io"
)
```

Or manually deploy via RStudio's Publish button.

## Features Being Tested

1. **Plotly hover tooltips** - Shows paper names when hovering over data points
2. Potential future: Restore ggiraph if plotly works reliably

## Dependencies

Requires `plotly` package in addition to production dependencies.
