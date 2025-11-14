# Linode Server Cron Job Setup

This guide explains how to set up automated daily data imports and dataset generation on a Linode server.

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
