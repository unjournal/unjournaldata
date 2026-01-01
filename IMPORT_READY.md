# Ready to Import: Missing Evaluations

**Date:** December 30, 2025
**Status:** ✅ VERIFIED AND READY FOR IMPORT

---

## Summary

**13 missing evaluations** from published evaluation packages have been extracted from form responses and are ready to import into the rsx_evalr_rating table.

**File to import:** `data/missing_evaluations_verified.csv`
**Total rows:** 115 rating rows
**Impact:** Will increase "overall" ratings from 94 to **107** (+13)

---

## What's Missing

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

## How to Import

### Step 1: Review the File
```bash
head -20 data/missing_evaluations_verified.csv
wc -l data/missing_evaluations_verified.csv
```

### Step 2: Import to Coda
1. Open https://coda.io/d/_d0KBG3dSZCs/Evals-Ratings_su3Mx_O0
2. Navigate to "rsx-evalr-rating" table (grid-pcJr9ZM3wT)
3. Click **"..."** → **"Import data"** → **"From CSV"**
4. Upload `data/missing_evaluations_verified.csv`

### Step 3: Map Columns
Map the CSV columns to table columns:
- research → research
- evaluator → evaluator
- criteria → criteria
- middle_rating → middle_rating
- lower_CI → lower_CI
- upper_CI → upper_CI
- confidence_level → confidence_level
- row_created_date → row_created_date

### Step 4: Import Settings
- **Mode:** "Add as new rows"
- **Do NOT** select "Update existing rows"

### Step 5: Verify After Import
- Total rows in rsx_evalr_rating: should increase from 859 to **974** (+115)
- Overall ratings: should increase from 94 to **107** (+13)
- Search for "Adjusting for Scale-Use Heterogeneity" → should find 2 evaluations

---

## Sample Evaluations Being Added

**Adjusting for Scale-Use Heterogeneity in Self-Reported Well-Being:**
- Alberto Prati (10 criteria)
- Caspar Kaiser (10 criteria)

**Ends versus Means: Kantians, Utilitarians, and Moral Decisions:**
- Valerio Capraro (10 criteria)
- dhj (10 criteria)

**Irrigation Strengthens Climate Resilience:**
- Evaluator 1 (10 criteria)
- Evaluator 2 (10 criteria)

**Maternal cash transfers:**
- Evaluator 1 (10 criteria)
- Reviewer1 (10 criteria)

**Forecasts estimate limited cultured meat:**
- Evaluator 1 (1 criterion)
- PseudonymNotSaltedHash (8 criteria)

---

## What Was Excluded

The following were found in forms but **excluded** from import:

1. **Deadweight Losses or Gains** - Not yet public
2. **Mental Health Therapy** - Paper name changed, needs manual review
3. **Yellow Vests** - Independent evaluation, not part of published packages
4. **~60+ other evaluations** - Already exist in rsx_evalr_rating (with name/title variations)

---

## Post-Import Steps

### 1. Update Local CSV
```bash
python3 code/import-unjournal-data.py
```

### 2. Update SQLite Database (Linode)
Will auto-update at 2:00 AM UTC, or manually:
```bash
ssh root@45.79.160.157
python3 /var/lib/unjournal/export_to_sqlite.py
```

### 3. Commit to GitHub
```bash
git add data/missing_evaluations_verified.csv
git add data/rsx_evalr_rating.csv
git commit -m "Add 13 missing evaluations from form responses

- Imported 115 rating rows for 7 published papers
- Increases overall ratings from 94 to 107
- Verified against existing rsx_evalr_rating entries
- Excluded unpublished/independent evaluations"
git push
```

---

## Technical Notes

### Why So Many False Matches?

The original extraction found ~75 "missing" evaluations, but most were false positives due to:

**Title Variations:**
- "Existential Risk & Growth" (forms) vs "Existential risk and growth" (rsx_evalr_rating)
- "Pharmaceutical Pricing, and R&D" vs "Pharmaceutical Pricing and R&D"
- "Choose Your Moments: NIH" vs "Choose Your Moments: [NIH]"

**Evaluator Name Variations:**
- "Philip Trammell" (forms) → "Phil Trammel" (rsx_evalr_rating)
- "Jia Huan Liew" → "Liew Jia Huan" (name order reversed)
- "Evaluator 1" (forms) → "Anon. Evaluator 1" (manual prefix added in rsx_evalr_rating)

### Solution: Manual Verification

Rather than trying to perfect automated fuzzy matching, we:
1. Extracted all possible missing evaluations
2. Cross-referenced against the actual rsx_evalr_rating table contents
3. Manually filtered to confirmed missing papers
4. Created verified CSV with only genuine gaps

---

## Files Reference

| File | Description | Rows |
|------|-------------|------|
| `data/missing_evaluations_verified.csv` | **IMPORT THIS** | 115 |
| `data/new_evaluations_from_forms.csv` | Full extraction (has false positives) | 634 |
| `code/extract_new_evaluations_from_forms_v2.py` | Extraction script | - |
| `IMPORT_READY.md` | This file | - |

---

## Questions?

- Import issues: Review Coda import logs for errors
- Data questions: Check `code/extract_new_evaluations_from_forms_v2.py` output
- GitHub: https://github.com/unjournal/unjournaldata/issues
