# Missing Evaluations Import Summary

**Date:** December 30, 2025
**Status:** ✅ VERIFIED AND READY FOR IMPORT

## Quick Facts

**Missing Evaluations Found:** 13 evaluations from form responses are not in rsx_evalr_rating table

**Data Generated:**
- File: `data/missing_evaluations_verified.csv` (FINAL - import this)
- Total rows: 115 rating rows
- Breakdown: 13 evaluations across 7 published papers

**Expected Impact:**
- rsx_evalr_rating rows: **859 → 974** (+115)
- Total evaluations: **94 → 107** (+13)
- Overall ratings: **94 → 107** (+13)

---

## What Was Found

### Verified Missing Evaluations (13 total)

| Paper | Evaluations | Rows |
|-------|-------------|------|
| Adjusting for Scale-Use Heterogeneity in Self-Reported Well-Being | 2 | 20 |
| Maternal cash transfers for gender equity and child development | 2 | 20 |
| Irrigation Strengthens Climate Resilience | 2 | 20 |
| Ends versus Means: Kantians, Utilitarians, and Moral Decisions | 2 | 20 |
| Does online fundraising increase charitable giving? | 2 | 16 |
| Forecasts estimate limited cultured meat production through 2050 | 2 | 9 |
| A systematic review and meta-analysis of social safety nets | 1 | 10 |

**Total: 13 evaluations across 7 papers**

---

## Why This Happened

**The Gap:**
1. Evaluators submit ratings via Coda forms (academic/applied stream tables)
2. **No automated sync** exists from forms → rsx_evalr_rating table
3. Forms accumulated 113 responses, but only 94 evaluations made it to rsx_evalr_rating
4. **13 evaluations were never transferred**

**The Challenge:**
Initial automated extraction found ~75 "missing" evaluations, but most were false positives due to:
- **Title variations**: "Existential Risk & Growth" vs "Existential risk and growth"
- **Name variations**: "Philip Trammell" vs "Phil Trammel", "Jia Huan Liew" vs "Liew Jia Huan"
- **Manual prefixes**: "Evaluator 1" vs "Anon. Evaluator 1"

**The Fix:**
Created `code/extract_new_evaluations_from_forms_v2.py` which:
- Reads form responses directly from Coda API
- Uses "Identification as an author" field for evaluator names
- Assigns "Evaluator 1", "Evaluator 2", etc. when identification is blank (by date order)
- Extracts all 10 rating criteria per evaluation
- **Manual verification** against actual rsx_evalr_rating contents to filter false positives

---

## What Was Excluded

The following were found in forms but **excluded** from import:

1. **Deadweight Losses or Gains** - Not yet public
2. **Mental Health Therapy** - Paper name changed, needs manual review
3. **Yellow Vests** - Independent evaluation, not part of published packages
4. **~60+ other evaluations** - Already exist in rsx_evalr_rating (with name/title variations)

---

## How to Import

### Step 1: Review the CSV
```bash
# Check the file
head -20 data/missing_evaluations_verified.csv
wc -l data/missing_evaluations_verified.csv
```

### Step 2: Import to Coda
1. Open https://coda.io/d/_d0KBG3dSZCs/Evals-Ratings_su3Mx_O0
2. Go to "rsx-evalr-rating" table (grid-pcJr9ZM3wT)
3. Click **"..."** menu → **"Import data"** → **"From CSV"**
4. Upload `data/missing_evaluations_verified.csv`

### Step 3: Map Columns
- `research` → research
- `evaluator` → evaluator
- `criteria` → criteria
- `middle_rating` → middle_rating
- `lower_CI` → lower_CI
- `upper_CI` → upper_CI
- `confidence_level` → confidence_level
- `row_created_date` → row_created_date

### Step 4: Import Settings
- **Mode:** "Add as new rows" (these are completely new evaluations)
- **Do NOT** select "Update existing rows"

### Step 5: Verify
After import:
- Total row count: should be ~974
- Filter by criteria = "overall": should be ~107 rows
- Search for "Adjusting for Scale-Use Heterogeneity": should find 2 evaluations
- Search for "Ends versus Means": should find 2 evaluations

---

## Post-Import Steps

### 1. Update Local CSV Export
Run the daily import script to sync the updated Coda data:
```bash
python3 code/import-unjournal-data.py
```

### 2. Update SQLite Database (Linode)
The cron job will auto-update at 2:00 AM UTC, or manually trigger:
```bash
ssh root@45.79.160.157
python3 /var/lib/unjournal/export_to_sqlite.py
```

### 3. Commit to GitHub
```bash
git add data/missing_evaluations_verified.csv
git add data/rsx_evalr_rating.csv
git commit -m "Add 13 missing evaluations from form responses to rsx_evalr_rating

- Imported 115 rating rows for 7 published papers
- Increases overall ratings from 94 to 107
- Verified against existing rsx_evalr_rating entries
- Excluded unpublished/independent evaluations"
git push
```

---

## Technical Details

### Evaluator Naming Logic
The script follows Unjournal conventions:

1. Check "Identification as an author" field
2. If provided (and not "No"), use that name
3. If blank, assign sequential numbers per paper based on submission date:
   - First submission → "Evaluator 1"
   - Second submission → "Evaluator 2"
   - etc.

### Rating Criteria Extracted
For each evaluation, up to 10 criteria:
- overall
- adv_knowledge
- claims
- methods
- logic_comms
- open_sci
- real_world
- gp_relevance
- merits_journal
- journal_predict

**Note:** Not all evaluations have all criteria (some evaluators skipped certain fields)

---

## Files Reference

| File | Purpose | Rows |
|------|---------|------|
| `code/extract_new_evaluations_from_forms_v2.py` | Extraction script (corrected) | - |
| `data/missing_evaluations_verified.csv` | **Import this to Coda** | 115 |
| `data/new_evaluations_from_forms.csv` | Full extraction (has false positives) | 634 |
| `docs/IMPORT_SUMMARY.md` | This file | - |
| `IMPORT_READY.md` | Quick reference guide | - |

---

## Questions?

- Script issues: Check script output for error messages
- Import problems: Review Coda import logs
- GitHub: https://github.com/unjournal/unjournaldata/issues
