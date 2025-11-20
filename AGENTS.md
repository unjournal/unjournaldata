# Repository Guidelines

## Project Structure & Data Flow
- `code/`: Python and R scripts for ingest, privacy filtering, PubPub harvests, and SQLite export; scripts write to `data/`.
- `data/`: CSV outputs from Coda and enriched datasets; auto-written by pipelines—do not edit by hand.
- `shinyapp/`: Quarto Shiny dashboard sources; reads `data/` outputs for publication to shinyapps.io.
- `website/`: Quarto website and blog posts published to `gh-pages`; posts live in `website/posts/*/index.qmd`.
- `linode_setup/`: Cron and helper scripts for the optional SQLite sync on Linode.

## Setup, Build, and Run
- Python (3.9+): `python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt`.
- R deps: from R, run `renv::restore()`; execute R jobs via `Rscript code/<script>.R`.
- Import latest Coda data (requires `CODA_API_KEY` in `.Renviron`): `python code/import-unjournal-data.py`.
- Build evaluator-paper dataset with privacy protections: `python code/create_evaluator_paper_dataset.py`.
- Optional SQLite export: `python code/export_to_sqlite.py --db-path ./unjournal_data.db` then inspect with `sqlite3 ./unjournal_data.db`.
- Website publish: `cd website && quarto publish gh-pages`; for local preview use `quarto preview`.
- PubPub harvest: `python code/harvest_pubpub_assets.py --output-dir pubpub_exports`.

## Coding Style & Naming Conventions
- Python: 4-space indent, `snake_case` for files/functions, prefer small reusable functions; add `--help` options when extending CLI scripts.
- R: prefer tidyverse style and explicit library calls; keep scripts idempotent and avoid writing inside `data/` without flags.
- File naming: keep new scripts under `code/` with descriptive verbs (e.g., `export_*`, `check_*`); avoid modifying tracked CSVs directly.

## Testing & Validation
- No formal test suite; validate changes by running the affected script end-to-end and spot-checking generated CSVs/DB tables.
- For data changes, inspect row counts or key columns (e.g., `sqlite3 ./unjournal_data.db "SELECT COUNT(*) FROM research;"`).
- For dashboards/sites, run Quarto preview locally before publishing; capture screenshots when altering visuals.

## Commit & Pull Request Guidelines
- Commits: concise, present-tense summaries (<72 chars) similar to `Fix evaluator_paper_level export` or `Add SQLite export script`; separate unrelated changes.
- PRs: include purpose, key commands run, data outputs touched (`data/*.csv`, `*.db`), and screenshots for UI changes; link relevant issues/tasks.
- Avoid committing secrets or local `.Renviron`/`.env` files; note any required env vars (`CODA_API_KEY`, `AIRTABLE_API_KEY`, `RSCONNECT_*`) in the PR description.

## Security & Secrets
- Never commit API keys; `.Renviron`, `.env`, and passwords are gitignored. Set `CODA_API_KEY` and other tokens locally or in GitHub Actions secrets.
- When sharing logs, redact evaluator names if anonymized variants are expected in outputs.
