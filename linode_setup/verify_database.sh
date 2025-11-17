#!/bin/bash

# Unjournal Database Verification Script
# Shows database schema, row counts, and sample data

DB_PATH="/var/lib/unjournal/unjournal_data.db"

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo "========================================"
echo "Unjournal Database Verification"
echo "========================================"
echo ""

# Check if database exists
if [ ! -f "$DB_PATH" ]; then
    echo "❌ Database not found at $DB_PATH"
    echo "   Run sync_cron.sh first to create the database"
    exit 1
fi

# Database info
echo "Database: $DB_PATH"
DB_SIZE=$(du -h "$DB_PATH" | cut -f1)
echo "Size: $DB_SIZE"
echo ""

# Show tables and row counts
echo "========================================"
echo "DATABASE SCHEMA & ROW COUNTS"
echo "========================================"

sqlite3 "$DB_PATH" << 'EOF'
.mode column
.headers on

SELECT
    'Table Name' as heading,
    'Rows' as count_heading;

SELECT 'research' as table_name, COUNT(*) as rows FROM research
UNION ALL SELECT 'evaluator_ratings', COUNT(*) FROM evaluator_ratings
UNION ALL SELECT 'paper_authors', COUNT(*) FROM paper_authors
UNION ALL SELECT 'survey_responses', COUNT(*) FROM survey_responses
UNION ALL SELECT 'evaluator_paper_level', COUNT(*) FROM evaluator_paper_level
UNION ALL SELECT 'researchers_evaluators', COUNT(*) FROM researchers_evaluators
UNION ALL SELECT 'export_metadata', COUNT(*) FROM export_metadata;
EOF

echo ""
echo "========================================"
echo "TABLE SCHEMAS"
echo "========================================"
echo ""

sqlite3 "$DB_PATH" << 'EOF'
.mode line

SELECT '--- RESEARCH TABLE ---' as separator;
.schema research

SELECT '' as blank;
SELECT '--- EVALUATOR_RATINGS TABLE ---' as separator;
.schema evaluator_ratings

SELECT '' as blank;
SELECT '--- PAPER_AUTHORS TABLE ---' as separator;
.schema paper_authors

SELECT '' as blank;
SELECT '--- SURVEY_RESPONSES TABLE ---' as separator;
.schema survey_responses

SELECT '' as blank;
SELECT '--- EVALUATOR_PAPER_LEVEL TABLE ---' as separator;
.schema evaluator_paper_level
EOF

echo ""
echo "========================================"
echo "SAMPLE DATA"
echo "========================================"
echo ""

echo "Top 3 papers by overall score:"
sqlite3 "$DB_PATH" << 'EOF'
.mode column
.headers on
SELECT
    label_paper_title,
    overall_mean_score,
    status
FROM research
WHERE overall_mean_score IS NOT NULL
ORDER BY overall_mean_score DESC
LIMIT 3;
EOF

echo ""
echo "Evaluator activity:"
sqlite3 "$DB_PATH" << 'EOF'
.mode column
.headers on
SELECT
    evaluator,
    COUNT(DISTINCT research) as papers_evaluated,
    COUNT(*) as total_ratings
FROM evaluator_ratings
GROUP BY evaluator
ORDER BY papers_evaluated DESC
LIMIT 5;
EOF

echo ""
echo "========================================"
echo "EXPORT HISTORY"
echo "========================================"

sqlite3 "$DB_PATH" << 'EOF'
.mode column
.headers on
SELECT
    table_name,
    row_count,
    export_timestamp,
    status
FROM export_metadata
ORDER BY export_timestamp DESC
LIMIT 10;
EOF

echo ""
echo "========================================"
echo "✓ Verification Complete"
echo "========================================"
echo ""
echo "Query examples: see docs/SQLITE_QUERIES.md"
echo "Access database: sqlite3 $DB_PATH"
echo ""
