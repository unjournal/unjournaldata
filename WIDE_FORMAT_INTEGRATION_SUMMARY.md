# Wide Format Integration Summary

## Overview

Successfully integrated ratings from Coda evaluation form responses into the wide-format `evaluator_paper_level.csv` file.

## Results

### Data Filled
- **Total values updated**: 582 missing values
- **Evaluations updated**: 38 out of 149 evaluations (25.5%)
- **Missing values reduction**: 26.3% (from 2,217 to 1,635 missing values)

### By Criterion

| Criterion | Total Filled | Middle Rating | Lower CI | Upper CI |
|-----------|--------------|---------------|----------|----------|
| real_world | 76 | 30 | 23 | 23 |
| overall | 66 | 24 | 21 | 21 |
| journal_predict | 64 | 24 | 20 | 20 |
| adv_knowledge | 63 | 23 | 20 | 20 |
| gp_relevance | 63 | 23 | 20 | 20 |
| merits_journal | 61 | 25 | 18 | 18 |
| logic_comms | 60 | 22 | 19 | 19 |
| methods | 57 | 19 | 19 | 19 |
| open_sci | 54 | 18 | 18 | 18 |
| claims | 18 | 6 | 6 | 6 |

## Files Generated

### 1. `data/evaluator_paper_level_updated.csv`
- **Complete file** with all 149 evaluations
- **All columns** from original file plus updated values
- **Use this** if you want to replace the entire table in Coda

### 2. `data/evaluator_paper_level_changes_only.csv`
- **Only 38 evaluations** that had changes
- **Same columns** as the full file
- **Use this** if you want to update only the changed rows in Coda

## Sample Updated Evaluations

1. **Adaptability and the Pivot Penalty in Science and Technology** / Evaluator 1 (30 values)
2. **Advance Market Commitments: Insights from Theory and Experience** / Dan Tortorice (15 values)
3. **Biodiversity Risk** / Evaluator 1 (27 values)
4. **Biodiversity Risk** / Evaluator 2 (27 values)
5. **Existential Risk & Growth** / Evaluator 1 (27 values)
6. **Existential Risk & Growth** / Evaluator 2 (27 values)
7. **Maternal cash transfers for gender equity** / Evaluator 1 (30 values)
8. **Maternal cash transfers for gender equity** / Evaluator 2 (30 values)
9. **The Comparative Impact of Cash Transfers** / Hannah Metzler (18 values)
10. And 29 more...

## Import Instructions for Coda

### Option A: Update Only Changed Rows (Recommended)

**File**: `data/evaluator_paper_level_changes_only.csv` (38 rows)

1. Open Coda document
2. Navigate to the `evaluator_paper_level` table
3. Use Coda's CSV import feature
4. **Match on**: `paper_title` + `evaluator` (composite key)
5. **Update fields**: All rating columns:
   - `adv_knowledge_lower_CI`, `adv_knowledge_middle_rating`, `adv_knowledge_upper_CI`
   - `claims_lower_CI`, `claims_middle_rating`, `claims_upper_CI`
   - `gp_relevance_lower_CI`, `gp_relevance_middle_rating`, `gp_relevance_upper_CI`
   - `journal_predict_lower_CI`, `journal_predict_middle_rating`, `journal_predict_upper_CI`
   - `logic_comms_lower_CI`, `logic_comms_middle_rating`, `logic_comms_upper_CI`
   - `merits_journal_lower_CI`, `merits_journal_middle_rating`, `merits_journal_upper_CI`
   - `methods_lower_CI`, `methods_middle_rating`, `methods_upper_CI`
   - `open_sci_lower_CI`, `open_sci_middle_rating`, `open_sci_upper_CI`
   - `overall_lower_CI`, `overall_middle_rating`, `overall_upper_CI`
   - `real_world_lower_CI`, `real_world_middle_rating`, `real_world_upper_CI`
6. **Action**: Update existing rows (not insert new ones)

### Option B: Replace Entire Table

**File**: `data/evaluator_paper_level_updated.csv` (149 rows)

1. Back up the current Coda table
2. Clear or delete the existing table
3. Import the entire CSV file
4. Verify all columns and data are correct

## Data Sources

The updated values came from:
- **Academic stream form responses**: 104 evaluations
  - File: `data/academic_stream_responses.csv`
  - Coda table: `grid-aDSyEIerdL` (Responses-academic-stream-evaluations)
- **Applied stream form responses**: 9 evaluations
  - File: `data/applied_stream_responses.csv`
  - Coda table: `grid-znNSTj_xX3` (Applied-stream-evaluations)

## Column Mappings

The script automatically mapped form response columns to wide format columns:

### Example: Overall Rating
- Form column: `Overall assessment ranking` → Wide column: `overall_middle_rating`
- Form column: `Lower Cl Overall assessment ranking` → Wide column: `overall_lower_CI`
- Form column: `Upper Cl - Overall assessment ranking` → Wide column: `overall_upper_CI`

### Example: Methods Rating
- Form column: `Methods:  - midpoint ranking` → Wide column: `methods_middle_rating`
- Form column: `Lower Cl - Methods` → Wide column: `methods_lower_CI`
- Form column: `Upper Cl - Methods` → Wide column: `methods_upper_CI`

## Still Missing Data

After this update, there are still **1,635 missing values** (36.6% of rating cells).

These missing values are from:
- Evaluations not yet entered in form response tables
- Evaluations where evaluators didn't provide CIs
- Evaluations that need to be looked up from PubPub

See `PUBPUB_LOOKUP_NEEDED.md` for guidance on finding remaining missing values.

## Verification

To verify the import worked correctly:

1. Check a few sample evaluations in Coda
2. Compare values with `data/academic_stream_responses.csv`
3. Ensure no existing data was overwritten incorrectly
4. Verify the count of non-null values increased by ~582

## Scripts Used

- `code/check_coda_form_responses.py` - Downloaded form responses
- `code/integrate_form_responses_to_wide_format.py` - Main integration script

## Next Steps

1. **Import the data** using Option A (changes only) or Option B (full file)
2. **Verify import** was successful
3. **Look up remaining missing values** from PubPub (see `PUBPUB_LOOKUP_NEEDED.md`)
4. **Re-run export** to update public CSV files with the new data
