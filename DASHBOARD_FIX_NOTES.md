# Dashboard Fix Notes - January 2026

## Problem

The Shiny dashboard at https://unjournal.shinyapps.io/uj-dashboard was showing blank plots and "Error: An error has occurred" messages.

## Root Cause Identified

The CSV file `data/rsx_evalr_rating.csv` has rating columns stored as **character strings**, not numbers:

```r
# Evidence from debugging:
> class(ratings$middle_rating)
[1] "character"

# Some values contain "\n" for missing data:
> head(ratings)
# middle_rating shows: "90", "75", "46", etc. as strings
# lower_CI shows: "85", "69", "\n" (newline for missing)
```

This causes ggplot2 to fail with: **"Discrete value supplied to continuous scale"**

## Fix Applied

In `shinyapp/dashboard/uj-dashboard.qmd`, the data import section was changed from:

```r
# OLD (broken):
ratings <- readr::read_csv(here("data/rsx_evalr_rating.csv"))
```

To:

```r
# NEW (fixed):
ratings <- readr::read_csv(here("data/rsx_evalr_rating.csv"), show_col_types = FALSE) |>
  mutate(
    middle_rating = as.numeric(middle_rating),
    lower_CI = as.numeric(lower_CI),
    upper_CI = as.numeric(upper_CI)
  )
```

## Commits Made

1. `fe4facb` - Fix data type conversion in dashboard (the main fix)
2. `ec464cc` - Fix data type conversion in static dashboard page
3. `4bc2e4b` - Add static fallback page for dashboard data
4. `533a4e9` - Add empty data handling to all plot functions

## Deployment Status

The GitHub Actions workflow keeps failing with HTTP 409:
```
Unable to dispatch task for application=11989094 as there are 1 tasks already in progress
```

This is a **shinyapps.io queue issue**, not a code issue. Previous deployments appear stuck.

## To Verify the Fix Works

1. Wait for shinyapps.io queue to clear (check https://www.shinyapps.io dashboard)
2. Re-run the workflow: `gh run rerun <run_id> --repo unjournal/unjournaldata`
3. Or manually trigger: push any small change to main

## Static Fallback Page

Created `website/posts/dashboard-data-jan2026/index.qmd` with static versions of all dashboard content. The website gh-pages publish was also failing (HTTP 400) - may need manual publish later.

## Files Changed

- `shinyapp/dashboard/uj-dashboard.qmd` - Main dashboard with data type fix
- `website/posts/dashboard-data-jan2026/index.qmd` - Static fallback page
- `code/import-unjournal-data.py` - Made robust for author_email/author_emails column name

## Why This Wasn't Caught Earlier

The CSV appears to have numeric-looking values, but `readr::read_csv()` guesses column types. When some rows have non-numeric values (like `"\n"` for missing), it reads the whole column as character. This worked before ggiraph was removed because ggiraph may have been failing silently, but static ggplot2 throws explicit errors.

---

## Display Improvements (January 19, 2026)

### Changes Made
- **Shortened criteria labels** for better readability:
  - "Global relevance/usefulness" (was "Relevance to global priorities/usefulness to practitioners")
  - "Claims and evidence" (was "Claims, strength, and characterization of Evidence")
  - "Open, replicable science" (was "Open, collaborative, replicable science")
- **Increased font sizes** in Individual Criteria and Paper comparison plots
- **Increased plot heights** (600px for criteria, 500px for comparison)
- **Removed dead link banner** (the "static data page" link that obscured content)

### Commits
- `6986b2c` - Improve dashboard display: larger fonts, shorter labels, remove dead link

---

## Development Dashboard Created

A separate development dashboard has been created for testing interactive features:

**Location:** `shinyapp/dashboard-dev/uj-dashboard-dev.qmd`

### Features
- **Plotly interactive hover tooltips** - shows paper names when hovering over data points
- Uses `plotlyOutput`/`renderPlotly` instead of static `plotOutput`/`renderPlot`
- Title shows "(Development)" to distinguish from production

### Deployment
The dev dashboard should be deployed as a separate app on shinyapps.io (e.g., `uj-dashboard-dev`). See `shinyapp/dashboard-dev/README.md` for deployment instructions.

### Background: Lost Interactive Features
The production dashboard lost interactive hover tooltips when ggiraph was removed (Jan 18, 2026). ggiraph was failing silently on shinyapps.io (no SVG output). The dev dashboard uses plotly as an alternative, which has better shinyapps.io compatibility.

### Commits
- `b4978cc` - Add development dashboard with plotly interactive features

---

## Plotly Integration into Production Dashboard (January 19, 2026)

After testing in the dev dashboard, plotly interactive features have been integrated into the main production dashboard.

### Changes Made
- **Overall Ratings plot**: Now uses plotly - hover over points to see paper names
- **Individual Criteria plot**: Now uses plotly - hover to see paper names
- **Paper Comparison plot**: Now uses plotly with:
  - Hover tooltips showing paper name and rating
  - **Median reference lines**: Grey | marks show median across all papers; Blue | marks show median for the selected research area (when not "All")

### Technical Details
- Replaced `renderPlot` with `renderPlotly` for all three interactive plots
- Uses `ggplotly(gg, tooltip = "text")` pattern to preserve ggplot2 aesthetics
- For Individual Criteria, uses `plotly::subplot()` to combine the two stacked plots
- For Paper Comparison, calculates medians from `res_ratings` data

### Dependencies
- Added `library(plotly)` to setup chunk (already installed in GitHub Actions workflow)
