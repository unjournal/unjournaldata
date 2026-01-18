#!/bin/bash

# Installation script for Unjournal Bibliometrics Cron Job
# Run this script once on the Linode server to set up weekly bibliometrics updates

set -e

echo "========================================"
echo "Installing Unjournal Bibliometrics Cron Job"
echo "========================================"

# Configuration
REPO_DIR="/opt/unjournal"
CRON_SCRIPT="$REPO_DIR/linode_setup/update_bibliometrics_cron.sh"
CRON_SCHEDULE="0 3 * * 0"  # 3:00 AM UTC every Sunday

# Check if repository exists
if [ ! -d "$REPO_DIR" ]; then
    echo "ERROR: Repository not found at $REPO_DIR"
    echo "Please run install_sqlite_sync.sh first to set up the repository"
    exit 1
fi

# Check if cron script exists
if [ ! -f "$CRON_SCRIPT" ]; then
    echo "ERROR: Cron script not found at $CRON_SCRIPT"
    echo "Please pull latest code from GitHub first"
    exit 1
fi

# Make script executable
chmod +x "$CRON_SCRIPT"
echo "✓ Made cron script executable"

# Install pyalex dependency
echo "Installing Python dependencies..."
pip3 install pyalex
echo "✓ pyalex installed"

# Check if cron job already exists
EXISTING_CRON=$(crontab -l 2>/dev/null | grep -F "update_bibliometrics_cron.sh" || true)

if [ -n "$EXISTING_CRON" ]; then
    echo "⚠ Bibliometrics cron job already exists:"
    echo "  $EXISTING_CRON"
    echo ""
    read -p "Do you want to replace it? (y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Keeping existing cron job"
        exit 0
    fi
    # Remove existing entry
    crontab -l 2>/dev/null | grep -v -F "update_bibliometrics_cron.sh" | crontab -
    echo "✓ Removed existing cron job"
fi

# Add new cron job
(crontab -l 2>/dev/null || true; echo "$CRON_SCHEDULE $CRON_SCRIPT") | crontab -
echo "✓ Added cron job: $CRON_SCHEDULE"

# Verify installation
echo ""
echo "========================================"
echo "Installation Complete!"
echo "========================================"
echo ""
echo "Cron schedule: Every Sunday at 3:00 AM UTC"
echo "Script: $CRON_SCRIPT"
echo "Log file: /var/log/unjournal/bibliometrics.log"
echo ""
echo "Current cron jobs:"
crontab -l | grep -E "(unjournal|bibliometrics)"
echo ""
echo "To test manually:"
echo "  sudo $CRON_SCRIPT"
echo ""
echo "To view logs:"
echo "  tail -50 /var/log/unjournal/bibliometrics.log"
