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

This exports three primary CSV files to `/data`:
- `research.csv`: evaluated papers
- `rsx_evalr_rating.csv`: quantitative ratings by evaluators
- `paper_authors.csv`: authors per paper

Additional data files generated:
- `evaluator_paper_level.csv`: wide-format dataset at evaluator-paper level with privacy protections (created by `create_evaluator_paper_dataset.py`)
- `evaluator_survey_responses.csv`: **PRIVATE** - evaluator survey data (gitignored, not committed to public repo, available only in SQLite database)
- `academic_stream_responses.csv`, `applied_stream_responses.csv`: survey response data
- `jql70a.csv`, `jql-enriched.csv`: journal quality rankings (external data)

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
2. **Evaluator-Paper Dataset**: Runs `code/create_evaluator_paper_dataset.py` to create wide-format dataset with privacy protections
3. **Data Commit**: Auto-commits updated CSV files to the repository
4. **Environment Setup**: Installs Python 3.11, R (via renv), Quarto, and system dependencies (JAGS, etc.)
5. **Dashboard Publish**: Publishes `shinyapp/dashboard` to shinyapps.io using rsconnect

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
data/*.csv files (research.csv, rsx_evalr_rating.csv, paper_authors.csv)
    ↓
code/create_evaluator_paper_dataset.py
    ↓
data/evaluator_paper_level.csv (wide-format with privacy protections)
    ↓
Auto-committed to repository
    ↓
shinyapp/dashboard/uj-dashboard.qmd (reads CSVs)
    ↓
Published to shinyapps.io
```

### Linode SQLite Database (Optional)

**Status:** Operational (as of 2025-12-15)

A separate SQLite database export is available for SQL-based data analysis and offline access.

**Location:** Linode server at `/var/lib/unjournal/unjournal_data.db`

**Export Script:** `code/export_to_sqlite.py`

**Database Schema:**
- `research` - Papers/projects being evaluated (323 papers as of Dec 2025)
- `evaluator_ratings` - Quantitative ratings in long format (859 ratings)
- `paper_authors` - Author relationships (757 entries)
- `survey_responses` - Combined academic + applied evaluator surveys (113 responses)
- `evaluator_paper_level` - Wide-format dataset with all ratings per evaluator-paper (194 rows)
- `researchers_evaluators` - Evaluator pool, public fields only (279 evaluators, NO emails/personal data)
- `bibliometrics` - Paper-level bibliometric data from OpenAlex (citations, venue, funders)
- `bibliometrics_history` - Time series of citation snapshots for tracking growth
- `export_metadata` - Export history and statistics

**Automated Sync:**
- Daily export at 2:00 AM UTC (cron job on Linode server)
- Cron script: `linode_setup/sync_cron.sh`
- Installation script: `linode_setup/install_sqlite_sync.sh`
- Logs: `/var/log/unjournal/sync_cron.log`
- Weekly backups: `/var/lib/unjournal/backups/` (30-day retention)

**Setup Documentation:** See `LINODE_CRON_SETUP.md` and `docs/DATASETTE_GUI_SETUP.md` for complete installation and configuration guides

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
code/export_to_sqlite.py (runs daily at 2:00 AM UTC via cron)
    ↓
/var/lib/unjournal/unjournal_data.db (SQLite database)
    ↓
    ├─ Datasette GUI (http://45.79.160.157:8001) - password-protected web interface
    └─ Direct SQL queries and analysis
```

**Datasette Web GUI:**
- **URL**: http://45.79.160.157:8001
- **Authentication**: Username `admin` (password-protected)
- **Features**: Browse tables, run SQL queries, export CSV/JSON, share query URLs
- **Setup**: See `docs/DATASETTE_GUI_SETUP.md`

### Bibliometrics Pipeline

**Status:** Operational (weekly updates)

Automated system to fetch paper-level bibliometric data from OpenAlex and update both Coda and local storage.

**Script:** `code/update_bibliometrics.py`

**Data collected from OpenAlex:**
- Citation counts (`cited_by_count`, `fwci`)
- Publication venue (journal name, type, tier)
- Funder information
- Author count and institutional affiliations
- Open access status

**Output files:**
- `data/bibliometrics.csv` - Current bibliometric data for all papers with DOIs
- `data/bibliometrics_history.csv` - Time series of citation snapshots (for tracking growth)

**Automated Sync:**
- Weekly update at 3:00 AM UTC every Sunday (Linode cron)
- Cron script: `linode_setup/update_bibliometrics_cron.sh`
- Installation script: `linode_setup/install_bibliometrics_cron.sh`
- Logs: `/var/log/unjournal/bibliometrics.log`

**Usage:**
```bash
# Run manually (local or Linode)
python3 code/update_bibliometrics.py

# Dry run (skip Coda update, CSV only)
python3 code/update_bibliometrics.py --dry-run

# Force update all papers (ignore last_updated threshold)
python3 code/update_bibliometrics.py --force
```

**SQLite tables:**
- `bibliometrics` - Current values per paper
- `bibliometrics_history` - Time series for citation tracking

**Data Flow (Bibliometrics):**
```
OpenAlex API
    ↓
code/update_bibliometrics.py (runs weekly at 3:00 AM UTC Sunday)
    ↓
├─ data/bibliometrics.csv (current values)
├─ data/bibliometrics_history.csv (time series)
├─ Coda database (DOI work view)
└─ SQLite database (via export_to_sqlite.py)
```

### Key Scripts

**Python Scripts:**
- `code/import-unjournal-data.py`: Main data import from Coda.io to CSV files
- `code/create_evaluator_paper_dataset.py`: Creates wide-format evaluator-paper dataset with privacy protections
- `code/export_to_sqlite.py`: Exports data to SQLite database (used by Linode server)
- `code/update_bibliometrics.py`: Fetches paper-level bibliometrics from OpenAlex, updates Coda and CSV
- `code/harvest_pubpub_assets.py`: Downloads Markdown/PDF exports from PubPub community
- `code/analyze_survey_responses.py`: Analyzes evaluator survey data
- `code/clean_and_merge_survey_data.py`: Processes and combines survey responses

**R Scripts:**
- `code/calibrate-journal-stats.R`: Enriches journal quality rankings with OpenAlex data, creates `data/jql-enriched.csv`
- `code/lookup-publication-outcomes.R`: Sourced by calibrate-journal-stats.R
- `code/create-data-for-DataExplorer.R`: Prepares data for DataExplorer Shiny app (currently not deployed)
- `code/DistAggModified.R`: Custom distribution aggregation functions

### Directory Structure
- `/code`: Python and R scripts for data processing
- `/data`: CSV exports from Coda.io and external data sources
- `/docs`: Documentation files for Linode setup, Datasette, and SQL queries
- `/linode_setup`: Automated SQLite sync scripts and installation scripts for Linode server
- `/shinyapp/dashboard`: Main Shiny dashboard (Quarto format)
- `/shinyapp/DataExplorer`: Secondary Shiny app (not currently deployed)
- `/website`: Quarto website with blog posts (published to gh-pages)
- `/nextjs-docs`: Next.js documentation site (experimental)
- `/renv`: R environment management (renv library)
- `/.github/workflows`: GitHub Actions automation workflows

## Important Notes

- **Data files in `/data` are auto-generated** and auto-committed by GitHub Actions. Don't edit them manually.
- **The DataExplorer app deployment** is commented out in the GitHub Actions workflow.
- **Website blog posts are frozen** to prevent rebuilds once published.
- **Privacy protections**: All publicly shared datasets exclude confidential feedback, COI disclosures, and personal contact information.
- **Multiple documentation formats**: Root-level `.md` files contain working/analysis documentation; `/docs` contains operational guides.

## Additional Documentation

**Root-level documentation files:**
- `EVALUATOR_DATASET_README.md`: Detailed documentation for evaluator-paper dataset and privacy protections
- `LINODE_CRON_SETUP.md`: Setup guide for Linode server automation (SQLite export and cron jobs)
- `MISSING_DATA_SUMMARY.md`, `PUBPUB_LOOKUP_NEEDED.md`, `WIDE_FORMAT_INTEGRATION_SUMMARY.md`: Working notes and analysis documentation
- `AGENTS.md`: Agent/automation configuration notes

**Documentation in `/docs` directory:**
- `docs/DATASETTE_GUI_SETUP.md`: Datasette web GUI installation and configuration
- `docs/LINODE_SQLITE_INTERNAL_GUIDE.md`: Internal guide for managing the SQLite database on Linode
- `docs/SQLITE_QUERIES.md`: Example SQL queries for the SQLite database
- `docs/LINODE_SETUP_FAQ.md`: Frequently asked questions for Linode setup

## Security & Secrets

**CRITICAL:** No API keys or secrets are committed to this repository.

- `.Renviron` files (containing `CODA_API_KEY`) are gitignored and never committed
- `.env` files (used by Linode SQLite sync) are gitignored and never committed
- GitHub Actions uses repository secrets for all API keys (`CODA_API_KEY`, `RSCONNECT_TOKEN`, `AIRTABLE_API_KEY`, etc.)
- Linode server stores API keys in `/var/lib/unjournal/.env` with 600 permissions

**Protected files in .gitignore:**
- `.Renviron` - R environment variables (contains `CODA_API_KEY`)
- `.env`, `*.env` - Python environment files
- `passwords.txt` - Any password files
- `data/evaluator_survey_responses.csv` - Private evaluator feedback (evaluators were promised this would not be public)
- `data/survey_responses_preview.csv` - Survey preview data
