# Repository Guidelines

Read `CLAUDE.md` first; it is the canonical instruction file. Do not duplicate
database-repository instructions here.

## Project Structure & Data Flow
- `code/`: Public analysis code plus the fail-closed public-export installer.
- `data/`: Privacy-checked presentation data and public analysis datasets.
- `shinyapp/`: Quarto Shiny dashboard sources; reads `data/` outputs for publication to shinyapps.io.
- `website/`: Quarto website and blog posts published to `gh-pages`; posts live in `website/posts/*/index.qmd`.

All Coda ingestion, SQLite, Linode, bibliometrics operations, and internal data
belong in the private `unjournal/unjournal-database` repository.

## Setup, Build, and Run
- Python (3.9+): `python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt`.
- R deps: from R, run `renv::restore()`; execute R jobs via `Rscript code/<script>.R`.
- Verify a public export: `python3 code/install_public_export.py --source <public_export_dir>`.
- Website publish: `cd website && quarto publish gh-pages`; for local preview use `quarto preview`.

## Coding Style & Naming Conventions
- Python: 4-space indent, `snake_case` for files/functions, prefer small reusable functions; add `--help` options when extending CLI scripts.
- R: prefer tidyverse style and explicit library calls; keep scripts idempotent and avoid writing inside `data/` without flags.
- File naming: keep new scripts under `code/` with descriptive verbs (e.g., `export_*`, `check_*`); avoid modifying tracked CSVs directly.

## Testing & Validation
- No formal test suite; validate changes by running the affected script end-to-end and spot-checking generated CSVs/DB tables.
- For data changes, run `python3 -m unittest tests/test_install_public_export.py`.
- For dashboards/sites, run Quarto preview locally before publishing; capture screenshots when altering visuals.

## Commit & Pull Request Guidelines
- Commits: concise, present-tense summaries (<72 chars) similar to `Fix evaluator_paper_level export` or `Add SQLite export script`; separate unrelated changes.
- PRs: include purpose, key commands run, data outputs touched (`data/*.csv`, `*.db`), and screenshots for UI changes; link relevant issues/tasks.
- Avoid committing secrets or local `.Renviron`/`.env` files; note any required deployment variables in the PR description.

## Security & Secrets
- Never commit API keys; `.Renviron`, `.env`, and passwords are gitignored. Set `CODA_API_KEY` and other tokens locally or in GitHub Actions secrets.
- Follow `PUBLIC_DATA.md`. Never publish evaluator names linked to papers,
  stable evaluator pseudonyms, personal contact information, confidential
  comments, COI data, or private Coda links.
