# Linode Setup FAQ - SQLite Database & Evaluator Dataset

## Question 1: Do we need a separate evaluator-paper dataset, or can it be embedded in SQLite?

### Answer: Keep it SEPARATE (recommended)

**Current architecture:**
```
Step 1: create_evaluator_paper_dataset.py
    ↓
    Creates: data/evaluator_paper_level.csv (privacy-protected)
    ↓
Step 2: export_to_sqlite.py
    ↓
    Reads the CSV + Coda directly
    ↓
    Creates: SQLite database with all tables
```

**Why keep separate:**

✅ **The CSV serves multiple purposes:**
- Committed to GitHub for public access
- Used by Shiny dashboard
- Used by R/Python analysis scripts
- Imported into SQLite database

✅ **Different use cases:**
- **CSV**: Public, portable, version-controlled, used by GitHub Pages
- **SQLite**: Optional, for SQL queries, Linode server only

✅ **Privacy controls happen in CSV creation:**
- `create_evaluator_paper_dataset.py` applies privacy protections
- SQLite import just reads the already-protected CSV
- Separation of concerns

✅ **Already working in GitHub Actions:**
- GitHub Actions creates the CSV daily
- CSV is auto-committed to repository
- Dashboard uses the committed CSV

### Could you merge them?

**Technically yes**, but you'd lose:
- Public CSV file on GitHub
- Dashboard integration (it reads the CSV)
- Version control of the dataset
- Portability (CSV is universal format)

**Recommendation: Keep separate** ✅

---

## Question 2: When will updates happen, and from which tables?

### Update Schedule

| System | Schedule | What Updates |
|--------|----------|--------------|
| **GitHub Actions** | • Daily at 13:30 UTC<br>• On push to main branch | • CSV files in `/data`<br>• `evaluator_paper_level.csv`<br>• Shiny dashboard deployment |
| **Linode Server** (if configured) | • Daily at 2:00 AM UTC | • SQLite database<br>• Includes evaluator_paper_level table |

### Data Source: Coda.io Tables

Both systems pull from these Coda tables:

**Direct Coda exports:**
1. **Research papers** (`grid-Iru9Fra3tE`)
   - → `research.csv` and `research` table in SQLite

2. **Evaluator ratings** (`grid-pcJr9ZM3wT`)
   - → `rsx_evalr_rating.csv` and `evaluator_ratings` table in SQLite

3. **Paper authors** (`grid-bJ5HubGR8H`)
   - → `paper_authors.csv` and `paper_authors` table in SQLite

4. **Survey responses - Academic** (`grid-aDSyEIerdL`)
   - → Combined into `survey_responses` table in SQLite

5. **Survey responses - Applied** (`grid-znNSTj_xX3`)
   - → Combined into `survey_responses` table in SQLite

**Combined/processed dataset:**
6. **Evaluator-paper level**
   - Source: Combines surveys + ratings from Coda (with privacy protections)
   - → `evaluator_paper_level.csv` → `evaluator_paper_level` table in SQLite

### Data Flow Diagram

```
Coda.io (source of truth)
    │
    ├─→ GitHub Actions (13:30 UTC daily)
    │   ├─→ import-unjournal-data.py
    │   │   └─→ research.csv, rsx_evalr_rating.csv, paper_authors.csv
    │   │
    │   ├─→ create_evaluator_paper_dataset.py
    │   │   └─→ evaluator_paper_level.csv (privacy-protected)
    │   │
    │   └─→ Deploy to shinyapps.io
    │
    └─→ Linode Server (2:00 AM UTC daily, if configured)
        ├─→ Pull latest code from GitHub
        ├─→ create_evaluator_paper_dataset.py (creates fresh CSV)
        └─→ export_to_sqlite.py
            └─→ /var/lib/unjournal/unjournal_data.db
                (reads evaluator_paper_level.csv + direct Coda export)
```

---

## Question 3: Where is the SQLite database now?

### Current Status: Database does NOT exist yet

**The database needs to be created on Linode** - it's not in the GitHub repository and shouldn't be (it would be large and change daily).

**When configured, it will be at:**
```
/var/lib/unjournal/unjournal_data.db
```

**To check if already set up:**
```bash
ssh your-user@your-linode-server
ls -lh /var/lib/unjournal/unjournal_data.db
```

**Current state:**
- ✅ **Scripts exist**: `code/export_to_sqlite.py`, `linode_setup/sync_cron.sh`
- ✅ **Documentation exists**: LINODE_CRON_SETUP.md
- ❌ **Database exists**: Needs one-time setup (see Question 4 below)

---

## Question 4: What do I need to do on Linode to make this work?

### Setup Steps (One-time, ~25 minutes)

#### Step 1: Check Current Status (5 minutes)

```bash
# SSH to Linode server
ssh user@your-linode-server

# Check if directory exists
ls -la /opt/unjournal

# Check if data directory exists
ls -la /var/lib/unjournal

# Check if .env file exists (DO NOT cat it - contains secrets)
ls -la /var/lib/unjournal/.env

# Check if cron job is scheduled
sudo crontab -l | grep unjournal
```

#### Step 2: Run Automated Installation (10 minutes)

**Option A: Automated installation (Recommended)**

```bash
# Download the installation script
cd /tmp
wget https://raw.githubusercontent.com/unjournal/unjournaldata/main/linode_setup/install_sqlite_sync.sh

# Run it
sudo bash install_sqlite_sync.sh
```

This script will:
- Install SQLite3 and Python dependencies (pandas, codaio, python-dotenv)
- Create directory structure:
  - `/opt/unjournal` (code repository)
  - `/var/lib/unjournal` (database storage)
  - `/var/lib/unjournal/backups` (automated backups)
  - `/var/log/unjournal` (logs)
- Clone repository to `/opt/unjournal`
- Create environment file template at `/var/lib/unjournal/.env`
- Create backup script

#### Step 3: Add Your Coda API Key (2 minutes)

```bash
# Edit the environment file
sudo nano /var/lib/unjournal/.env

# Replace the placeholder with your actual key:
CODA_API_KEY=your-actual-api-key-here

# Save: Ctrl+X, then Y, then Enter

# Verify permissions are secure (should be 600)
ls -l /var/lib/unjournal/.env
# Should show: -rw------- (owner read/write only)

# If not 600, fix it:
sudo chmod 600 /var/lib/unjournal/.env
```

**Getting Your Coda API Key:**
1. Go to https://coda.io/account
2. Click "Generate API token"
3. Copy the token (looks like: `abc123def456...`)
4. **IMPORTANT**: Store it securely - you won't be able to see it again!

#### Step 4: Set Up Cron Job (2 minutes)

```bash
# Edit root's crontab
sudo crontab -e

# Add this line (runs daily at 2:00 AM UTC):
0 2 * * * /opt/unjournal/linode_setup/sync_cron.sh

# Save and exit (in vi: press Esc, type :wq, press Enter)

# Verify it was added:
sudo crontab -l
```

#### Step 5: Test Manually (5 minutes)

```bash
# Run the sync script manually
cd /opt/unjournal
sudo /opt/unjournal/linode_setup/sync_cron.sh

# Check the log for errors
sudo tail -50 /var/log/unjournal/sync_cron.log

# If successful, verify database was created
ls -lh /var/lib/unjournal/unjournal_data.db

# Check database size
du -h /var/lib/unjournal/unjournal_data.db

# Quick database test
sqlite3 /var/lib/unjournal/unjournal_data.db "SELECT COUNT(*) FROM research;"
```

#### Step 6: Set Up Weekly Backups (Optional, 2 minutes)

```bash
# Edit root's crontab again
sudo crontab -e

# Add this line (runs Sundays at 3:00 AM UTC):
0 3 * * 0 /var/lib/unjournal/backup_database.sh

# Save and exit
```

### Alternative: Manual Installation

If you prefer manual installation or the automated script fails, follow the complete step-by-step instructions in [LINODE_CRON_SETUP.md](../LINODE_CRON_SETUP.md).

---

## Question 5: Security Risk of Secrets on Linode?

### Short Answer: **Low risk IF configured correctly** ✅

### Security Assessment

**Good security practices (if followed):**

✅ **File permissions = 600 (owner-only read/write)**
```bash
-rw------- 1 root root  50 Nov 16 12:00 .env
```
Only root or the file owner can read this file.

✅ **Directory permissions = 750 (owner full, group read/execute)**
```bash
drwxr-x--- 2 root root 4096 Nov 16 12:00 /var/lib/unjournal
```

✅ **SSH key authentication (not passwords)**
- Only team members with SSH keys can access
- Better than committing secrets to GitHub

✅ **Standard practice for production servers**
- This is how secrets are managed on most servers
- Better than: environment variables, config repos, etc.

### Potential Risks & Mitigations

| Risk | Mitigation |
|------|------------|
| **Unauthorized SSH access** | • Use SSH keys only (disable password auth)<br>• Keep SSH keys secure<br>• Use `fail2ban` to block brute force |
| **Local privilege escalation** | • Keep server patched<br>• Minimal user accounts<br>• Strong passwords for sudo |
| **Backup exposure** | • Encrypt backups<br>• Secure backup destinations |
| **Log exposure** | • Logs don't contain API keys<br>• Log directory permissions: 750 |

### Security Checklist

Before deploying:

```bash
# 1. Check file permissions
ls -l /var/lib/unjournal/.env
# Should show: -rw------- (600)

# 2. Verify SSH key-only access
sudo grep "PasswordAuthentication" /etc/ssh/sshd_config
# Should show: PasswordAuthentication no

# 3. Check who has sudo access
sudo grep "^sudo:" /etc/group
# Should list only trusted team members

# 4. Verify firewall is enabled
sudo ufw status
# Should show: Status: active

# 5. Check fail2ban is running (optional but recommended)
sudo systemctl status fail2ban
```

### Comparison: Linode vs GitHub Secrets

| Aspect | Linode `.env` file | GitHub Secrets |
|--------|-------------------|----------------|
| **Visibility** | Only SSH users | GitHub admins + Actions |
| **Access Control** | File permissions (600) | GitHub permissions |
| **Audit Log** | SSH logs | GitHub audit log |
| **Encryption** | Filesystem encryption | Encrypted at rest |
| **Best Use** | Server operations | CI/CD pipelines |

**Bottom Line:** Linode `.env` file is SECURE if:
- Only trusted team has SSH access ✅
- File permissions are 600 ✅
- Server is properly maintained ✅

This is standard practice and **safer than committing to GitHub**.

---

## Question 6: Do I need to do anything NOW?

### Decision Tree

```
Do you want SQL query access to Unjournal data?
│
├─ NO → You're done! ✅
│        GitHub Actions already handles everything.
│        CSV files update daily automatically.
│        Dashboard deploys automatically.
│
└─ YES → Set up Linode (one-time setup)
         Follow steps in Question 4 above.
         Takes ~25 minutes.
         Then runs automatically daily.
```

### What's Already Working (No Action Needed)

✅ **GitHub Actions** (already configured):
- Runs daily at 13:30 UTC
- Creates CSV files from Coda
- Creates `evaluator_paper_level.csv` with privacy protections
- Deploys Shiny dashboard
- All automated ✅

### What Needs Setup (Only if you want SQLite database)

🔧 **Linode Server** (optional - for SQL queries):
- One-time setup required (~25 minutes)
- Add `CODA_API_KEY` to `/var/lib/unjournal/.env`
- Set up cron job
- Then runs automatically daily at 2:00 AM UTC

---

## Troubleshooting

### Problem: Script fails with "CODA_API_KEY not set"

**Solution:**
```bash
# Check if .env file exists
ls -la /var/lib/unjournal/.env

# Check if it has content (but don't display the key!)
sudo wc -l /var/lib/unjournal/.env
# Should show: 1 or more lines

# Check if symlink exists
ls -la /opt/unjournal/.Renviron
# Should point to: /var/lib/unjournal/.env

# Recreate symlink if needed
sudo ln -sf /var/lib/unjournal/.env /opt/unjournal/.Renviron
```

### Problem: Permission denied errors

**Solution:**
```bash
# Fix ownership
sudo chown -R root:root /opt/unjournal
sudo chown -R root:root /var/lib/unjournal
sudo chown -R root:root /var/log/unjournal

# Fix permissions
sudo chmod 600 /var/lib/unjournal/.env
sudo chmod 750 /var/lib/unjournal
sudo chmod 750 /var/log/unjournal
```

### Problem: Database has "status_x" column error

**This is expected** - the evaluator_paper_level table has a known issue with duplicate status columns from the CSV merge. The core tables (research, evaluator_ratings, paper_authors, survey_responses) will export successfully. This is documented as a non-critical issue.

### Problem: Cron job doesn't run

**Solution:**
```bash
# Check if cron daemon is running
sudo systemctl status cron

# Check crontab entry
sudo crontab -l

# Check system cron logs
sudo grep CRON /var/log/syslog | tail -20

# Test script manually
sudo /opt/unjournal/linode_setup/sync_cron.sh
sudo tail -100 /var/log/unjournal/sync_cron.log
```

---

## Summary

| Question | Answer |
|----------|--------|
| Keep datasets separate? | **YES** - CSV serves multiple purposes |
| When do updates happen? | GitHub: 13:30 UTC daily<br>Linode: 2:00 AM UTC (if configured) |
| What tables update? | All tables from Coda (research, ratings, surveys, etc.) |
| Where is database now? | **Doesn't exist yet** - needs one-time Linode setup |
| Need to do anything now? | **Only if you want SQLite database** (~25 min setup)<br>Otherwise, GitHub Actions handles everything |
| Security risk? | **Low risk** with proper file permissions (600) |
| Who has access? | Only people with SSH keys to Linode server |

---

## Support

- **Installation Issues**: See [LINODE_CRON_SETUP.md](../LINODE_CRON_SETUP.md)
- **Query Examples**: See [SQLITE_QUERIES.md](SQLITE_QUERIES.md)
- **GitHub Issues**: https://github.com/unjournal/unjournaldata/issues
