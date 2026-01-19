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
