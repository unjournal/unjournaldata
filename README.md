# unjournaldata

This is the repository for
[Unjournal](https://www.unjournal.org) evaluations, meta-analysis, and meta-science.

Outputs and reports from here are published at <https://unjournal.github.io/unjournaldata>.


## How it works: data and dashboards

### Data Pipeline Overview

```
Coda.io (source database)
    ↓
GitHub Actions (daily + on push to main)
    ├→ code/import-unjournal-data.py → CSV files (data/*.csv)
    ├→ code/create_evaluator_paper_dataset.py → evaluator_paper_level.csv (with privacy protections)
    └→ Shiny dashboard deployment → https://unjournal.shinyapps.io/uj-dashboard

Optional: Linode Server (daily at 2 AM UTC)
    └→ code/export_to_sqlite.py → SQLite database
       (reads evaluator_paper_level.csv + direct Coda export)
```

### GitHub Actions Workflow

A single GitHub Action (`.github/workflows/import-render-publish.yml`):

1. **Exports data from Coda** to CSV files in the `/data` folder via `code/import-unjournal-data.py`
2. **Creates evaluator-paper dataset** with privacy protections via `code/create_evaluator_paper_dataset.py`
3. **Deploys the [Shiny](https://shiny.posit.co) dashboard** at <https://unjournal.shinyapps.io/uj-dashboard>

This action is automatically run:

* when the "main" branch is pushed to
* once daily at 13:30 UTC


## How it works: website and blog posts

The Unjournal data website is in the `/website` folder. It's not
created on GitHub, but directly on developer machines. 

* To add a blog post, create a new folder inside `website/posts`, and an 
  `index.qmd` file inside the folder. 
* Then navigate to the `website` folder and run `quarto publish gh-pages` from 
  the command line. This will update the `gh-pages` branch on GitHub, which 
  will then be reflected on the [unjournal.github.io website](https://unjournal.github.io/unjournaldata).
* Individual blog posts are *frozen*, so they won't be updated once they have been
  created. See [here](https://quarto.org/docs/websites/website-blog.html#freezing-posts).
* Also add and push your blog post, so your source code is visible on GitHub.
* See <https://quarto.org/docs/websites/website-blog.html> and 
  <https://quarto.org/docs/publishing/github-pages.html> for more details.


## Data

### CSV Files (Primary Data Format)

The files in the `/data` folder are imported from Coda:

* `paper_authors.csv`: Lists of authors per paper.
* `research.csv`: evaluated papers.
* `rsx_evalr_rating.csv`: quantitative ratings given by each evaluator for each
  paper.
* `evaluator_paper_level.csv`: Combined dataset at evaluator-paper level with privacy protections (no confidential feedback, COI info, or personal contact information).

There's also some data from other sources:

* `jql70a.csv`: a list of journal quality rankings, maintained by
  [Prof. Anne-Wil Harzing](https://harzing.com/resources/journal-quality-list)
  and converted to CSV format. We thank Prof. Harzing for creating this valuable
  resource.
* `jql-enriched.csv`: the same data, enriched with h-index and
  citedness information from [Openalex](https://openalex.org), and
  our own meta-ranking of journals, via `code/calibrate-journal-stats.R`.

### SQLite Database (Optional)

For SQL-based analysis and offline access, an optional SQLite database export is available.

**Database location:** Linode server at `/var/lib/unjournal/unjournal_data.db`

**Database tables:**
- `research` - Papers/projects being evaluated (~323 papers as of Dec 2025)
- `evaluator_ratings` - Quantitative ratings in long format (~859 ratings)
- `paper_authors` - Author relationships (~757 entries)
- `survey_responses` - Combined academic + applied evaluator surveys (~113 responses)
- `evaluator_paper_level` - Wide-format dataset with all ratings per evaluator-paper (194 rows)
- `researchers_evaluators` - Evaluator pool (279 evaluators, public fields only)
- `export_metadata` - Export history and statistics

**Setup and usage:**
- Setup instructions: See [LINODE_CRON_SETUP.md](LINODE_CRON_SETUP.md)
- Query examples: See [docs/SQLITE_QUERIES.md](docs/SQLITE_QUERIES.md)
- Export script: `code/export_to_sqlite.py`
- Automated daily sync at 2:00 AM UTC (Linode server)

**Create local database:**
```bash
# Requires CODA_API_KEY in .Renviron file
python3 code/export_to_sqlite.py --db-path ./unjournal_data.db

# Query the database
sqlite3 ./unjournal_data.db
```

## Privacy & Data Protection

All publicly shared datasets follow strict privacy protections:

- **NO confidential feedback** or evaluator comments
- **NO conflicts of interest** (COI) disclosures
- **NO personal contact information**
- **NO internal pseudonyms** or private identifiers

Public evaluator identifiers only:
- Names if evaluator chose to use their name (e.g., "Ioannis Bournakis")
- Generic "Evaluator 1", "Evaluator 2" for anonymous evaluations

See [EVALUATOR_DATASET_README.md](EVALUATOR_DATASET_README.md) for detailed privacy documentation.

## Documentation

**Main documentation:**
- **[README.md](README.md)** (this file) - Project overview and quick start
- **[CLAUDE.md](CLAUDE.md)** - Detailed architecture and developer guide
- **[EVALUATOR_DATASET_README.md](EVALUATOR_DATASET_README.md)** - Evaluator-paper dataset documentation

**Linode/SQLite setup:**
- **[LINODE_CRON_SETUP.md](LINODE_CRON_SETUP.md)** - SQLite database setup for Linode server
- **[docs/DATASETTE_GUI_SETUP.md](docs/DATASETTE_GUI_SETUP.md)** - Datasette web GUI setup
- **[docs/LINODE_SQLITE_INTERNAL_GUIDE.md](docs/LINODE_SQLITE_INTERNAL_GUIDE.md)** - Internal database management guide
- **[docs/SQLITE_QUERIES.md](docs/SQLITE_QUERIES.md)** - SQL query examples

## PubPub export utility

The repository includes `code/harvest_pubpub_assets.py`, a standalone script
that downloads fresh Markdown and PDF exports for every pub in a PubPub
community (``unjournal.pubpub.org`` by default).

### Quick start

1. Ensure you have Python 3.9+ available. Create and activate a virtual
   environment if you do not want to install dependencies globally:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the harvester, pointing it at an output directory where the Markdown and
   PDF exports should be written (the directory will be created if necessary):

   ```bash
   python code/harvest_pubpub_assets.py --output-dir pubpub_exports
   ```

   When the command finishes you will have fresh `<pub-slug>.md` and
   `<pub-slug>.pdf` files for every pub in the community.

### Additional usage tips

* Display all available options (including how to target a different community):

  ```bash
  python code/harvest_pubpub_assets.py --help
  ```

* To re-run the harvest later, simply execute the same command again; the
  script always requests new exports from PubPub before downloading them, so
  you will receive the latest content.

* Use `--community-host` if you want to collect assets from a community other
  than `unjournal.pubpub.org`, for example:

  ```bash
  python code/harvest_pubpub_assets.py \
      --community-host yourcommunity.pubpub.org \
      --output-dir ./yourcommunity_exports
  ```

* If you encounter transient network issues, the script will retry each
  download a few times. Re-running the command typically resolves failures
  caused by temporary connectivity errors.

