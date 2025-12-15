# Datasette Web GUI Setup - Unjournal Database

Beautiful, read-only web interface for browsing the Unjournal SQLite database.

## Features

✅ **Read-only** - Safe for production (can't accidentally modify data)
✅ **Beautiful interface** - Modern, responsive design
✅ **SQL queries** - Run custom queries with syntax highlighting
✅ **Data exploration** - Filter, sort, export to CSV/JSON
✅ **Password protected** - Secure access control
✅ **Auto-updates** - Automatically serves the latest database

## Quick Install

### On Linode Server:

```bash
# Download and run installation script
cd /tmp
wget https://raw.githubusercontent.com/unjournal/unjournaldata/main/linode_setup/install_datasette.sh
sudo bash install_datasette.sh
```

### Set Password

```bash
# Generate password hash
datasette hash-password

# Enter your desired password when prompted
# Copy the hash that's generated
```

### Configure Authentication

```bash
# Edit metadata file
sudo nano /etc/datasette/metadata.json

# Replace REPLACE_WITH_HASH in the "plugins" section with the hash you just generated
# The key configuration is:
# "allow": {"unauthenticated": false}  <- This denies access to unauthenticated users
# "plugins": {
#   "datasette-auth-passwords": {
#     "admin_password_hash": "pbkdf2_sha256$..."  <- Your hash here
#   }
# }
```

### Start Service

```bash
# Start Datasette
sudo systemctl start datasette

# Enable auto-start on boot
sudo systemctl enable datasette

# Check status
sudo systemctl status datasette
```

### Configure Firewall

```bash
# Allow port 8001 through firewall
sudo ufw allow 8001/tcp
sudo ufw status
```

### Access the GUI

Open in your browser:
```
http://your-linode-ip:8001
```

Login with username `admin` and the password you set.

### Changing the Password

To change the admin password after initial setup:

```bash
# Generate new password hash
python3 -c "
from datasette_auth_passwords import hash_password
pw_hash = hash_password('YOUR_NEW_PASSWORD')
print(pw_hash)
"

# Copy the hash output, then edit metadata.json
sudo nano /etc/datasette/metadata.json

# Replace the admin_password_hash value with your new hash
# Should look like: "admin_password_hash": "pbkdf2_sha256$480000$..."

# Restart Datasette
sudo systemctl restart datasette
```

**Note**: After changing the password, you may need to hard refresh the login page (`Ctrl+Shift+R` or `Cmd+Shift+R`) to avoid CSRF token errors.

---

## Using Datasette

### Browse Tables

- **research** - 309 evaluated papers
- **evaluator_ratings** - 851 quantitative ratings
- **paper_authors** - 757 author entries
- **survey_responses** - 113 survey responses (public fields only)
- **evaluator_paper_level** - 194 evaluator-paper combinations
- **researchers_evaluators** - ~300 evaluators (public info only)

### Run SQL Queries

Click "SQL" in the menu to run custom queries:

```sql
-- Top 10 papers by score
SELECT label_paper_title, overall_mean_score
FROM research
WHERE overall_mean_score IS NOT NULL
ORDER BY overall_mean_score DESC
LIMIT 10;

-- Papers with most evaluators
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

### Export Data

- Click any table
- Filter/sort as desired
- Click "CSV" or "JSON" to download

### Share Queries

Datasette creates shareable URLs for queries:
```
http://your-ip:8001/unjournal_data?sql=YOUR_QUERY
```

---

## Management

### Check Logs

```bash
# View service logs
sudo journalctl -u datasette -f

# Check recent errors
sudo journalctl -u datasette --since "1 hour ago"
```

### Restart Service

```bash
sudo systemctl restart datasette
```

### Stop Service

```bash
sudo systemctl stop datasette
```

### Update Datasette

```bash
sudo pip3 install --upgrade --break-system-packages datasette datasette-auth-passwords
sudo systemctl restart datasette
```

---

## Security Best Practices

✅ **Password protection enabled** - Required by default
✅ **Read-only mode** - Cannot modify database
✅ **Firewall configured** - Only necessary ports open
✅ **Regular updates** - Keep Datasette updated

### Optional: Use HTTPS (Recommended)

For production, set up HTTPS with Nginx reverse proxy:

```bash
# Install Nginx
sudo apt install nginx

# Configure reverse proxy (see Nginx docs)
# Point to localhost:8001

# Get SSL certificate with Let's Encrypt
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx
```

### Optional: IP Whitelist

Restrict access to specific IPs:

```bash
# In /etc/datasette/settings.json, add:
{
  "allow": {
    "unauthenticated": false,
    "ip": ["1.2.3.4", "5.6.7.8"]
  }
}
```

---

## Troubleshooting

### Port already in use

```bash
# Check what's using port 8001
sudo lsof -i :8001

# Kill the process or change Datasette port
sudo nano /etc/systemd/system/datasette.service
# Change --port 8001 to --port 8002
sudo systemctl daemon-reload
sudo systemctl restart datasette
```

### Database file not found

```bash
# Check database exists
ls -l /var/lib/unjournal/unjournal_data.db

# Check permissions
sudo chmod 640 /var/lib/unjournal/unjournal_data.db
sudo chown root:datasette /var/lib/unjournal/unjournal_data.db
```

### Can't connect

```bash
# Check service is running
sudo systemctl status datasette

# Check firewall
sudo ufw status

# Check Datasette is listening
sudo netstat -tlnp | grep 8001
```

### Authentication not working

```bash
# Verify password hash in metadata.json
sudo cat /etc/datasette/metadata.json

# Regenerate hash (use Python script since datasette hash-password requires interactive input)
python3 -c "
from datasette_auth_passwords import hash_password
pw_hash = hash_password('YOUR_NEW_PASSWORD')
print(pw_hash)
"

# Update metadata.json with new hash
sudo nano /etc/datasette/metadata.json
# Replace the admin_password_hash value in the plugins section

# Restart service
sudo systemctl restart datasette
```

### CSRF token error on login

If you see "form-urlencoded POST field did not match cookie":

1. **Hard refresh** the login page: `Ctrl+Shift+R` (Windows/Linux) or `Cmd+Shift+R` (Mac)
2. **Or** clear browser cookies for the site
3. **Or** try in an incognito/private window

This happens when the browser caches an old login form after Datasette restarts.

---

## Advanced Configuration

### Custom Homepage

Edit `/etc/datasette/metadata.json`:

```json
{
  "title": "Unjournal Data",
  "description_html": "<h2>Welcome!</h2><p>Custom content here</p>"
}
```

### Add More Databases

```bash
# Edit service file
sudo nano /etc/systemd/system/datasette.service

# Add more database files
ExecStart=/usr/local/bin/datasette serve \
    /var/lib/unjournal/unjournal_data.db \
    /path/to/another.db \
    ...
```

### Plugins

```bash
# Install useful plugins
sudo pip3 install --break-system-packages \
    datasette-vega \
    datasette-cluster-map \
    datasette-json-html

# Restart service
sudo systemctl restart datasette
```

---

## Uninstall

```bash
# Stop and disable service
sudo systemctl stop datasette
sudo systemctl disable datasette

# Remove service file
sudo rm /etc/systemd/system/datasette.service

# Remove configuration
sudo rm -rf /etc/datasette

# Remove user
sudo userdel datasette

# Uninstall packages
sudo pip3 uninstall datasette datasette-auth-passwords

# Reload systemd
sudo systemctl daemon-reload
```

---

## Resources

- **Datasette Documentation**: https://docs.datasette.io/
- **Plugin Directory**: https://datasette.io/plugins
- **GitHub**: https://github.com/simonw/datasette
- **SQL Tutorial**: https://www.sqlitetutorial.net/

---

## Support

For issues with the Unjournal database:
- GitHub: https://github.com/unjournal/unjournaldata/issues
- Query examples: See [SQLITE_QUERIES.md](SQLITE_QUERIES.md)

For Datasette issues:
- Datasette GitHub: https://github.com/simonw/datasette/issues
- Community: https://datasette.io/discord
