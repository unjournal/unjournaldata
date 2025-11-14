# PubPub Survey Data Recovery - Import Instructions

## Summary

Successfully scraped **33 evaluations** from PubPub that contain survey response data. After cleaning, recovered:

- **31 responses** with "How long have you been in this field?"
- **25 responses** with "How many proposals, papers, and projects have you evaluated/reviewed?"
- **19 responses** with Field/expertise
- **9 responses** with time spent data
- **4 responses** with process rating data

## Current Coverage in Coda

Your existing Coda data has:
- **111 total survey responses**
- **92 non-null** values for "How long have you been in this field?"
- **90 non-null** values for "How many proposals, papers, and projects have you evaluated/reviewed?"

## Data Recovery Potential

The scraped PubPub data can potentially fill **~19 gaps** for years in field and **~21 gaps** for papers reviewed (accounting for overlap).

## Files Generated

1. **`pubpub_scraped_survey_data.csv`** - Raw scraped data from PubPub (messy, with HTML)
2. **`pubpub_survey_CLEANED_for_coda_import.csv`** - Cleaned data ready for Coda import ⭐

## How to Import into Coda

### Option 1: Manual Review and Import (Recommended)

1. Open `data/pubpub_survey_CLEANED_for_coda_import.csv` in Excel/Google Sheets
2. Review the data quality - particularly these columns:
   - "How long have you been in this field?" (31 values)
   - "How many proposals, papers, and projects have you evaluated/reviewed?" (25 values)
3. For each row, use the `eval_url` to match against existing Coda records
4. Manually copy values into Coda where they're currently missing

### Option 2: Bulk Import with Matching

If you want to automate this:
1. Export your current Coda "Responses: academic stream" table as CSV
2. Match rows by evaluation URL or paper title
3. Fill in missing values from the cleaned PubPub data
4. Re-import to Coda

## Data Quality Notes

### Clean Data ✅
- **Years in field**: Most entries are clean (e.g., "10+", "8 years", "15 years", "20 years")
- **Papers reviewed**: Most entries are clean (e.g., "10+", "200", "25+", "100+", "6", "60")

### Remaining Issues ⚠️
- Some "years in field" responses contain full sentences (e.g., "Eighteen years working on digital advertising, thirty years evangelizing...")
- Field/expertise column still has some HTML fragments
- Some duplicate rows exist (same eval_url appearing multiple times - can be deduplicated)
- Time spent and process rating had very poor extraction rates

## Sample Data

| Paper | Years in Field | Papers Reviewed |
|-------|---------------|-----------------|
| Evaluation 1 of "Does online fundraising..." | 10+ | 10+ |
| Evaluation 2 of "Does online fundraising..." | Eighteen years working on digital advertising... | 200 |
| Evaluation 1 of "Irrigation Strengthens..." | 8 years | 10+ |
| Evaluation 2 of "Irrigation Strengthens..." | 15 years | 25+ |
| Evaluation 1 of "Maternal cash transfers..." | 10 | |
| Evaluation 1 of "A systematic review..." | 20 years | 6 |
| Evaluation 2 of "A systematic review..." | 27 years | 100+ |

## Next Steps

1. ✅ Review `data/pubpub_survey_CLEANED_for_coda_import.csv`
2. ⬜ Deduplicate rows (remove duplicate eval_urls, keeping best data)
3. ⬜ Match against Coda records using eval_url or paper title
4. ⬜ Import missing values into Coda
5. ⬜ Re-run `code/import-unjournal-data.py` to refresh the public CSV
6. ⬜ Re-render the blog post to incorporate new data

## Technical Details

### Scraping Method
- Used RSS feed to enumerate all evaluation summaries
- Extracted individual evaluation links from summary pages
- Scraped survey responses from each evaluation page using BeautifulSoup
- Applied regex patterns to extract structured data from free-text HTML

### Cleaning Method
- Removed HTML navigation elements and junk patterns
- Extracted numeric values from text responses
- Applied field-specific cleaning logic for years vs. papers reviewed
- Truncated overly long responses to 150 characters

### Scripts Used
1. `code/scrape_pubpub_surveys.py` - Web scraping
2. `code/clean_and_merge_survey_data.py` - Data cleaning
