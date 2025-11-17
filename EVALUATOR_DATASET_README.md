# Evaluator-Paper Level Dataset

## Overview

The `evaluator_paper_level.csv` dataset provides a comprehensive view of evaluations at the **evaluator-paper level** (one row per evaluator-paper combination).

## Dataset Structure

- **~150 rows** (evaluator-paper combinations)
- **45+ columns** including:
  - Evaluator identifiers (PUBLIC NAMES ONLY - no pseudonyms)
  - Paper metadata
  - Survey responses (experience, time spent, field expertise)
  - Quantitative ratings (10 criteria with confidence intervals)
  - Evaluation stream (academic/applied)

## Key Columns

### Identifiers
- `evaluator` - PUBLIC evaluator identifier:
  - Names from ratings table if evaluator chose to use their name (e.g., "Ioannis Bournakis", "Romain Espinosa")
  - Generic "Evaluator 1", "Evaluator 2" for anonymous evaluations
  - **NEVER includes pseudonyms or confidential identifiers**
- `paper_title` - Full paper title
- `evaluation_stream` - "academic" or "applied"

### Survey Responses
- `How long have you been in this field?`
- `How many proposals, papers, and projects have you evaluated/reviewed?`
- `Approximately how long did you spend completing this evaluation?`
- `Field/expertise`
- `How would you rate this template and process?`
- `Would you be willing to consider evaluating a revised version of this work?`
- `hours_spent_manual_impute` - Manual coding of hours spent

### Quantitative Ratings (with confidence intervals)
Each criterion has 4 columns: `{criterion}_middle_rating`, `{criterion}_lower_CI`, `{criterion}_upper_CI`, `{criterion}_confidence_level`

**Criteria:**
1. `overall` - Overall assessment
2. `adv_knowledge` - Advancing knowledge
3. `claims` - Justifying/communicating claims
4. `gp_relevance` - Global priorities relevance
5. `journal_predict` - Journal tier prediction
6. `logic_comms` - Logic and communication
7. `merits_journal` - Journal publication merit
8. `methods` - Methods and execution
9. `open_sci` - Open science practices
10. `real_world` - Real-world robustness

### Paper Metadata
- `status` - Paper status in evaluation pipeline
- `research_url` - URL to research paper
- `doi` - Digital Object Identifier
- `main_cause_cat` - Primary cause category
- `cause_description` - Description of cause area

## Data Sources

Data is merged from:
1. **Coda Tables:**
   - "Responses: academic stream evaluations" (`grid-aDSyEIerdL`)
   - "Responses: applied stream evaluations" (`grid-znNSTj_xX3`)
   - "Evaluator Ratings" (`grid-pcJr9ZM3wT`)
   - "Research Papers" (`grid-Iru9Fra3tE`)

2. **PubPub Scraped Data:** (31 additional evaluations)
   - Survey responses scraped from individual evaluation pages

## Data Characteristics

### Coverage
- **Survey responses**: 94 rows (45%)
- **Quantitative ratings**: 94 rows (45%)
- **Both survey + ratings**: 1 row (0.5%)

Low overlap between survey and ratings is expected - many evaluations have either survey OR ratings, not both.

### Privacy & Exclusions

⚠️ **CRITICAL: This dataset has strong privacy protections**

**INCLUDED** (PUBLIC information only):
- Public evaluator identifiers (names if evaluator chose to use their name, or generic "Evaluator N")
- Survey responses: experience, time spent, field expertise
- Quantitative ratings with confidence intervals
- Paper metadata

**EXCLUDED** (confidential/sensitive):
- ❌ Evaluator pseudonyms (private codes used internally)
- ❌ Evaluator personal contact information
- ❌ Conflicts of interest (COI) disclosures
- ❌ Confidential comments and feedback
- ❌ Process feedback questions
- ❌ Re-evaluation willingness
- ❌ Any identifying feedback that could reveal evaluator identity

## File Generation

### Script
`code/create_evaluator_paper_dataset.py`

### How to Run Manually
```bash
# From project root
python3 code/create_evaluator_paper_dataset.py
```

### Requirements
- Coda API key in `.Renviron` file
- Python 3.9+ with packages: `codaio`, `pandas`, `python-dotenv`

## Automated Updates

### GitHub Actions (Daily)
The dataset is automatically regenerated daily via `.github/workflows/import-render-publish.yml`:

1. Fetches latest data from Coda
2. Runs `create_evaluator_paper_dataset.py`
3. Commits updated CSV to repository

### Linode Server (Cron Job)
For Linode server automation, see: `LINODE_CRON_SETUP.md`

## Usage Examples

### R
```r
library(readr)
df <- read_csv("data/evaluator_paper_level.csv")

# Analyze evaluator experience
summary(df$`How long have you been in this field?`)

# Compare ratings across criteria
library(tidyr)
ratings <- df %>%
  select(evaluator, paper_title, ends_with("_middle_rating")) %>%
  pivot_longer(ends_with("_middle_rating"),
               names_to = "criterion",
               values_to = "rating")
```

### Python
```python
import pandas as pd

df = pd.read_csv('data/evaluator_paper_level.csv')

# Filter to evaluations with both survey and ratings
complete = df[df['How long have you been in this field?'].notna() &
              df['overall_middle_rating'].notna()]

# Average ratings by criterion
rating_cols = [c for c in df.columns if c.endswith('_middle_rating')]
df[rating_cols].mean()
```

## Notes

- Paper titles are used for merging - slight variations can prevent matches
- Some evaluators have multiple evaluations of the same paper (revisions)
- NaN values are common - not all evaluations include all fields
- Evaluator identifiers follow privacy protections:
  - Public names are used if evaluator chose to identify themselves
  - Generic "Evaluator N" labels for anonymous evaluations
  - No internal pseudonyms or private identifiers are exposed

## Contact

For questions or issues with this dataset:
- GitHub: https://github.com/unjournal/unjournaldata/issues
- Documentation: https://unjournal.github.io/unjournaldata/
