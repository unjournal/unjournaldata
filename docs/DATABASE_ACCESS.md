# Unjournal Database - Web Access Guide

Quick reference for accessing the Unjournal database through your web browser.

---

## 🌐 Web Access (Datasette GUI)

**URL:** http://45.79.160.157:8001

**Login Credentials:**
- **Username:** `admin`
- **Password:** (contact database administrator)

**What you can do:**
- ✅ Browse all database tables
- ✅ Run custom SQL queries
- ✅ Export data to CSV/JSON
- ✅ Filter, sort, and search
- ✅ Share query URLs with others

---

## Available Tables

When you log in, you'll see these tables:

| Table | Description | Row Count |
|-------|-------------|-----------|
| **research** | Evaluated papers/projects | ~323 |
| **evaluator_ratings** | Quantitative ratings (long format) | ~859 |
| **paper_authors** | Author relationships | ~757 |
| **survey_responses** | Evaluator survey data (public fields) | ~113 |
| **evaluator_paper_level** | Wide-format evaluator-paper dataset | ~194 |
| **researchers_evaluators** | Evaluator pool (public info only) | ~279 |
| **export_metadata** | Export history and statistics | - |

---

## Quick Start Examples

### Browse a Table
1. Click on any table name (e.g., "research")
2. Use the filter boxes at the top of each column
3. Click column headers to sort
4. Click "CSV" or "JSON" to export

### Run a SQL Query
1. Click "SQL" in the top menu
2. Enter your query:
```sql
SELECT label_paper_title, overall_mean_score
FROM research
WHERE overall_mean_score IS NOT NULL
ORDER BY overall_mean_score DESC
LIMIT 10;
```
3. Click "Run SQL"
4. Export results with CSV/JSON buttons

### Find Papers by Evaluator
```sql
SELECT
  r.label_paper_title,
  COUNT(DISTINCT rt.evaluator) as num_evaluators,
  AVG(rt.middle_rating) as avg_rating
FROM research r
LEFT JOIN evaluator_ratings rt ON r.label_paper_title = rt.research
GROUP BY r.label_paper_title
HAVING num_evaluators > 0
ORDER BY num_evaluators DESC;
```

---

## More Query Examples

See [SQLITE_QUERIES.md](SQLITE_QUERIES.md) for a comprehensive collection of example SQL queries.

---

## Direct SSH Access (Advanced Users)

If you have SSH access to the Linode server:

```bash
# Connect to server
ssh root@45.79.160.157

# Access database directly
sqlite3 /var/lib/unjournal/unjournal_data.db

# Example query
sqlite> SELECT COUNT(*) FROM research;
```

---

## Data Updates

- **Automatic Updates:** Database is updated daily at 2:00 AM UTC via cron job
- **Data Source:** Coda.io (via `code/export_to_sqlite.py`)
- **Sync Logs:** Available on server at `/var/log/unjournal/sync_cron.log`

---

## Troubleshooting

### Can't log in?
- Try hard refresh: `Ctrl+Shift+R` (Windows/Linux) or `Cmd+Shift+R` (Mac)
- Clear browser cookies for the site
- Try in incognito/private browsing mode

### CSRF token error?
This happens when the browser caches an old login form. Do a hard refresh or clear cookies.

### Site not loading?
Check if the Datasette service is running (requires SSH access):
```bash
ssh root@45.79.160.157
sudo systemctl status datasette
```

### Forgot password?
Contact the database administrator or reset via SSH (see [DATASETTE_GUI_SETUP.md](DATASETTE_GUI_SETUP.md))

---

## Additional Documentation

- **Setup Guide:** [DATASETTE_GUI_SETUP.md](DATASETTE_GUI_SETUP.md)
- **SQL Examples:** [SQLITE_QUERIES.md](SQLITE_QUERIES.md)
- **Linode Setup:** [LINODE_SQLITE_INTERNAL_GUIDE.md](LINODE_SQLITE_INTERNAL_GUIDE.md)
- **General FAQ:** [LINODE_SETUP_FAQ.md](LINODE_SETUP_FAQ.md)

---

## Security & Privacy

- 🔒 **Password Protected** - Authentication required for all access
- 🔒 **Read-Only** - Cannot modify the database through the web interface
- 🔒 **Privacy Protected** - No confidential feedback, emails, or personal data in public tables
- 🔒 **Gitignored Data** - `evaluator_survey_responses.csv` is NOT in the public repository or database

---

## Support

**For access issues or questions:**
- GitHub Issues: https://github.com/unjournal/unjournaldata/issues
- Email: Contact Unjournal administrators

**For Datasette technical issues:**
- Datasette Docs: https://docs.datasette.io/
- Datasette GitHub: https://github.com/simonw/datasette
