# SQLite Query Examples for Unjournal Database

This document provides example SQL queries for analyzing Unjournal data in the SQLite database.

## Database Location

Default path: `/var/lib/unjournal/unjournal_data.db`

## Opening the Database

```bash
sqlite3 /var/lib/unjournal/unjournal_data.db
```

## Helpful SQLite Commands

```sql
-- Show all tables
.tables

-- Show schema for a specific table
.schema research

-- Enable column headers
.headers on

-- Set output mode to table format
.mode table

-- Export results to CSV
.mode csv
.output results.csv
SELECT * FROM research;
.output stdout

-- Show query execution time
.timer on
```

---

## Basic Queries

### List All Papers

```sql
SELECT
    label_paper_title,
    status,
    doi,
    overall_mean_score
FROM research
ORDER BY label_paper_title;
```

### Top Rated Papers

```sql
SELECT
    label_paper_title,
    overall_mean_score,
    status
FROM research
WHERE overall_mean_score IS NOT NULL
ORDER BY overall_mean_score DESC
LIMIT 10;
```

### Papers by Category

```sql
SELECT
    main_cause_cat as category,
    COUNT(*) as paper_count,
    ROUND(AVG(overall_mean_score), 2) as avg_score
FROM research
WHERE overall_mean_score IS NOT NULL
GROUP BY main_cause_cat
ORDER BY paper_count DESC;
```

### Papers Published This Year

```sql
SELECT
    label_paper_title,
    status,
    created_at
FROM research
WHERE created_at >= date('now', 'start of year')
ORDER BY created_at DESC;
```

---

## Evaluator & Rating Queries

### Evaluators by Number of Reviews

```sql
SELECT
    evaluator,
    COUNT(DISTINCT research) as papers_reviewed,
    COUNT(*) as total_ratings
FROM evaluator_ratings
GROUP BY evaluator
ORDER BY papers_reviewed DESC
LIMIT 20;
```

### Average Ratings by Evaluator

```sql
SELECT
    evaluator,
    COUNT(DISTINCT research) as papers,
    ROUND(AVG(middle_rating), 2) as avg_rating
FROM evaluator_ratings
WHERE criteria = 'overall'
GROUP BY evaluator
HAVING papers >= 2
ORDER BY avg_rating DESC;
```

### Rating Distribution by Criterion

```sql
SELECT
    criteria,
    COUNT(*) as count,
    ROUND(MIN(middle_rating), 2) as min,
    ROUND(AVG(middle_rating), 2) as avg,
    ROUND(MAX(middle_rating), 2) as max
FROM evaluator_ratings
WHERE middle_rating IS NOT NULL
GROUP BY criteria
ORDER BY criteria;
```

### Papers with Multiple Evaluators

```sql
SELECT
    r.label_paper_title,
    COUNT(DISTINCT rt.evaluator) as num_evaluators,
    r.overall_mean_score
FROM research r
LEFT JOIN evaluator_ratings rt
    ON r.label_paper_title = rt.research
GROUP BY r.label_paper_title
HAVING num_evaluators >= 2
ORDER BY num_evaluators DESC;
```

---

## Survey Data Queries

### Evaluator Experience Distribution

```sql
SELECT
    years_in_field,
    COUNT(*) as count
FROM survey_responses
WHERE years_in_field IS NOT NULL
  AND years_in_field != ''
GROUP BY years_in_field
ORDER BY count DESC;
```

### Time Spent on Evaluations

```sql
SELECT
    ROUND(AVG(hours_spent_manual_impute), 1) as avg_hours,
    ROUND(MIN(hours_spent_manual_impute), 1) as min_hours,
    ROUND(MAX(hours_spent_manual_impute), 1) as max_hours,
    COUNT(*) as total_evaluations
FROM survey_responses
WHERE hours_spent_manual_impute IS NOT NULL;
```

### Survey Completion Rate by Stream

```sql
SELECT
    evaluation_stream,
    COUNT(*) as total_surveys,
    SUM(CASE WHEN years_in_field IS NOT NULL THEN 1 ELSE 0 END) as has_years,
    SUM(CASE WHEN papers_reviewed IS NOT NULL THEN 1 ELSE 0 END) as has_papers_reviewed,
    SUM(CASE WHEN time_spent IS NOT NULL THEN 1 ELSE 0 END) as has_time_spent
FROM survey_responses
GROUP BY evaluation_stream;
```

---

## Combined Queries (Joins)

### Papers with Ratings and Authors

```sql
SELECT
    r.label_paper_title,
    r.overall_mean_score,
    GROUP_CONCAT(DISTINCT a.author, '; ') as authors,
    COUNT(DISTINCT rt.evaluator) as num_evaluators
FROM research r
LEFT JOIN paper_authors a ON r.label_paper_title = a.research
LEFT JOIN evaluator_ratings rt ON r.label_paper_title = rt.research
GROUP BY r.label_paper_title
ORDER BY r.overall_mean_score DESC
LIMIT 10;
```

### Evaluator Performance vs. Experience

```sql
SELECT
    epl.evaluator,
    epl.years_in_field,
    epl.papers_reviewed,
    COUNT(*) as num_evaluations,
    ROUND(AVG(epl.overall_rating), 2) as avg_overall_rating
FROM evaluator_paper_level epl
WHERE epl.overall_rating IS NOT NULL
GROUP BY epl.evaluator
HAVING num_evaluations >= 2
ORDER BY num_evaluations DESC;
```

### Rating Consensus Analysis

```sql
-- Papers with high rating variance (disagreement among evaluators)
SELECT
    research,
    COUNT(*) as num_ratings,
    ROUND(AVG(middle_rating), 2) as mean_rating,
    ROUND(MAX(middle_rating) - MIN(middle_rating), 2) as rating_spread
FROM evaluator_ratings
WHERE criteria = 'overall'
  AND middle_rating IS NOT NULL
GROUP BY research
HAVING num_ratings >= 2
ORDER BY rating_spread DESC
LIMIT 10;
```

### Complete Evaluator-Paper Summary

```sql
SELECT
    epl.evaluator,
    epl.paper_title,
    epl.years_in_field,
    epl.papers_reviewed,
    epl.overall_rating,
    epl.methods_rating,
    epl.claims_rating,
    r.main_cause_cat,
    r.doi
FROM evaluator_paper_level epl
LEFT JOIN research r ON epl.paper_title = r.label_paper_title
WHERE epl.overall_rating IS NOT NULL
ORDER BY epl.overall_rating DESC
LIMIT 20;
```

---

## Analysis Queries

### Rating Criteria Correlation

```sql
-- Compare methods and claims ratings
SELECT
    r1.research as paper,
    r1.middle_rating as methods_rating,
    r2.middle_rating as claims_rating,
    ABS(r1.middle_rating - r2.middle_rating) as difference
FROM evaluator_ratings r1
JOIN evaluator_ratings r2
    ON r1.research = r2.research
    AND r1.evaluator = r2.evaluator
WHERE r1.criteria = 'methods'
  AND r2.criteria = 'claims'
  AND r1.middle_rating IS NOT NULL
  AND r2.middle_rating IS NOT NULL
ORDER BY difference DESC
LIMIT 10;
```

### Time Trends

```sql
-- Papers evaluated over time
SELECT
    strftime('%Y-%m', created_at) as month,
    COUNT(*) as papers_added,
    ROUND(AVG(overall_mean_score), 2) as avg_score
FROM research
WHERE created_at IS NOT NULL
GROUP BY month
ORDER BY month DESC;
```

### Export Metadata Analysis

```sql
-- Track export history
SELECT
    table_name,
    row_count,
    export_timestamp,
    status
FROM export_metadata
WHERE status = 'success'
ORDER BY export_timestamp DESC
LIMIT 20;
```

---

## Data Quality Checks

### Missing Ratings

```sql
-- Papers without overall ratings
SELECT
    label_paper_title,
    status
FROM research
WHERE overall_mean_score IS NULL
  AND status LIKE '%published%'
ORDER BY label_paper_title;
```

### Incomplete Evaluations

```sql
-- Evaluations with ratings but no survey data
SELECT
    rt.research,
    rt.evaluator,
    COUNT(DISTINCT rt.criteria) as num_criteria
FROM evaluator_ratings rt
LEFT JOIN survey_responses sr
    ON rt.research = sr.paper_title
WHERE sr.paper_title IS NULL
GROUP BY rt.research, rt.evaluator
ORDER BY num_criteria DESC;
```

### Survey Response Rates

```sql
SELECT
    COUNT(*) as total_responses,
    SUM(CASE WHEN years_in_field IS NOT NULL AND years_in_field != '' THEN 1 ELSE 0 END) as has_experience,
    SUM(CASE WHEN field_expertise IS NOT NULL AND field_expertise != '' THEN 1 ELSE 0 END) as has_expertise,
    ROUND(100.0 * SUM(CASE WHEN years_in_field IS NOT NULL THEN 1 ELSE 0 END) / COUNT(*), 1) as experience_pct
FROM survey_responses;
```

---

## Export Queries

### Export to CSV for Analysis

```sql
.mode csv
.output paper_ratings_summary.csv

SELECT
    r.label_paper_title,
    r.main_cause_cat,
    r.overall_mean_score,
    COUNT(DISTINCT rt.evaluator) as num_evaluators,
    r.doi,
    r.research_url
FROM research r
LEFT JOIN evaluator_ratings rt ON r.label_paper_title = rt.research
GROUP BY r.label_paper_title
ORDER BY r.overall_mean_score DESC;

.output stdout
```

### Export Evaluator Summary

```sql
.mode csv
.output evaluator_summary.csv

SELECT
    evaluator,
    years_in_field,
    papers_reviewed,
    COUNT(*) as num_evaluations,
    ROUND(AVG(overall_rating), 2) as avg_rating,
    MIN(date_entered) as first_evaluation,
    MAX(date_entered) as last_evaluation
FROM evaluator_paper_level
GROUP BY evaluator
ORDER BY num_evaluations DESC;

.output stdout
```

---

## Advanced Queries

### Nested Query: Papers Above Average

```sql
SELECT
    label_paper_title,
    overall_mean_score,
    ROUND(overall_mean_score - (SELECT AVG(overall_mean_score) FROM research WHERE overall_mean_score IS NOT NULL), 2) as above_avg
FROM research
WHERE overall_mean_score > (
    SELECT AVG(overall_mean_score)
    FROM research
    WHERE overall_mean_score IS NOT NULL
)
ORDER BY above_avg DESC;
```

### Window Function: Ranking Papers

```sql
SELECT
    label_paper_title,
    main_cause_cat,
    overall_mean_score,
    RANK() OVER (ORDER BY overall_mean_score DESC) as overall_rank,
    RANK() OVER (PARTITION BY main_cause_cat ORDER BY overall_mean_score DESC) as category_rank
FROM research
WHERE overall_mean_score IS NOT NULL
ORDER BY overall_rank
LIMIT 20;
```

### Common Table Expression (CTE)

```sql
WITH evaluator_stats AS (
    SELECT
        evaluator,
        COUNT(*) as num_ratings,
        AVG(middle_rating) as avg_rating
    FROM evaluator_ratings
    WHERE criteria = 'overall' AND middle_rating IS NOT NULL
    GROUP BY evaluator
)
SELECT
    es.evaluator,
    es.num_ratings,
    ROUND(es.avg_rating, 2) as avg_rating,
    sr.years_in_field,
    sr.papers_reviewed
FROM evaluator_stats es
LEFT JOIN survey_responses sr ON 1=1  -- Note: would need proper join key
WHERE es.num_ratings >= 3
ORDER BY es.num_ratings DESC;
```

---

## Backup and Maintenance Queries

### Database Statistics

```sql
-- Table sizes
SELECT
    name as table_name,
    (SELECT COUNT(*) FROM sqlite_master WHERE type='index' AND tbl_name=m.name) as num_indexes
FROM sqlite_master m
WHERE type='table'
ORDER BY name;
```

### Vacuum Database (Reclaim Space)

```sql
-- Run this periodically to optimize database
VACUUM;
```

### Check Database Integrity

```sql
PRAGMA integrity_check;
```

---

## Tips & Best Practices

1. **Use EXPLAIN QUERY PLAN** to optimize slow queries:
   ```sql
   EXPLAIN QUERY PLAN
   SELECT * FROM research WHERE overall_mean_score > 80;
   ```

2. **Index commonly queried columns** (already created by export script):
   - `evaluator_ratings(research, evaluator, criteria)`
   - `paper_authors(research)`
   - `evaluator_paper_level(evaluator, paper_title)`

3. **Use LIMIT** for large result sets to avoid memory issues

4. **Transaction safety** for bulk updates:
   ```sql
   BEGIN TRANSACTION;
   -- Your updates here
   COMMIT;
   ```

5. **Backup before major queries**:
   ```bash
   sqlite3 /var/lib/unjournal/unjournal_data.db ".backup backup_$(date +%Y%m%d).db"
   ```

---

## Additional Resources

- SQLite Documentation: https://sqlite.org/docs.html
- SQLite Tutorial: https://www.sqlitetutorial.net/
- GitHub Repository: https://github.com/unjournal/unjournaldata
- Support: Open an issue at https://github.com/unjournal/unjournaldata/issues
