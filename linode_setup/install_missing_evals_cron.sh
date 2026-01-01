#!/bin/bash
#
# Installation script for missing evaluations extraction cron job
# Run this on your Linode server as root
#
# Usage:
#   sudo bash install_missing_evals_cron.sh
#

set -e

echo "=========================================="
echo "Installing Missing Evaluations Cron Job"
echo "=========================================="

# Check if running as root
if [ "$EUID" -ne 0 ]; then
    echo "ERROR: Please run as root (use sudo)"
    exit 1
fi

# Configuration
UNJOURNAL_DIR="/var/lib/unjournal"
REPO_DIR="${UNJOURNAL_DIR}/unjournaldata"
OUTPUT_DIR="${UNJOURNAL_DIR}/missing_evaluations"
LOG_DIR="/var/log/unjournal"

# 1. Create necessary directories
echo ""
echo "[1/6] Creating directories..."
mkdir -p "${OUTPUT_DIR}"
mkdir -p "${LOG_DIR}"
echo "✓ Created ${OUTPUT_DIR}"
echo "✓ Created ${LOG_DIR}"

# 2. Copy the cron script
echo ""
echo "[2/6] Installing cron script..."
if [ ! -f "linode_setup/extract_missing_evals_cron.sh" ]; then
    echo "ERROR: Run this script from the repository root directory"
    exit 1
fi

cp linode_setup/extract_missing_evals_cron.sh "${UNJOURNAL_DIR}/extract_missing_evals_cron.sh"
chmod +x "${UNJOURNAL_DIR}/extract_missing_evals_cron.sh"
echo "✓ Installed ${UNJOURNAL_DIR}/extract_missing_evals_cron.sh"

# 3. Verify .env file exists with CODA_API_KEY
echo ""
echo "[3/6] Checking environment file..."
if [ ! -f "${UNJOURNAL_DIR}/.env" ]; then
    echo "WARNING: ${UNJOURNAL_DIR}/.env not found"
    echo "Creating template .env file..."
    cat > "${UNJOURNAL_DIR}/.env" << 'EOF'
# Coda API Key
# Get your API key from: https://coda.io/account
CODA_API_KEY=your_coda_api_key_here
EOF
    chmod 600 "${UNJOURNAL_DIR}/.env"
    echo "✓ Created ${UNJOURNAL_DIR}/.env (YOU MUST EDIT THIS FILE WITH YOUR API KEY)"
else
    # Check if CODA_API_KEY is set
    if grep -q "^CODA_API_KEY=.\+$" "${UNJOURNAL_DIR}/.env"; then
        echo "✓ CODA_API_KEY found in ${UNJOURNAL_DIR}/.env"
    else
        echo "WARNING: CODA_API_KEY not set in ${UNJOURNAL_DIR}/.env"
        echo "Please add: CODA_API_KEY=your_api_key"
    fi
fi

# 4. Install Python dependencies
echo ""
echo "[4/6] Installing Python dependencies..."
cd "${REPO_DIR}"

# Check if requirements.txt exists
if [ -f "requirements.txt" ]; then
    pip3 install -r requirements.txt > /dev/null 2>&1 || {
        echo "WARNING: Some pip packages may have failed to install"
    }
    echo "✓ Installed Python dependencies"
else
    echo "WARNING: requirements.txt not found, installing key packages manually..."
    pip3 install codaio python-dotenv pandas > /dev/null 2>&1
    echo "✓ Installed codaio, python-dotenv, pandas"
fi

# 5. Set up cron job
echo ""
echo "[5/6] Setting up cron job..."

# Check if cron job already exists
if crontab -l 2>/dev/null | grep -q "extract_missing_evals_cron.sh"; then
    echo "Cron job already exists, skipping..."
else
    # Add cron job: Daily at 2:30 AM UTC (30 minutes after SQLite export)
    (crontab -l 2>/dev/null; echo "# Extract missing evaluations from Coda forms (daily at 2:30 AM UTC)") | crontab -
    (crontab -l 2>/dev/null; echo "30 2 * * * ${UNJOURNAL_DIR}/extract_missing_evals_cron.sh") | crontab -
    echo "✓ Added cron job (runs daily at 2:30 AM UTC)"
fi

# 6. Test the script
echo ""
echo "[6/6] Testing the script..."
echo "Running a test extraction (this may take 30-60 seconds)..."

"${UNJOURNAL_DIR}/extract_missing_evals_cron.sh"

if [ -f "${OUTPUT_DIR}/LATEST_SUMMARY.txt" ]; then
    echo ""
    echo "✓ Test successful!"
    echo ""
    echo "=========================================="
    cat "${OUTPUT_DIR}/LATEST_SUMMARY.txt"
    echo "=========================================="
else
    echo "WARNING: Test may have failed, check logs:"
    echo "  tail -50 /var/log/unjournal/extract_missing_evals.log"
fi

# Print final instructions
echo ""
echo "=========================================="
echo "Installation Complete!"
echo "=========================================="
echo ""
echo "Configuration:"
echo "  Script:       ${UNJOURNAL_DIR}/extract_missing_evals_cron.sh"
echo "  Output:       ${OUTPUT_DIR}/"
echo "  Logs:         ${LOG_DIR}/extract_missing_evals.log"
echo "  Schedule:     Daily at 2:30 AM UTC"
echo ""
echo "View Results:"
echo "  Latest CSV:   cat ${OUTPUT_DIR}/new_evaluations_latest.csv"
echo "  Summary:      cat ${OUTPUT_DIR}/LATEST_SUMMARY.txt"
echo "  Logs:         tail -f ${LOG_DIR}/extract_missing_evals.log"
echo ""
echo "Cron Jobs:"
echo "  List:         crontab -l"
echo "  Edit:         crontab -e"
echo ""
echo "Manual Run:"
echo "  sudo ${UNJOURNAL_DIR}/extract_missing_evals_cron.sh"
echo ""
echo "IMPORTANT:"
echo "  1. Verify ${UNJOURNAL_DIR}/.env has your CODA_API_KEY"
echo "  2. Review extractions before importing to Coda"
echo "  3. Files are stored ONLY on this server (not in public GitHub)"
echo ""
