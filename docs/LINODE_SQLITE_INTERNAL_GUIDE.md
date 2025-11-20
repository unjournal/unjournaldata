# Linode SQLite Internal Guide

## Goals
- Keep the Linode SQLite database fresh, performant, and private.
- Provide a single, password-protected web entry point (docs + GUI).
- Offer quick-start commands for analysts and maintainers.

## Where & How to Access
- DB path: `/var/lib/unjournal/unjournal_data.db` (owned by the cron user).
- SSH first: `ssh linode-user@<host>`; never expose the DB publicly.
- Refresh manually (uses CODA_API_KEY from `/var/lib/unjournal/.env`):
  ```bash
  cd /opt/unjournal
  python3 code/export_to_sqlite.py --db-path /var/lib/unjournal/unjournal_data.db
  sqlite3 /var/lib/unjournal/unjournal_data.db "PRAGMA integrity_check;"
  ```
- Back up before heavy work:
  ```bash
  sqlite3 /var/lib/unjournal/unjournal_data.db ".backup /var/lib/unjournal/backups/unjournal_$(date +%Y%m%d).db"
  ```

## Password-Protected Web Docs & GUI (recommended pattern)
1. **Create static docs** (served behind auth):
   - Place Markdown/HTML in `/var/lib/unjournal/docs` (generated from this repo’s `docs/`).
   - Serve with nginx basic auth:
     ```bash
     sudo apt install nginx apache2-utils
     sudo htpasswd -c /etc/nginx/.htpasswd unjournal
     # add server block pointing root to /var/lib/unjournal/docs with `auth_basic` + TLS
     sudo nginx -t && sudo systemctl reload nginx
     ```
2. **Add a simple GUI (read-only)**:
   - In a venv: `pip install datasette datasette-permissions-sqlite`.
   - Launch (bound to localhost): `datasette /var/lib/unjournal/unjournal_data.db --metadata metadata.json`.
   - Reverse-proxy via nginx with the same `auth_basic` block; keep `allow_download` off in `metadata.json` if desired.
   - Start as a service (example unit):
     ```ini
     [Service]
     ExecStart=/opt/unjournal/.venv/bin/datasette /var/lib/unjournal/unjournal_data.db --host 127.0.0.1 --port 8011
     WorkingDirectory=/opt/unjournal
     Restart=always
     ```
3. **Single password**: store the hash only in `/etc/nginx/.htpasswd`; rotate monthly.

## Routine Health Checks
- Size & schema: `sqlite3 ... ".schema"` and `.tables`.
- Index sanity: confirm indexes exist (see schema below); run `VACUUM` monthly during low traffic.
- Logs: `/var/log/unjournal/sqlite_export.log` (created when directory exists).

## Data Schema (summary)
- `research(label_paper_title PK, status, doi, main_cause_cat, overall_mean_score, created_at, updated_at)`
- `evaluator_ratings(id PK, research FK→research, evaluator, criteria, middle_rating, lower_CI, upper_CI, confidence_level, row_created_date, created_at, updated_at, UNIQUE(research,evaluator,criteria))`
- `paper_authors(id PK, research FK→research, author, author_emails, corresponding, created_at, updated_at)`
- `survey_responses(id PK, paper_title, evaluation_stream, years_in_field, papers_reviewed, time_spent, field_expertise, research_link_coda, status, date_entered, hours_spent_manual_impute, created_at, updated_at)`
- `evaluator_paper_level(id PK, evaluator, paper_title, evaluation_stream, years_in_field, papers_reviewed, ratings/interval columns..., research_link_coda, status, date_entered, hours_spent, research_url, doi, main_cause_cat, created_at, updated_at, UNIQUE(paper_title,evaluator))`
- `researchers_evaluators(id PK, name_text UNIQUE, email, expertise, affiliated_organization, created_at, updated_at)`
- `export_metadata(id PK, table_name, row_count, export_timestamp, status, error_message)`
- Indexes: ratings(research/evaluator/criteria), paper_authors(research), evaluator_paper_level(evaluator/paper_title).

## Schema Visual
```mermaid
erDiagram
  research ||--o{ evaluator_ratings : "research"
  research ||--o{ paper_authors : "research"
  research ||--o{ evaluator_paper_level : "paper_title"

  research {
    TEXT label_paper_title PK
    TEXT status
    TEXT doi
    TEXT main_cause_cat
    REAL overall_mean_score
  }
  evaluator_ratings {
    INTEGER id PK
    TEXT research FK
    TEXT evaluator
    TEXT criteria
    REAL middle_rating
  }
  paper_authors {
    INTEGER id PK
    TEXT research FK
    TEXT author
    TEXT author_emails
  }
  evaluator_paper_level {
    INTEGER id PK
    TEXT paper_title FK
    TEXT evaluator
    REAL overall_rating
    REAL methods_rating
    REAL claims_rating
  }
  survey_responses {
    INTEGER id PK
    TEXT paper_title
    TEXT evaluation_stream
  }
  researchers_evaluators {
    INTEGER id PK
    TEXT name_text UNIQUE
    TEXT email
  }
  export_metadata {
    INTEGER id PK
    TEXT table_name
    INTEGER row_count
    TEXT status
  }
```

## Quick Usage Recipes
- Top papers with ≥2 evaluators:
  ```sql
  SELECT r.label_paper_title, COUNT(DISTINCT rt.evaluator) AS evaluators, r.overall_mean_score
  FROM research r
  JOIN evaluator_ratings rt ON r.label_paper_title = rt.research
  GROUP BY r.label_paper_title
  HAVING evaluators >= 2
  ORDER BY evaluators DESC;
  ```
- Export evaluator summary to CSV:
  ```bash
  sqlite3 /var/lib/unjournal/unjournal_data.db <<'SQL'
  .mode csv
  .output /tmp/evaluator_summary.csv
  SELECT evaluator, COUNT(*) AS num_ratings, ROUND(AVG(middle_rating),2) AS avg_rating
  FROM evaluator_ratings
  WHERE middle_rating IS NOT NULL
  GROUP BY evaluator
  ORDER BY num_ratings DESC;
  .output stdout
  SQL
  ```
