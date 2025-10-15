# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This repository manages [The Unjournal](https://www.unjournal.org) evaluations data, meta-analysis, and dashboards. It automatically exports data from Coda.io and publishes interactive dashboards and a static website.

**Main outputs:**
- Shiny dashboard: https://unjournal.shinyapps.io/uj-dashboard
- Website: https://unjournal.github.io/unjournaldata

## Key Commands

### Data Import
```bash
# Import data from Coda.io (requires CODA_API_KEY environment variable)
python3 code/import-unjournal-data.py
```

This exports three CSV files to `/data`:
- `research.csv`: evaluated papers
- `rsx_evalr_rating.csv`: quantitative ratings by evaluators
- `paper_authors.csv`: authors per paper

### Python Environment
```bash
# Install Python dependencies
pip install -r requirements.txt

# PubPub harvester (downloads Markdown/PDF exports)
python code/harvest_pubpub_assets.py --output-dir pubpub_exports
```

### R Environment
This project uses `renv` for R dependency management.

```bash
# Restore R environment (run from R console)
renv::restore()

# Calibrate journal statistics
Rscript code/calibrate-journal-stats.R
```

### Dashboard Development
The Shiny dashboard is in `shinyapp/dashboard/uj-dashboard.qmd` (Quarto Shiny document).

**Note:** The dashboard sources `code/import-unjournal-data.R` which doesn't exist in the repository. This file is likely generated or the reference is outdated. The dashboard uses data from CSV files in `/data`.

### Website Publishing
The website is in `/website` and uses Quarto.

```bash
cd website
quarto publish gh-pages
```

Blog posts are **frozen** (they won't be rebuilt once created). To add a blog post:
1. Create a new folder in `website/posts`
2. Add an `index.qmd` file in that folder
3. Run `quarto publish gh-pages` from the `website` directory

## Architecture

### Automated Pipeline (GitHub Actions)
The `.github/workflows/import-render-publish.yml` workflow runs daily at 13:30 UTC and on pushes to main:

1. **Data Import**: Runs `code/import-unjournal-data.py` to fetch data from Coda.io
2. **Data Commit**: Auto-commits updated CSV files to the repository
3. **Environment Setup**: Installs Python 3.11, R (via renv), Quarto, and system dependencies (JAGS, etc.)
4. **Dashboard Publish**: Publishes `shinyapp/dashboard` to shinyapps.io using rsconnect

**Required secrets:**
- `CODA_API_KEY`: Coda.io API access
- `RSCONNECT_USER`, `RSCONNECT_TOKEN`, `RSCONNECT_SECRET`: Shinyapps.io credentials
- `AIRTABLE_API_KEY`: (used by dashboard)
- `RENV_GITHUB_PAT`: GitHub PAT for renv package installation

### Data Flow
```
Coda.io (source database)
    ↓
code/import-unjournal-data.py
    ↓
data/*.csv files (committed to repo)
    ↓
shinyapp/dashboard/uj-dashboard.qmd (reads CSVs)
    ↓
Published to shinyapps.io
```

### Key R Scripts
- `code/calibrate-journal-stats.R`: Enriches journal quality rankings with OpenAlex data, creates `data/jql-enriched.csv`
- `code/lookup-publication-outcomes.R`: Sourced by calibrate-journal-stats.R
- `code/create-data-for-DataExplorer.R`: Prepares data for DataExplorer Shiny app (currently not deployed)
- `code/DistAggModified.R`: Custom distribution aggregation functions

### Directory Structure
- `/code`: Python and R scripts for data processing
- `/data`: CSV exports from Coda.io and external data sources
- `/shinyapp/dashboard`: Main Shiny dashboard (Quarto format)
- `/shinyapp/DataExplorer`: Secondary Shiny app (not currently deployed)
- `/website`: Quarto website with blog posts (published to gh-pages)
- `/renv`: R environment management (renv library)

## Important Notes

- The dashboard references `code/import-unjournal-data.R` (line 104 of uj-dashboard.qmd) but this file doesn't exist. The actual data import uses the Python script.
- Data files in `/data` are auto-generated and auto-committed by GitHub Actions. Don't edit them manually.
- The DataExplorer app deployment is commented out in the GitHub Actions workflow.
- Website blog posts are frozen to prevent rebuilds.
- Environment variables are shared between Python (`.Renviron`) and GitHub Actions (secrets). The `.Renviron` file must never be committed.
