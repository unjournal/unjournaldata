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

### Linode SQLite Database (Optional)

**Status:** Operational (as of 2025-11-15)

A separate SQLite database export is available for SQL-based data analysis and offline access.

**Location:** Linode server at `/var/lib/unjournal/unjournal_data.db`

**Export Script:** `code/export_to_sqlite.py`

**Database Schema:**
- `research` - Papers/projects being evaluated (309 papers as of Nov 2025)
- `evaluator_ratings` - Quantitative ratings in long format (859 ratings)
- `paper_authors` - Author relationships (757 entries)
- `survey_responses` - Combined academic + applied evaluator surveys (113 responses)
- `evaluator_paper_level` - Wide-format dataset with all ratings per evaluator-paper
- `researchers_evaluators` - Evaluator pool (requires team management doc access)
- `export_metadata` - Export history and statistics

**Automated Sync:**
- Daily export at 2:00 AM UTC (cron job on Linode server)
- Cron script: `linode_setup/sync_cron.sh`
- Installation script: `linode_setup/install_sqlite_sync.sh`
- Logs: `/var/log/unjournal/sync_cron.log`
- Weekly backups: `/var/lib/unjournal/backups/` (30-day retention)

**Setup Documentation:** See `LINODE_CRON_SETUP.md` for complete installation and configuration guide

**Known Issues:**
- The `evaluator_paper_level` table export may fail with "status_x" column error due to duplicate column names in source CSV. This is non-critical as the core tables (research, evaluator_ratings, paper_authors, survey_responses) export successfully.

**Sample Queries:**
```bash
# Connect to database
sqlite3 /var/lib/unjournal/unjournal_data.db

# Papers with most evaluators
SELECT
  r.label_paper_title,
  COUNT(DISTINCT rt.evaluator) as num_evaluators,
  COUNT(rt.id) as num_ratings
FROM research r
LEFT JOIN evaluator_ratings rt ON r.label_paper_title = rt.research
GROUP BY r.label_paper_title
HAVING num_evaluators > 0
ORDER BY num_evaluators DESC;
```

**Data Flow (Linode):**
```
Coda.io (source database)
    ↓
code/export_to_sqlite.py (runs daily via cron)
    ↓
/var/lib/unjournal/unjournal_data.db (SQLite database)
    ↓
Available for SQL queries and analysis
```

### Key R Scripts
- `code/calibrate-journal-stats.R`: Enriches journal quality rankings with OpenAlex data, creates `data/jql-enriched.csv`
- `code/lookup-publication-outcomes.R`: Sourced by calibrate-journal-stats.R
- `code/create-data-for-DataExplorer.R`: Prepares data for DataExplorer Shiny app (currently not deployed)
- `code/DistAggModified.R`: Custom distribution aggregation functions

### Directory Structure
- `/code`: Python and R scripts for data processing
- `/data`: CSV exports from Coda.io and external data sources
- `/linode_setup`: Automated SQLite sync scripts for Linode server
- `/shinyapp/dashboard`: Main Shiny dashboard (Quarto format)
- `/shinyapp/DataExplorer`: Secondary Shiny app (not currently deployed)
- `/website`: Quarto website with blog posts (published to gh-pages)
- `/renv`: R environment management (renv library)

## Important Notes

- The dashboard references `code/import-unjournal-data.R` (line 104 of uj-dashboard.qmd) but this file doesn't exist. The actual data import uses the Python script.
- Data files in `/data` are auto-generated and auto-committed by GitHub Actions. Don't edit them manually.
- The DataExplorer app deployment is commented out in the GitHub Actions workflow.
- Website blog posts are frozen to prevent rebuilds.

## Security & Secrets

**CRITICAL:** No API keys or secrets are committed to this repository.

- `.Renviron` files (containing `CODA_API_KEY`) are gitignored and never committed
- `.env` files (used by Linode SQLite sync) are gitignored and never committed
- GitHub Actions uses repository secrets for all API keys (`CODA_API_KEY`, `RSCONNECT_TOKEN`, `AIRTABLE_API_KEY`, etc.)
- Linode server stores API keys in `/var/lib/unjournal/.env` with 600 permissions

**Protected files in .gitignore:**
- `.Renviron` - R environment variables
- `.env`, `*.env` - Python environment files
- `passwords.txt` - Any password files
