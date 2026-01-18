#!/bin/bash

# Unjournal Bibliometrics Update - Cron Wrapper Script
# This script runs weekly (Sundays at 3:00 AM UTC) to update bibliometric data
# from OpenAlex for all papers with DOIs.

# Configuration
REPO_DIR="/opt/unjournal"
LOG_DIR="/var/log/unjournal"
LOG_FILE="$LOG_DIR/bibliometrics.log"
ENV_FILE="/var/lib/unjournal/.env"

# Ensure log directory exists
mkdir -p "$LOG_DIR"

# Function to log with timestamp
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

# ========================================
# START BIBLIOMETRICS UPDATE
# ========================================
log "========================================"
log "Starting Unjournal bibliometrics update"
log "========================================"

# Change to repository directory
cd "$REPO_DIR" || {
    log "ERROR: Could not cd to $REPO_DIR"
    exit 1
}

# Pull latest code from GitHub
log "Pulling latest code from GitHub..."
if git pull origin main >> "$LOG_FILE" 2>&1; then
    log "✓ Code updated successfully"
else
    log "⚠ Git pull failed (continuing with existing code)"
fi

# Export environment variables
if [ -f "$ENV_FILE" ]; then
    export $(cat "$ENV_FILE" | grep -v '^#' | xargs)
    log "✓ Environment variables loaded"
else
    log "ERROR: Environment file not found: $ENV_FILE"
    exit 1
fi

# Check for CODA_API_KEY
if [ -z "$CODA_API_KEY" ]; then
    log "ERROR: CODA_API_KEY not set in $ENV_FILE"
    exit 1
fi

# Ensure pyalex is installed
log "Checking Python dependencies..."
if ! python3 -c "import pyalex" 2>/dev/null; then
    log "Installing pyalex..."
    pip3 install pyalex >> "$LOG_FILE" 2>&1
fi

# Run bibliometrics update
log "Running bibliometrics update..."
if python3 "$REPO_DIR/code/update_bibliometrics.py" >> "$LOG_FILE" 2>&1; then
    log "✓ Bibliometrics update completed successfully"
    EXIT_CODE=0
else
    log "ERROR: Bibliometrics update failed with exit code $?"
    EXIT_CODE=1
fi

# Show CSV info
BIBLIOMETRICS_CSV="$REPO_DIR/data/bibliometrics.csv"
if [ -f "$BIBLIOMETRICS_CSV" ]; then
    ROW_COUNT=$(wc -l < "$BIBLIOMETRICS_CSV")
    log "Bibliometrics CSV rows: $((ROW_COUNT - 1))"  # Subtract header
else
    log "WARNING: Bibliometrics CSV not found: $BIBLIOMETRICS_CSV"
fi

# Cleanup: Keep only last 30 days of logs
find "$LOG_DIR" -name "*.log" -mtime +30 -delete

log "========================================"
log "Bibliometrics update completed with exit code: $EXIT_CODE"
log "========================================"

exit $EXIT_CODE
