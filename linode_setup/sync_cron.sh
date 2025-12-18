#!/bin/bash

# Unjournal SQLite Sync - Cron Wrapper Script
# This script runs as a daily cron job to sync Coda data to SQLite

# Configuration
REPO_DIR="/opt/unjournal"
DB_PATH="/var/lib/unjournal/unjournal_data.db"
LOG_DIR="/var/log/unjournal"
LOG_FILE="$LOG_DIR/sync_cron.log"
ENV_FILE="/var/lib/unjournal/.env"
PUBPUB_EXPORT_DIR="/var/lib/unjournal/pubpub_exports"

# Ensure log directory exists
mkdir -p "$LOG_DIR"

# Function to log with timestamp
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

# ========================================
# START SYNC
# ========================================
log "========================================"
log "Starting Unjournal SQLite sync"
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

# Step 1: Create evaluator-paper dataset (with privacy protections)
log "Creating evaluator-paper dataset..."
if python3 "$REPO_DIR/code/create_evaluator_paper_dataset.py" >> "$LOG_FILE" 2>&1; then
    log "✓ Evaluator-paper dataset created successfully"
else
    log "⚠ Evaluator-paper dataset creation failed (continuing with export)"
fi

# Step 2: Run SQLite export (includes evaluator-paper data if available)
log "Running SQLite export..."
if python3 "$REPO_DIR/code/export_to_sqlite.py" --db-path "$DB_PATH" >> "$LOG_FILE" 2>&1; then
    log "✓ Export completed successfully"
    EXIT_CODE=0
else
    log "ERROR: Export failed with exit code $?"
    EXIT_CODE=1
fi

# Step 3: Harvest PubPub Markdown/PDF exports
log "Harvesting PubPub exports..."
mkdir -p "$PUBPUB_EXPORT_DIR"
if python3 "$REPO_DIR/code/harvest_pubpub_assets.py" --output-dir "$PUBPUB_EXPORT_DIR" >> "$LOG_FILE" 2>&1; then
    log "✓ PubPub exports harvested successfully"
else
    log "⚠ PubPub export harvest failed (continuing)"
fi

# Show database info
if [ -f "$DB_PATH" ]; then
    DB_SIZE=$(du -h "$DB_PATH" | cut -f1)
    log "Database size: $DB_SIZE"
else
    log "WARNING: Database file not found: $DB_PATH"
fi

# Cleanup: Keep only last 30 days of logs
find "$LOG_DIR" -name "*.log" -mtime +30 -delete

log "========================================"
log "Sync completed with exit code: $EXIT_CODE"
log "========================================"

exit $EXIT_CODE
