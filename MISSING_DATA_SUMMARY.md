# Missing Ratings and CI Values - Recovery Summary

**Last Updated:** December 2025

## Overview

This document summarizes the missing rating and confidence interval values in the Unjournal's `rsx_evalr_rating` table and the data recovery process.

## CRITICAL UPDATE (December 2025)

A comprehensive analysis revealed that the gap between form responses and the rsx_evalr_rating table includes entirely MISSING EVALUATIONS, not just missing values for existing evaluations.

**Discovery:**
- **13 complete evaluations** from form responses were verified as missing from rsx_evalr_rating
- These represent **115 rating rows** (13 evaluations × ~9 criteria each)
- **13 "overall" ratings** missing
- Affects **7 unique published papers**

**Note:** Initial automated extraction found ~75 "missing" evaluations, but most were false positives due to title/name variations (e.g., "Philip Trammell" vs "Phil Trammel", "Evaluator 1" vs "Anon. Evaluator 1"). Manual verification against actual rsx_evalr_rating contents was required.

This is separate from and in addition to the partial missing values documented below.

## Total Missing Data

- **Total ratings with missing values**: 136 out of 859 (15.8%)
  - Missing `middle_rating`: 30
  - Missing `lower_CI`: 134
  - Missing `upper_CI`: 136
- **Affected papers**: 15
- **Affected evaluations**: 25 (paper + evaluator combinations)

## Data Recovered from Coda Form Responses

**Recovered**: 74 ratings across 14 evaluations

**File**: `data/missing_ratings_from_forms.csv`

### Successfully Recovered Evaluations:

1. **Advance Market Commitments: Insights from Theory and Experience**
   - Dan Tortorice: 9 criteria (all with CIs)
   - David Manheim: 3 criteria
   - Joel Tan: 2 criteria

2. **Artificial Intelligence and Economic Growth**
   - Phil Trammel: 3 criteria
   - Seth Benzell: 1 criterion

3. **Banning wildlife trade can boost demand for unregulated threatened species**
   - Anonymous_8: 9 criteria
   - Liew Jia Huan: 9 criteria

4. **Long term cost-effectiveness of resilient foods for global catastrophes**
   - Alex Bates: 1 criterion
   - Anca Hanea: 1 criterion
   - Scott Janzwood: 7 criteria

5. **Money (Not) to Burn: Payments for Ecosystem Services**
   - Anon. evaluator 2 1: 2 criteria

6. **The Comparative Impact of Cash Transfers and a Psychotherapy Program**
   - Hannah Metzler: 9 criteria (all with CIs)

7. **The Environmental Effects of Economic Production**
   - Anonymous_19: 9 criteria
   - Elias Cisneros: 9 criteria

## Data Still Missing (Need to Check PubPub)

**Still Missing**: 62 ratings across 14 evaluations

### Evaluations to Check on PubPub:

1. **Asymmetry in Civic Information: An Experiment on Tax Participation**
   - **Evaluator 2**: overall, merits_journal
   - PubPub URL: https://unjournal.pubpub.org/pub/e2civicasymmetry
   - **Data Found on PubPub**: overall: 75 (65-85), merits_journal: 3.5

2. **Cognitive Behavioral Therapy among Ghana's Rural Poor**
   - **Anon. Evaluator 1**: 9 criteria (all ratings)
   - **Anon. Evaluator 2**: journal_predict, merits_journal

3. **Forecasting Existential Risks: Evidence From a Long-Run Forecasting Tournament**
   - **Anon. evaluation 2**: 7 criteria

4. **Replicability & Generalisability: A Guide to CEA discounts**
   - **Anon. evaluator 1**: 4 criteria
   - **Max Meier**: 4 criteria

5. **Stagnation and Scientific Incentives**
   - **Daniel Lee**: adv_knowledge, methods

6. **The animal welfare cost of meat**
   - **Romain Espinosa**: 8 criteria

7. **The wellbeing cost-effectiveness of StrongMinds and Friendship Bench**
   - **Evaluator 1**: journal_predict, merits_journal

8. **When Celebrities Speak: A Nationwide Twitter Experiment**
   - **Anirugh Tagat**: 9 criteria
   - **Anonymous_14**: 9 criteria

9. **Artificial Intelligence and Economic Growth**
   - **Phil Trammel**: journal_predict
   - **Seth Benzell**: journal_predict

10. **Long term cost-effectiveness of resilient foods**
    - **Scott Janzwood**: methods, open_sci

## Next Steps

1. **Immediate Import**: Import `data/missing_ratings_from_forms.csv` (74 rows) into Coda
   - Match on: `research` + `evaluator` + `criteria`
   - Update fields: `middle_rating`, `lower_CI`, `upper_CI`

2. **Manual Lookup**: For the 14 remaining evaluations, check PubPub to find:
   - Search unjournal.pubpub.org for each paper title
   - Find evaluator-specific pages
   - Extract rating values from "Summary Measures" tables

3. **Create Supplemental File**: After PubPub lookup, create a second CSV with the remaining values

## Files Generated

### Original Files (Partial Missing Values)
- `data/academic_stream_responses.csv` - Full academic stream form responses (104 rows)
- `data/applied_stream_responses.csv` - Full applied stream form responses (9 rows)
- `data/missing_ratings_from_forms.csv` - Recovered ratings ready for import (74 rows)
- `code/extract_missing_ratings_from_coda_forms.py` - Extraction script for partial data

### NEW Files (Completely Missing Evaluations - December 2025)
- `data/missing_evaluations_verified.csv` - **13 verified complete evaluations** ready for import (115 rows)
- `data/new_evaluations_from_forms.csv` - Full extraction with false positives (634 rows, not for import)
- `code/extract_new_evaluations_from_forms_v2.py` - Extraction script (uses correct evaluator identification logic)
- `docs/CODA_IMPORT_INSTRUCTIONS.md` - Step-by-step import guide
- `IMPORT_READY.md` - Quick reference for import process

**Combined Total:** 189 rating rows ready to add to rsx_evalr_rating (115 verified new + 74 missing values)

## Import Instructions for Coda

The file `data/missing_ratings_from_forms.csv` has these columns:
- `research` - Paper title (match key)
- `evaluator` - Evaluator code (match key)
- `criteria` - Rating criterion (match key)
- `middle_rating` - Middle/point estimate
- `lower_CI` - Lower confidence interval
- `upper_CI` - Upper confidence interval

To import:
1. Open Coda table: `rsx_evalr_rating` (grid-pcJr9ZM3wT)
2. Use Coda's merge/update feature
3. Match on the combination of: `research` + `evaluator` + `criteria`
4. Update blank values in: `middle_rating`, `lower_CI`, `upper_CI`
