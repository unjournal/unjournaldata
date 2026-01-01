#!/bin/bash
#
# Cron script to extract missing evaluations from Coda form responses
# This runs on Linode server to keep data private (not committed to public GitHub)
#
# Installed location: /var/lib/unjournal/extract_missing_evals_cron.sh
# Cron schedule: Daily at 2:30 AM UTC (after SQLite export completes)
#

set -e

# Configuration
UNJOURNAL_DIR="/var/lib/unjournal"
OUTPUT_DIR="${UNJOURNAL_DIR}/missing_evaluations"
LOG_FILE="/var/log/unjournal/extract_missing_evals.log"
SCRIPT_PATH="${UNJOURNAL_DIR}/unjournaldata/code/extract_new_evaluations_from_forms_v2.py"
ENV_FILE="${UNJOURNAL_DIR}/.env"

# Ensure output directory exists
mkdir -p "${OUTPUT_DIR}"
mkdir -p "$(dirname ${LOG_FILE})"

# Log function
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "${LOG_FILE}"
}

log "=========================================="
log "Starting missing evaluations extraction"
log "=========================================="

# Load environment variables (CODA_API_KEY)
if [ -f "${ENV_FILE}" ]; then
    source "${ENV_FILE}"
    log "Loaded environment from ${ENV_FILE}"
else
    log "ERROR: Environment file not found: ${ENV_FILE}"
    exit 1
fi

# Verify CODA_API_KEY is set
if [ -z "${CODA_API_KEY}" ]; then
    log "ERROR: CODA_API_KEY not set in environment"
    exit 1
fi

# Change to repo directory
cd "${UNJOURNAL_DIR}/unjournaldata" || {
    log "ERROR: Could not change to repo directory"
    exit 1
}

# Pull latest code from GitHub (public repo - just the extraction script logic)
log "Pulling latest code from GitHub..."
git pull origin main >> "${LOG_FILE}" 2>&1 || {
    log "WARNING: Git pull failed, using existing code"
}

# Run the extraction script
log "Running extraction script..."
python3 "${SCRIPT_PATH}" > "${OUTPUT_DIR}/extraction_output.txt" 2>&1
EXIT_CODE=$?

if [ ${EXIT_CODE} -eq 0 ]; then
    log "✓ Extraction completed successfully"

    # Check if new evaluations were found
    if [ -f "data/new_evaluations_from_forms.csv" ]; then
        # Copy to output directory with timestamp
        TIMESTAMP=$(date '+%Y%m%d_%H%M%S')
        cp "data/new_evaluations_from_forms.csv" "${OUTPUT_DIR}/new_evaluations_${TIMESTAMP}.csv"
        cp "data/new_evaluations_from_forms.csv" "${OUTPUT_DIR}/new_evaluations_latest.csv"

        # Count evaluations
        EVAL_COUNT=$(tail -n +2 "data/new_evaluations_from_forms.csv" | cut -d',' -f2 | sort -u | wc -l | tr -d ' ')
        ROW_COUNT=$(tail -n +2 "data/new_evaluations_from_forms.csv" | wc -l | tr -d ' ')

        log "Found ${EVAL_COUNT} missing evaluations (${ROW_COUNT} total rows)"
        log "Saved to: ${OUTPUT_DIR}/new_evaluations_latest.csv"

        # Create a summary file
        cat > "${OUTPUT_DIR}/LATEST_SUMMARY.txt" << EOF
Missing Evaluations Extraction Summary
Generated: $(date '+%Y-%m-%d %H:%M:%S UTC')

Missing Evaluations Found: ${EVAL_COUNT}
Total Rating Rows: ${ROW_COUNT}

Files:
- Latest CSV: ${OUTPUT_DIR}/new_evaluations_latest.csv
- Timestamped: ${OUTPUT_DIR}/new_evaluations_${TIMESTAMP}.csv
- Full output: ${OUTPUT_DIR}/extraction_output.txt

Next Steps:
1. Review the CSV file: cat ${OUTPUT_DIR}/new_evaluations_latest.csv
2. Manually verify which evaluations are genuinely missing
3. Create verified CSV for import to Coda
4. Import via Coda UI: https://coda.io/d/_d0KBG3dSZCs/Evals-Ratings_su3Mx_O0

Note: This is automated extraction. Always manually verify before importing to Coda.
EOF

        log "Summary saved to: ${OUTPUT_DIR}/LATEST_SUMMARY.txt"
    else
        log "WARNING: Extraction script ran but did not generate CSV file"
    fi
else
    log "ERROR: Extraction script failed with exit code ${EXIT_CODE}"
    log "Check output: ${OUTPUT_DIR}/extraction_output.txt"
fi

# Keep only last 30 days of timestamped files
log "Cleaning up old extraction files (keeping last 30 days)..."
find "${OUTPUT_DIR}" -name "new_evaluations_*.csv" -type f -mtime +30 -delete 2>/dev/null || true

log "=========================================="
log "Extraction process complete"
log "=========================================="
