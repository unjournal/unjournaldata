# Public data boundary

This public repository does not ingest Coda data and must not copy the private
database repository's `data/` directory.

The only supported data path is:

1. `unjournal-database/code/build_public_export.py` creates `public_export/`
   from a strict allowlist and fails closed on private fields or values.
2. The private workflow publishes only that bundle to this repository's
   dedicated `public-data` branch.
3. `code/install_public_export.py` verifies the file set, schemas, row counts,
   SHA-256 hashes, email-like values, and private Coda URLs.
4. GitHub Actions installs the verified files in `data/` and publishes the
   dashboard.

The public workflow does not hold a credential for the private repository.

## Managed files

| File | Public contents |
|---|---|
| `research.csv` | Paper metadata needed by public analyses |
| `rsx_evalr_rating.csv` | Ratings with per-paper generic evaluator labels and an anonymity flag |
| `evaluator_paper_level.csv` | Evaluation stream and hours spent, with paper/evaluator identifiers removed |

The generic evaluator labels are deliberately scoped to a paper. They must not
be replaced with names, hashes, internal codes, or stable cross-paper
pseudonyms.

## Prohibited content

Do not commit raw evaluation-form exports, author or evaluator email addresses,
confidential comments, COI disclosures, raw willingness or process feedback,
private Coda links, evaluator names joined to papers, or internal pseudonyms.

Operational data, imports, SQLite files, server scripts, and private audit
evidence belong in `unjournal/unjournal-database`.

## Approved aggregate survey restoration

David authorized restoring non-identifying experience statistics and process
feedback summaries on November 23, 2026. The historical aggregate snapshot in
`website/posts/evaluator-survey-insights/survey_aggregate_snapshot.json` contains
only summary statistics and counts. The post may present broad paraphrased
feedback themes and aggregate willingness counts with their sample and parsing
limitations. This exception does not permit individual answers, distinctive
quotations, respondent-level experience or expertise, or links between feedback,
people, and papers. Raw survey files remain private.
