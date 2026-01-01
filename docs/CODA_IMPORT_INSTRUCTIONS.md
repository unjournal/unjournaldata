# Importing Missing Evaluations into Coda's rsx_evalr_rating Table

This guide explains how to import missing evaluation ratings from form responses into Coda's `rsx_evalr_rating` table.

## Background

The Unjournal has two sources of evaluation data:

1. **rsx_evalr_rating table** (grid-pcJr9ZM3wT) - The aggregated ratings table
2. **Form responses** - Academic and applied stream evaluation forms where evaluators submit ratings

Historically, there has been a gap: evaluations submitted via forms were not automatically flowing into the rsx_evalr_rating aggregation table. This guide shows how to bridge that gap.

---

## Two Types of Missing Data

### Type 1: Completely New Evaluations
**File:** `data/new_evaluations_from_forms.csv`
**Script:** `code/extract_new_evaluations_from_forms.py`

These are evaluations that exist in form responses but have NO rows at all in rsx_evalr_rating.

**Current Status (as of script run):**
- 50 missing evaluations
- 440 rating rows to add
- 49 "overall" ratings to add

### Type 2: Partial Evaluations (Missing Values)
**File:** `data/missing_ratings_from_forms.csv`
**Script:** `code/extract_missing_ratings_from_coda_forms.py`

These are evaluations that exist in rsx_evalr_rating but are missing some rating values (e.g., missing confidence intervals).

---

## Import Process

### For Type 1: New Evaluations (Recommended First)

These evaluations don't exist in the table at all, so you can safely add them.

#### Step 1: Open the rsx_evalr_rating Table
1. Go to https://coda.io/d/_d0KBG3dSZCs/Evals-Ratings_su3Mx_O0
2. Navigate to the "rsx-evalr-rating" table (grid-pcJr9ZM3wT)

#### Step 2: Import CSV
1. Click the **"..."** menu at the top right of the table
2. Select **"Import data"** → **"From CSV"**
3. Upload `data/new_evaluations_from_forms.csv`

#### Step 3: Map Columns
Map CSV columns to table columns:
- `research` → research
- `evaluator` → evaluator
- `criteria` → criteria
- `middle_rating` → middle_rating
- `lower_CI` → lower_CI
- `upper_CI` → upper_CI
- `confidence_level` → confidence_level
- `row_created_date` → row_created_date

#### Step 4: Choose Import Method
- Select **"Add as new rows"** (since these are completely new evaluations)
- **Do NOT** select "Update existing rows" for this import

#### Step 5: Verify Import
After import, check:
- Total rows should increase from **859 to ~1,299** (+440 rows)
- "Overall" ratings should increase from **94 to ~143** (+49 ratings)
- Unique papers with ratings should increase from **49 to ~87**

#### Step 6: Spot Check
Manually verify a few entries:
1. Search for "Adjusting for Scale-Use Heterogeneity" - should now have 2 evaluations
2. Search for "Ends versus Means" - should now have 2 evaluations
3. Check that ratings have proper confidence intervals where available

---

### For Type 2: Missing Values (Optional, After Type 1)

Only do this if you also want to fill in missing values for existing evaluations.

#### Step 1: Open the rsx_evalr_rating Table
Same as above.

#### Step 2: Import CSV
1. Click **"..."** menu → **"Import data"** → **"From CSV"**
2. Upload `data/missing_ratings_from_forms.csv`

#### Step 3: Map Columns
Same column mapping as Type 1.

#### Step 4: Choose Import Method
- Select **"Update existing rows"**
- Match on: `research` + `evaluator` + `criteria` (composite key)
- Update: `middle_rating`, `lower_CI`, `upper_CI`
- **Important:** Configure to only update blank/null values (don't overwrite existing data)

#### Step 5: Verify
- Check that existing ratings weren't changed
- Verify that previously blank confidence intervals now have values

---

## Validation Queries

After import, run these checks to verify success:

### Check 1: Total Evaluation Count
```
Count unique (research, evaluator) combinations
Expected: ~145 (95 original + 50 new)
```

### Check 2: Overall Ratings Count
```
Filter by: criteria = "overall"
Count rows
Expected: ~143 (94 original + 49 new)
```

### Check 3: Papers with Ratings
```
Count unique papers in research column
Expected: ~87 (49 original + 38 new unique papers)
```

### Check 4: Verify Specific Papers
Check these papers that were previously missing:

1. **Adjusting for Scale-Use Heterogeneity in Self-Reported Well-Being**
   - Should have 2 evaluations (Prati, Friedrich)

2. **Ends versus Means: Kantians, Utilitarians, and Moral Decisions**
   - Should have 2 evaluations (ValerioCapraro, dhj)

3. **Does online fundraising increase charitable giving?**
   - Should have 2 evaluations (Feynman, tabare)

4. **Forecasts estimate limited cultured meat production through 2050**
   - Should have 2 evaluations (-, PseudonymNotSaltedHash)

5. **Irrigation Strengthens Climate Resilience**
   - Should have 2 evaluations (Ag space adventurer, Adam Smith)

6. **Social Safety Nets, Women's Economic...**
   - Should have 1 evaluation (wheeler)

---

## Troubleshooting

### Problem: Import fails with "Duplicate key" error
**Cause:** Some evaluations may already exist in the table
**Solution:**
1. Re-run the extraction script to get fresh data
2. Or manually filter out duplicates from the CSV before importing

### Problem: Column mapping doesn't match
**Cause:** Column names may have changed in Coda table
**Solution:**
1. Check actual column names in the rsx_evalr_rating table
2. Update the mapping accordingly
3. Or edit the CSV headers to match Coda column names exactly

### Problem: Confidence intervals show as null
**Cause:** Some evaluations don't have confidence intervals in form responses
**Solution:** This is expected - not all evaluators provided CIs. Leave as null.

### Problem: Numbers are too high/low
**Cause:** Possible data duplication or incorrect filtering
**Solution:**
1. Check for duplicate rows in Coda
2. Use the "row_created_date" field to identify recently imported rows
3. Delete and re-import if necessary

---

## Post-Import Steps

### 1. Update GitHub Repository
After successful import, run the daily import script to update the GitHub CSV exports:
```bash
python3 code/import-unjournal-data.py
```

This will update `data/rsx_evalr_rating.csv` with the newly imported data.

### 2. Update SQLite Database (Linode)
The nightly cron job will automatically update the SQLite database with the new data at 2:00 AM UTC.

Or manually trigger:
```bash
ssh root@45.79.160.157
python3 /var/lib/unjournal/export_to_sqlite.py
```

### 3. Commit Changes to GitHub
```bash
git add data/rsx_evalr_rating.csv
git commit -m "Update rsx_evalr_rating with 50 missing evaluations from forms

- Added 440 rating rows from form responses
- Increased overall ratings from 94 to 143
- Now includes evaluations for 38 additional papers"
git push
```

---

## Files Reference

| File | Purpose | Generated By |
|------|---------|--------------|
| `data/new_evaluations_from_forms.csv` | Completely new evaluations to import | `code/extract_new_evaluations_from_forms.py` |
| `data/missing_ratings_from_forms.csv` | Missing values for existing evaluations | `code/extract_missing_ratings_from_coda_forms.py` |
| `data/rsx_evalr_rating.csv` | Current export of rsx_evalr_rating table | `code/import-unjournal-data.py` |

---

## Expected Final State

After importing both Type 1 and Type 2:

| Metric | Before | After Type 1 | After Type 2 |
|--------|--------|--------------|--------------|
| Total rows | 859 | ~1,299 | ~1,300+ |
| Total evaluations | 95 | ~145 | ~145 |
| Overall ratings | 94 | ~143 | ~143 |
| Unique papers | 49 | ~87 | ~87 |
| Published papers covered | 49/56 | ~55/56 | ~55/56 |

**Remaining gap:** 1 paper still missing (requires PubPub scraping)
- "Cash Transfers for Child Development: Experimental Evidence from India"

---

## Questions?

For issues or questions:
- Check `MISSING_DATA_SUMMARY.md` for background on missing data analysis
- Review script output logs for details on what was extracted
- GitHub Issues: https://github.com/unjournal/unjournaldata/issues
