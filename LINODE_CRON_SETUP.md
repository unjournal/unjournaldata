# Linode Server Automation Setup

This guide explains how to set up automated daily processes on a Linode server:
1. **CSV Export** - Export Coda data to CSV files (for GitHub)
2. **SQLite Database** - Export Coda data to local SQLite database
3. **Dataset Generation** - Create evaluator-paper level dataset
4. **Missing Evaluations** - Extract missing evaluations from Coda forms (PRIVATE - not committed to GitHub)

Choose the setup that fits your needs.

## Prerequisites

1. **Linode server** with:
   - Python 3.9+
   - Git configured
   - SSH key for GitHub access

2. **Repository cloned** on server:
   ```bash
   cd /path/to/projects
   git clone git@github.com:unjournal/unjournaldata.git
   cd unjournaldata
   ```

3. **Python dependencies installed**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Coda API key** stored in `.Renviron`:
   ```bash
   # Create .Renviron file (if it doesn't exist)
   echo "CODA_API_KEY=your-api-key-here" > .Renviron
   chmod 600 .Renviron  # Restrict permissions
   ```

## Setup Steps

### 1. Create Update Script

Create a bash script that runs all data import and generation tasks:

```bash
cat > /path/to/projects/unjournaldata/update_data.sh << 'EOF'
#!/bin/bash

# Update Unjournal Data - Automated Script
# Runs data import from Coda and generates evaluator-paper dataset

cd /path/to/projects/unjournaldata || exit 1

# Log file with timestamp
LOG_FILE="logs/cron_update_$(date +%Y%m%d).log"
mkdir -p logs

echo "================================" >> "$LOG_FILE"
echo "Update started: $(date)" >> "$LOG_FILE"
echo "================================" >> "$LOG_FILE"

# Pull latest code from GitHub
echo "Pulling latest code..." >> "$LOG_FILE"
git pull origin main >> "$LOG_FILE" 2>&1

# Run data import
echo "Importing data from Coda..." >> "$LOG_FILE"
python3 code/import-unjournal-data.py >> "$LOG_FILE" 2>&1
IMPORT_STATUS=$?

if [ $IMPORT_STATUS -ne 0 ]; then
    echo "ERROR: Data import failed with status $IMPORT_STATUS" >> "$LOG_FILE"
    exit 1
fi

# Run evaluator-paper dataset creation
echo "Creating evaluator-paper dataset..." >> "$LOG_FILE"
python3 code/create_evaluator_paper_dataset.py >> "$LOG_FILE" 2>&1
DATASET_STATUS=$?

if [ $DATASET_STATUS -ne 0 ]; then
    echo "ERROR: Dataset creation failed with status $DATASET_STATUS" >> "$LOG_FILE"
    exit 1
fi

# Commit and push updated data
echo "Committing updated data..." >> "$LOG_FILE"
git config user.email "cron@linode"
git config user.name "Linode Cron"
git add data/*.csv >> "$LOG_FILE" 2>&1
git diff-index --quiet HEAD data/*.csv || {
    git commit -m "Automated data update: $(date +%Y-%m-%d)" >> "$LOG_FILE" 2>&1
    git push origin main >> "$LOG_FILE" 2>&1
    echo "Data pushed to GitHub" >> "$LOG_FILE"
}

echo "================================" >> "$LOG_FILE"
echo "Update completed: $(date)" >> "$LOG_FILE"
echo "================================" >> "$LOG_FILE"

# Keep only last 30 days of logs
find logs -name "cron_update_*.log" -mtime +30 -delete

EOF
```

**Important:** Replace `/path/to/projects/unjournaldata` with your actual path!

### 2. Make Script Executable

```bash
chmod +x /path/to/projects/unjournaldata/update_data.sh
```

### 3. Test the Script

Run the script manually to verify it works:

```bash
/path/to/projects/unjournaldata/update_data.sh
```

Check the log file:
```bash
cat /path/to/projects/unjournaldata/logs/cron_update_$(date +%Y%m%d).log
```

### 4. Set Up Cron Job

Open crontab editor:
```bash
crontab -e
```

Add the following line to run daily at 2:00 PM UTC (adjust time as needed):

```cron
# Update Unjournal data daily at 2:00 PM UTC
0 14 * * * /path/to/projects/unjournaldata/update_data.sh
```

**Other schedule options:**
```cron
# Every 6 hours
0 */6 * * * /path/to/projects/unjournaldata/update_data.sh

# Every day at midnight
0 0 * * * /path/to/projects/unjournaldata/update_data.sh

# Every Monday at 8 AM
0 8 * * 1 /path/to/projects/unjournaldata/update_data.sh
```

Save and exit the editor (`:wq` in vim, `Ctrl+X` then `Y` in nano).

### 5. Verify Cron Job is Scheduled

```bash
crontab -l
```

You should see your new cron job listed.

### 6. Monitor Execution

Cron jobs typically send output via email. To redirect output to a file instead:

```cron
0 14 * * * /path/to/projects/unjournaldata/update_data.sh >> /path/to/projects/unjournaldata/logs/cron_output.log 2>&1
```

## Monitoring & Troubleshooting

### Check Recent Logs

```bash
# View today's log
tail -f /path/to/projects/unjournaldata/logs/cron_update_$(date +%Y%m%d).log

# View all recent logs
ls -ltr /path/to/projects/unjournaldata/logs/

# Check for errors
grep -i error /path/to/projects/unjournaldata/logs/cron_update_*.log
```

### Check Cron Status

```bash
# System cron logs (Ubuntu/Debian)
grep CRON /var/log/syslog

# Check if cron daemon is running
systemctl status cron
```

### Common Issues

**1. Cron job doesn't run:**
- Check cron is running: `systemctl status cron`
- Verify crontab entry: `crontab -l`
- Check system logs: `grep CRON /var/log/syslog`

**2. Script fails with "command not found":**
- Use full paths in script (e.g., `/usr/bin/python3`)
- Add PATH to script: `export PATH=/usr/local/bin:/usr/bin:/bin`

**3. Git operations fail:**
- Verify SSH key: `ssh -T git@github.com`
- Check git config: `git config --list`
- Ensure `.ssh/known_hosts` includes github.com

**4. API authentication fails:**
- Verify `.Renviron` exists: `ls -la /path/to/projects/unjournaldata/.Renviron`
- Check permissions: `stat -c "%a" .Renviron` (should be 600)
- Test manually: `python3 -c "import os; from dotenv import load_dotenv; load_dotenv('.Renviron'); print(os.getenv('CODA_API_KEY'))"`

### Disable/Enable Cron Job

**Temporarily disable:**
```bash
crontab -e
# Comment out the line with #:
# 0 14 * * * /path/to/projects/unjournaldata/update_data.sh
```

**Permanently remove:**
```bash
crontab -e
# Delete the line, save and exit
```

## Email Notifications

To receive email notifications on success/failure:

### Install mail utility (if not installed):
```bash
sudo apt-get install mailutils
```

### Modify script to send email:

Add to end of `update_data.sh`:

```bash
# Send email notification
if [ $DATASET_STATUS -eq 0 ]; then
    echo "Unjournal data update completed successfully" | mail -s "Cron Success: Unjournal Data" your-email@example.com
else
    echo "Unjournal data update FAILED. Check logs at $LOG_FILE" | mail -s "Cron FAILURE: Unjournal Data" your-email@example.com
fi
```

## Security Notes

1. **Never commit `.Renviron`** to git (it's in `.gitignore`)
2. **Restrict log file permissions** if they contain sensitive information:
   ```bash
   chmod 700 logs
   ```
3. **Rotate logs regularly** (script already includes 30-day cleanup)
4. **Use SSH keys** for GitHub authentication, not passwords

## Alternative: Systemd Timer

For more control, use systemd timers instead of cron:

### 1. Create service file:
```bash
sudo nano /etc/systemd/system/unjournal-update.service
```

```ini
[Unit]
Description=Update Unjournal Data
After=network.target

[Service]
Type=oneshot
User=your-username
WorkingDirectory=/path/to/projects/unjournaldata
ExecStart=/path/to/projects/unjournaldata/update_data.sh
```

### 2. Create timer file:
```bash
sudo nano /etc/systemd/system/unjournal-update.timer
```

```ini
[Unit]
Description=Run Unjournal Data Update Daily
Requires=unjournal-update.service

[Timer]
OnCalendar=daily
OnCalendar=14:00:00
Persistent=true

[Install]
WantedBy=timers.target
```

### 3. Enable and start:
```bash
sudo systemctl daemon-reload
sudo systemctl enable unjournal-update.timer
sudo systemctl start unjournal-update.timer
```

### 4. Check status:
```bash
systemctl status unjournal-update.timer
systemctl list-timers
```

## Support

For issues:
- GitHub: https://github.com/unjournal/unjournaldata/issues
- Check logs first: `/path/to/projects/unjournaldata/logs/`
- Test script manually before debugging cron

---

# Part 2: SQLite Database Setup

For local database access with SQL queries (recommended for analysis and offline access).

## Quick Start

Run the automated installation script:

```bash
# Download and run installation script
cd /tmp
wget https://raw.githubusercontent.com/unjournal/unjournaldata/main/linode_setup/install_sqlite_sync.sh
sudo bash install_sqlite_sync.sh
```

This will:
- Install SQLite3 and Python dependencies
- Create directory structure (`/var/lib/unjournal`, `/var/log/unjournal`)
- Clone repository to `/opt/unjournal`
- Set up environment file template
- Create backup script

## Manual Setup

If you prefer manual installation:

### 1. Install Dependencies

```bash
# Install SQLite3
sudo apt-get update
sudo apt-get install -y sqlite3 libsqlite3-dev

# Install Python packages
pip3 install codaio pandas python-dotenv
```

### 2. Create Directory Structure

```bash
sudo mkdir -p /opt/unjournal
sudo mkdir -p /var/lib/unjournal
sudo mkdir -p /var/lib/unjournal/backups
sudo mkdir -p /var/log/unjournal

# Set permissions
sudo chmod 750 /var/lib/unjournal
sudo chmod 750 /var/log/unjournal
```

### 3. Clone Repository

```bash
cd /opt/unjournal
git clone https://github.com/unjournal/unjournaldata.git .
```

### 4. Configure API Key

```bash
# Create environment file
sudo nano /var/lib/unjournal/.env

# Add this content:
CODA_API_KEY=your-api-key-here
```

```bash
# Secure the file
sudo chmod 600 /var/lib/unjournal/.env

# Link to repository
sudo ln -s /var/lib/unjournal/.env /opt/unjournal/.Renviron
```

## Testing the Export

Test the SQLite export manually before setting up cron:

```bash
cd /opt/unjournal

# Step 1: Create evaluator-paper dataset (optional but recommended)
sudo python3 code/create_evaluator_paper_dataset.py

# Step 2: Export to SQLite database
sudo python3 code/export_to_sqlite.py --db-path /var/lib/unjournal/unjournal_data.db
```

**Note:** The evaluator-paper dataset (`data/evaluator_paper_level.csv`) is created with privacy protections and then included in the SQLite export. The automated cron job runs both steps.

Expected output:
```
================================================================================
Starting Coda to SQLite export
================================================================================

1. Exporting research papers...
   Exporting 85 rows to research
   Successfully exported 85 rows to research

2. Exporting evaluator ratings...
   Exporting 859 rows to evaluator_ratings
   Successfully exported 859 rows to evaluator_ratings

[...]

================================================================================
EXPORT SUMMARY
================================================================================
Duration: 12.34 seconds
Database: /var/lib/unjournal/unjournal_data.db
Database size: 2.45 MB
Rows exported:
  research: 85
  evaluator_ratings: 859
  paper_authors: 123
  survey_responses: 113
  evaluator_paper_level: 149
  researchers_evaluators: 0
================================================================================
```

## Querying the Database

Once exported, you can query the SQLite database:

```bash
# Open database
sqlite3 /var/lib/unjournal/unjournal_data.db

# Show tables
.tables

# Show schema for a table
.schema research

# Run a query
SELECT label_paper_title, overall_mean_score 
FROM research 
WHERE overall_mean_score > 80
ORDER BY overall_mean_score DESC
LIMIT 10;

# Export query results to CSV
.mode csv
.output top_papers.csv
SELECT * FROM research WHERE overall_mean_score > 80;
.output stdout

# Exit
.quit
```

For more query examples, see: [docs/SQLITE_QUERIES.md](docs/SQLITE_QUERIES.md)

## Automated Daily Sync

### Using Cron

Set up daily export at 2:00 AM:

```bash
sudo crontab -e
```

Add this line:
```cron
# Daily SQLite export at 2:00 AM
0 2 * * * /opt/unjournal/linode_setup/sync_cron.sh
```

### Verify Cron Job

```bash
# List cron jobs
sudo crontab -l

# Check if cron daemon is running
sudo systemctl status cron

# View sync logs
tail -f /var/log/unjournal/sync_cron.log
```

## Automated Backups

Set up weekly database backups:

```bash
sudo crontab -e
```

Add:
```cron
# Weekly database backup (Sunday 3:00 AM)
0 3 * * 0 /var/lib/unjournal/backup_database.sh
```

Backups are stored in: `/var/lib/unjournal/backups/`

They are automatically:
- Compressed with gzip
- Deleted after 30 days

### Manual Backup

```bash
sudo /var/lib/unjournal/backup_database.sh
```

### Restore from Backup

```bash
# List backups
ls -lh /var/lib/unjournal/backups/

# Restore
gunzip -c /var/lib/unjournal/backups/unjournal_data_20250114_030000.db.gz > /var/lib/unjournal/unjournal_data.db
```

## Database Schema

The SQLite database contains these tables:

1. **research** - Papers/projects being evaluated
   - Primary key: `label_paper_title`
   - 85 rows, ~15 columns

2. **evaluator_ratings** - Quantitative ratings (long format)
   - Foreign key: `research` → `research(label_paper_title)`
   - 859 rows, 8 columns
   - Unique: `(research, evaluator, criteria)`

3. **paper_authors** - Author relationships
   - Foreign key: `research` → `research(label_paper_title)`
   - ~123 rows

4. **survey_responses** - Evaluator survey data
   - Combined academic + applied streams
   - ~113 rows

5. **evaluator_paper_level** - Combined wide-format dataset
   - Unique: `(paper_title, evaluator)`
   - 149 rows, 45 columns
   - Includes all rating criteria with confidence intervals

6. **researchers_evaluators** - Evaluator pool
   - (Requires team management doc access)

7. **export_metadata** - Export history and statistics

## Monitoring

### Check Export Status

```bash
# View recent exports
sqlite3 /var/lib/unjournal/unjournal_data.db "
SELECT 
  table_name,
  row_count,
  export_timestamp,
  status
FROM export_metadata
ORDER BY export_timestamp DESC
LIMIT 10;"
```

### Check Database Size

```bash
du -h /var/lib/unjournal/unjournal_data.db
```

### View Sync Logs

```bash
# Latest sync
tail -n 50 /var/log/unjournal/sync_cron.log

# All syncs today
grep "$(date +%Y-%m-%d)" /var/log/unjournal/sync_cron.log

# Failed syncs
grep "ERROR" /var/log/unjournal/sync_cron.log
```

## Troubleshooting

### Export Fails with "CODA_API_KEY not set"

```bash
# Check environment file
sudo cat /var/lib/unjournal/.env

# Ensure it contains:
CODA_API_KEY=your-actual-key-here

# Test loading environment
source /var/lib/unjournal/.env
echo $CODA_API_KEY
```

### Permission Denied Errors

```bash
# Fix ownership
sudo chown -R $USER:$USER /opt/unjournal
sudo chown -R $USER:$USER /var/lib/unjournal
sudo chown -R $USER:$USER /var/log/unjournal
```

### Database Locked Error

```bash
# Check for other processes using database
sudo lsof /var/lib/unjournal/unjournal_data.db

# If cron is running, wait for it to finish
# Or kill the process if needed
```

### Import Fails with Python Errors

```bash
# Reinstall Python packages
pip3 install --upgrade codaio pandas python-dotenv

# Check Python version (need 3.8+)
python3 --version
```

## Accessing from Other Machines

### Copy Database to Local Machine

```bash
# From local machine
scp user@linode-server:/var/lib/unjournal/unjournal_data.db ./

# Then query locally
sqlite3 ./unjournal_data.db
```

### Remote Access via SSH Tunnel

```bash
# On local machine
ssh -L 5000:localhost:5000 user@linode-server

# On Linode server (in another terminal)
cd /var/lib/unjournal
python3 -m http.server 5000

# Access from local browser
# http://localhost:5000/unjournal_data.db
```

## Integration with Analysis Tools

### Python

```python
import sqlite3
import pandas as pd

# Connect
conn = sqlite3.connect('/var/lib/unjournal/unjournal_data.db')

# Query
df = pd.read_sql_query("""
    SELECT 
        r.label_paper_title,
        r.overall_mean_score,
        COUNT(DISTINCT rt.evaluator) as num_evaluators
    FROM research r
    LEFT JOIN evaluator_ratings rt ON r.label_paper_title = rt.research
    GROUP BY r.label_paper_title
    ORDER BY r.overall_mean_score DESC
""", conn)

print(df.head())
conn.close()
```

### R

```r
library(DBI)
library(RSQLite)

# Connect
con <- dbConnect(RSQLite::SQLite(), "/var/lib/unjournal/unjournal_data.db")

# Query
df <- dbGetQuery(con, "
  SELECT * FROM research 
  WHERE overall_mean_score > 80
")

# List tables
dbListTables(con)

# Disconnect
dbDisconnect(con)
```

## Support

For issues:
- Check logs: `/var/log/unjournal/`
- GitHub Issues: https://github.com/unjournal/unjournaldata/issues
- Documentation: See `docs/SQLITE_QUERIES.md` for query examples

---

# Part 3: Missing Evaluations Extraction (PRIVATE)

**IMPORTANT:** This extracts potentially unpublished evaluation data from Coda forms. Data is stored **ONLY on your Linode server** and is NOT committed to the public GitHub repository.

## Overview

This automated process:
- Runs daily after the SQLite export (2:30 AM UTC)
- Extracts evaluations from Coda forms that don't exist in `rsx_evalr_rating` table
- Saves results to `/var/lib/unjournal/missing_evaluations/` (private, server-only)
- Generates a summary for manual review
- Keeps 30-day history

## Quick Install

Run the automated installation script on your Linode server:

```bash
# SSH to your Linode server
ssh root@your-linode-ip

# Navigate to repository
cd /var/lib/unjournal/unjournaldata

# Pull latest code (to get the installation script)
git pull origin main

# Run installation
sudo bash linode_setup/install_missing_evals_cron.sh
```

The script will:
1. Create `/var/lib/unjournal/missing_evaluations/` directory
2. Install the cron script
3. Verify environment variables (CODA_API_KEY)
4. Install Python dependencies (codaio, pandas, python-dotenv)
5. Set up cron job (daily at 2:30 AM UTC)
6. Run a test extraction

## Manual Installation

If you prefer manual setup:

### 1. Create Directories

```bash
sudo mkdir -p /var/lib/unjournal/missing_evaluations
sudo mkdir -p /var/log/unjournal
```

### 2. Copy Cron Script

```bash
cd /var/lib/unjournal/unjournaldata
sudo cp linode_setup/extract_missing_evals_cron.sh /var/lib/unjournal/
sudo chmod +x /var/lib/unjournal/extract_missing_evals_cron.sh
```

### 3. Verify Environment File

```bash
# Check if .env exists with CODA_API_KEY
sudo cat /var/lib/unjournal/.env

# If not, create it:
sudo nano /var/lib/unjournal/.env
```

Add:
```bash
CODA_API_KEY=your-coda-api-key-here
```

```bash
# Secure the file
sudo chmod 600 /var/lib/unjournal/.env
```

### 4. Install Python Dependencies

```bash
pip3 install codaio pandas python-dotenv
```

### 5. Set Up Cron Job

```bash
sudo crontab -e
```

Add:
```cron
# Extract missing evaluations from Coda forms (daily at 2:30 AM UTC)
30 2 * * * /var/lib/unjournal/extract_missing_evals_cron.sh
```

### 6. Test the Script

```bash
sudo /var/lib/unjournal/extract_missing_evals_cron.sh
```

## Viewing Results

After the cron job runs (or after manual test):

### View Summary

```bash
cat /var/lib/unjournal/missing_evaluations/LATEST_SUMMARY.txt
```

Example output:
```
Missing Evaluations Extraction Summary
Generated: 2025-12-30 02:30:15 UTC

Missing Evaluations Found: 13
Total Rating Rows: 115

Files:
- Latest CSV: /var/lib/unjournal/missing_evaluations/new_evaluations_latest.csv
- Timestamped: /var/lib/unjournal/missing_evaluations/new_evaluations_20251230_023015.csv
- Full output: /var/lib/unjournal/missing_evaluations/extraction_output.txt

Next Steps:
1. Review the CSV file
2. Manually verify which evaluations are genuinely missing
3. Create verified CSV for import to Coda
4. Import via Coda UI
```

### View Latest CSV

```bash
# Preview first 20 rows
head -20 /var/lib/unjournal/missing_evaluations/new_evaluations_latest.csv

# Count rows
wc -l /var/lib/unjournal/missing_evaluations/new_evaluations_latest.csv

# Count unique evaluations
tail -n +2 /var/lib/unjournal/missing_evaluations/new_evaluations_latest.csv | cut -d',' -f1,2 | sort -u | wc -l
```

### View Logs

```bash
# Latest run
tail -50 /var/log/unjournal/extract_missing_evals.log

# All runs today
grep "$(date +%Y-%m-%d)" /var/log/unjournal/extract_missing_evals.log

# Errors
grep "ERROR" /var/log/unjournal/extract_missing_evals.log
```

## Workflow for Importing to Coda

1. **Review the extraction**:
   ```bash
   cat /var/lib/unjournal/missing_evaluations/LATEST_SUMMARY.txt
   ```

2. **Download CSV to your local machine**:
   ```bash
   # From your local machine
   scp root@your-linode-ip:/var/lib/unjournal/missing_evaluations/new_evaluations_latest.csv ~/Downloads/
   ```

3. **Manually verify** which evaluations are genuinely missing:
   - Check against published evaluation packages
   - Exclude unpublished papers
   - Exclude independent evaluations
   - Check for name/title variations

4. **Create verified CSV** with only confirmed missing evaluations

5. **Import to Coda**:
   - Open https://coda.io/d/_d0KBG3dSZCs/Evals-Ratings_su3Mx_O0
   - Go to "rsx-evalr-rating" table
   - Click "..." → "Import data" → "From CSV"
   - Upload your verified CSV
   - Map columns correctly
   - Import as "Add new rows"

6. **Verify import**:
   - Check row counts in Coda
   - Spot-check a few evaluations

See `IMPORT_READY.md` for detailed import instructions.

## Files and Directories

```
/var/lib/unjournal/
├── .env                                    # API keys (private, 600 permissions)
├── unjournaldata/                          # Git repository
│   ├── code/
│   │   └── extract_new_evaluations_from_forms_v2.py
│   └── linode_setup/
│       ├── extract_missing_evals_cron.sh
│       └── install_missing_evals_cron.sh
├── missing_evaluations/                    # PRIVATE - extraction results
│   ├── LATEST_SUMMARY.txt                  # Summary of latest extraction
│   ├── new_evaluations_latest.csv          # Latest extraction (overwritten daily)
│   ├── new_evaluations_20251230_023015.csv # Timestamped archives (30-day retention)
│   └── extraction_output.txt               # Full script output
└── extract_missing_evals_cron.sh           # Cron script

/var/log/unjournal/
└── extract_missing_evals.log               # Cron execution logs
```

## Cron Schedule

- **Time**: 2:30 AM UTC daily
- **After**: SQLite export (which runs at 2:00 AM)
- **Duration**: ~30-60 seconds
- **Network**: Requires internet access to reach Coda API

## Manual Execution

Run the script manually anytime:

```bash
sudo /var/lib/unjournal/extract_missing_evals_cron.sh
```

This is useful for:
- Testing after code updates
- Immediate extraction without waiting for cron
- Debugging issues

## Troubleshooting

### Script Fails with "ModuleNotFoundError: codaio"

```bash
# Install missing Python packages
pip3 install codaio pandas python-dotenv

# Verify installation
python3 -c "import codaio; print('OK')"
```

### Script Fails with "CODA_API_KEY not set"

```bash
# Check environment file
sudo cat /var/lib/unjournal/.env

# Should contain:
CODA_API_KEY=your-actual-key

# Test loading
source /var/lib/unjournal/.env
echo $CODA_API_KEY
```

### No New Evaluations Found

This is normal! It means:
- All form responses are already in `rsx_evalr_rating`
- The extraction will still generate a summary with 0 missing evaluations

### Git Pull Fails

Not critical - the script will use existing code if git pull fails. Check:

```bash
cd /var/lib/unjournal/unjournaldata
git status
git pull origin main
```

### Cron Job Not Running

```bash
# Check if cron is running
sudo systemctl status cron

# Check cron logs
grep "extract_missing_evals" /var/log/syslog

# Verify cron job exists
sudo crontab -l | grep extract_missing_evals
```

## Security Notes

**CRITICAL SECURITY:**
1. **Data stays on server**: Extraction results are NEVER committed to public GitHub
2. **Private directory**: `/var/lib/unjournal/missing_evaluations/` is only accessible via SSH
3. **Environment security**: `.env` file has 600 permissions (readable only by owner)
4. **30-day retention**: Old extractions are auto-deleted after 30 days

**Why this matters:**
- Form responses may contain evaluations of unpublished papers
- Evaluator names might not be public yet
- Some papers may never be published
- Manual review is required before making data public

## Monitoring

### Check Last Run

```bash
# View summary
cat /var/lib/unjournal/missing_evaluations/LATEST_SUMMARY.txt

# Check timestamp
ls -lh /var/lib/unjournal/missing_evaluations/new_evaluations_latest.csv
```

### Check History

```bash
# List all timestamped extractions
ls -lht /var/lib/unjournal/missing_evaluations/new_evaluations_*.csv

# Count evaluations over time
for f in /var/lib/unjournal/missing_evaluations/new_evaluations_*.csv; do
    echo "$f: $(tail -n +2 "$f" | wc -l) rows"
done
```

### Email Notifications (Optional)

To receive email when new missing evaluations are found, edit the cron script:

```bash
sudo nano /var/lib/unjournal/extract_missing_evals_cron.sh
```

Add before the final log line:

```bash
# Send email if new evaluations found
if [ ${EVAL_COUNT} -gt 0 ]; then
    echo "Found ${EVAL_COUNT} missing evaluations. Check: ${OUTPUT_DIR}/LATEST_SUMMARY.txt" | \
        mail -s "Unjournal: ${EVAL_COUNT} Missing Evaluations Found" your-email@example.com
fi
```

## Disabling the Cron Job

Temporarily disable:

```bash
sudo crontab -e
# Comment out the line with #:
# 30 2 * * * /var/lib/unjournal/extract_missing_evals_cron.sh
```

Permanently remove:

```bash
sudo crontab -e
# Delete the line, save and exit
```

## Updating the Extraction Script

The extraction script is updated via git pull in the repository:

```bash
cd /var/lib/unjournal/unjournaldata
git pull origin main
```

The cron job automatically pulls latest code before each run, so updates are picked up automatically.

To force update immediately:

```bash
cd /var/lib/unjournal/unjournaldata
git pull origin main
sudo /var/lib/unjournal/extract_missing_evals_cron.sh  # Test with latest code
```

## Support

For issues:
- Check logs: `/var/log/unjournal/extract_missing_evals.log`
- Check output: `/var/lib/unjournal/missing_evaluations/extraction_output.txt`
- GitHub Issues: https://github.com/unjournal/unjournaldata/issues
- See `IMPORT_READY.md` for import instructions

---
