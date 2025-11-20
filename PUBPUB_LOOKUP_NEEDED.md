# PubPub Manual Lookup Required

## Evaluations Still Missing Data - PubPub URLs to Check

These 14 evaluations have missing ratings that couldn't be found in Coda form responses. They likely exist on PubPub and need manual lookup.

---

### 1. Asymmetry in Civic Information: An Experiment on Tax Participation among Informal Firms in Togo

**Evaluator 2** - Missing: `overall`, `merits_journal`

- Evaluation URL: https://unjournal.pubpub.org/pub/e2civicasymmetry
- **Data already found**:
  - overall: 75 (lower: 65, upper: 85)
  - merits_journal: 3.5 (no CI)

---

### 2. Cognitive Behavioral Therapy among Ghana's Rural Poor Is Effective Regardless of Baseline Mental Distress

**Anon. Evaluator 1** - Missing: `adv_knowledge`, `methods`, `logic_comms`, `real_world`, `gp_relevance`, `open_sci`, `merits_journal`, `overall`, `journal_predict`

- Search for: "Cognitive Behavioral Therapy Ghana"
- Look for anonymous evaluator pages

**Anon. Evaluator 2** - Missing: `merits_journal`, `journal_predict`

- Same paper, different evaluator

---

### 3. Forecasting Existential Risks: Evidence From a Long-Run Forecasting Tournament

**Anon. evaluation 2** - Missing: `adv_knowledge`, `methods`, `logic_comms`, `open_sci`, `real_world`, `gp_relevance`, `overall`

- Search for: "Forecasting Existential Risks"

---

### 4. Replicability & Generalisability: A Guide to CEA discounts

**Anon. evaluator 1** - Missing: `journal_predict`, `merits_journal`, `methods`, `real_world`

- Search for: "Replicability Generalisability CEA discounts"

**Max Meier** - Missing: `journal_predict`, `merits_journal`, `open_sci`, `real_world`

- Same paper, different evaluator

---

### 5. Stagnation and Scientific Incentives

**Daniel Lee** - Missing: `adv_knowledge`, `methods`

- Search for: "Stagnation Scientific Incentives"

---

### 6. The animal welfare cost of meat: evidence from a survey of hypothetical scenarios among Belgian consumers

**Romain Espinosa** - Missing: `adv_knowledge`, `claims`, `methods`, `logic_comms`, `open_sci`, `real_world`, `gp_relevance`, `overall`

- Search for: "animal welfare cost of meat Belgian"

---

### 7. The wellbeing cost-effectiveness of StrongMinds and Friendship Bench

**Evaluator 1** - Missing: `merits_journal`, `journal_predict`

- Search for: "StrongMinds Friendship Bench"

---

### 8. When Celebrities Speak: A Nationwide Twitter Experiment Promoting Vaccination In Indonesia

**Anirugh Tagat** - Missing: `adv_knowledge`, `methods`, `logic_comms`, `real_world`, `gp_relevance`, `journal_predict`, `open_sci`, `merits_journal`, `overall`

- Search for: "Celebrities Twitter Vaccination Indonesia"

**Anonymous_14** - Missing: `adv_knowledge`, `methods`, `logic_comms`, `real_world`, `gp_relevance`, `journal_predict`, `open_sci`, `merits_journal`, `overall`

- Same paper, different evaluator

---

### 9. Artificial Intelligence and Economic Growth

**Phil Trammel** - Missing: `journal_predict`

- Search for: "Artificial Intelligence Economic Growth"

**Seth Benzell** - Missing: `journal_predict`

- Same paper, different evaluator

---

### 10. Long term cost-effectiveness of resilient foods for global catastrophes compared to artificial general intelligence safety

**Scott Janzwood** - Missing: `methods`, `open_sci`

- Search for: "resilient foods global catastrophes"

---

## How to Look Up Data on PubPub

1. Go to https://unjournal.pubpub.org
2. Search for the paper title (use keywords from above)
3. Look for evaluation links (usually labeled "Evaluator 1", "Evaluator 2", or evaluator names)
4. On each evaluation page, look for "Summary Measures" or "Quantitative Ratings" table
5. Extract:
   - **Overall assessment**: Usually shown as "XX/100" with CI range
   - **Journal rank tier**: Usually shown as "X.X/5"
   - **Other criteria**: Look for detailed metrics section

## Data Format Needed

For each missing rating, record:
- Paper title
- Evaluator name
- Criterion name
- Middle rating
- Lower CI (if available)
- Upper CI (if available)

## Template for Recording Data

```csv
research,evaluator,criteria,middle_rating,lower_CI,upper_CI
"Paper Title",Evaluator Name,overall,75,65,85
"Paper Title",Evaluator Name,merits_journal,3.5,,
```

Save as: `data/missing_ratings_from_pubpub.csv`

Then combine with `data/missing_ratings_from_forms.csv` for complete import.
