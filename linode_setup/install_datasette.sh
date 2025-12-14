#!/bin/bash

# Install Datasette - Web GUI for SQLite Database
# This provides a beautiful, read-only interface to browse the Unjournal database

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo "========================================"
echo "Installing Datasette Web GUI"
echo "========================================"
echo ""

# Check if running as root
if [ "$EUID" -ne 0 ]; then
    echo -e "${YELLOW}This script should be run with sudo${NC}"
    exit 1
fi

# 1. Install Datasette and plugins
echo "1. Installing Datasette and plugins..."
pip3 install --break-system-packages datasette datasette-auth-passwords datasette-cluster-map

# 2. Create datasette user and directory
echo ""
echo "2. Creating datasette service user..."
useradd -r -s /bin/false datasette 2>/dev/null || echo "   User 'datasette' already exists"

# 3. Create configuration directory
echo ""
echo "3. Creating configuration..."
mkdir -p /etc/datasette
chown datasette:datasette /etc/datasette

# Create metadata file
cat > /etc/datasette/metadata.json << 'EOF'
{
  "title": "Unjournal Data Explorer",
  "description": "Browse The Unjournal evaluation data",
  "license": "CC0",
  "license_url": "https://creativecommons.org/publicdomain/zero/1.0/",
  "source": "Coda.io",
  "source_url": "https://github.com/unjournal/unjournaldata",
  "databases": {
    "unjournal_data": {
      "title": "Unjournal Evaluations Database",
      "description": "Research papers, evaluations, and metadata from The Unjournal",
      "tables": {
        "research": {
          "title": "Research Papers",
          "description": "Evaluated papers and projects"
        },
        "evaluator_ratings": {
          "title": "Evaluator Ratings",
          "description": "Quantitative ratings given by evaluators"
        },
        "paper_authors": {
          "title": "Paper Authors",
          "description": "Authors per paper"
        },
        "survey_responses": {
          "title": "Survey Responses",
          "description": "Evaluator survey data (public fields only)"
        },
        "evaluator_paper_level": {
          "title": "Evaluator-Paper Level",
          "description": "Combined dataset with privacy protections"
        },
        "researchers_evaluators": {
          "title": "Researchers & Evaluators Pool",
          "description": "Public information about evaluators (no emails or personal data)"
        }
      }
    }
  }
}
EOF

# Create settings file (with authentication)
cat > /etc/datasette/settings.json << 'EOF'
{
  "allow": {
    "unauthenticated": false
  },
  "plugins": {
    "datasette-auth-passwords": {
      "admin_password_hash": "REPLACE_WITH_HASH"
    }
  }
}
EOF

# 4. Create systemd service
echo ""
echo "4. Creating systemd service..."
cat > /etc/systemd/system/datasette.service << 'EOF'
[Unit]
Description=Datasette - Unjournal Data Explorer
After=network.target

[Service]
Type=simple
User=datasette
Group=datasette
WorkingDirectory=/var/lib/unjournal
ExecStart=/usr/local/bin/datasette serve \
    /var/lib/unjournal/unjournal_data.db \
    --metadata /etc/datasette/metadata.json \
    --setting settings /etc/datasette/settings.json \
    --host 0.0.0.0 \
    --port 8001 \
    --cors
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF

# 5. Set permissions
echo ""
echo "5. Setting permissions..."
chown -R datasette:datasette /etc/datasette
chmod 755 /etc/datasette
chmod 644 /etc/datasette/metadata.json
chmod 600 /etc/datasette/settings.json

# Allow datasette user to read the database
usermod -a -G root datasette
chmod 750 /var/lib/unjournal
chmod 640 /var/lib/unjournal/unjournal_data.db
chown root:datasette /var/lib/unjournal/unjournal_data.db

# 6. Reload systemd
systemctl daemon-reload

echo ""
echo "========================================"
echo -e "${GREEN}Datasette Installed!${NC}"
echo "========================================"
echo ""
echo "NEXT STEPS:"
echo ""
echo "1. Set a password for the admin user:"
echo "   datasette hash-password"
echo "   (Copy the hash)"
echo ""
echo "2. Edit the settings file and replace REPLACE_WITH_HASH:"
echo "   sudo nano /etc/datasette/settings.json"
echo ""
echo "3. Start the service:"
echo "   sudo systemctl start datasette"
echo "   sudo systemctl enable datasette"
echo ""
echo "4. Check status:"
echo "   sudo systemctl status datasette"
echo ""
echo "5. Access in browser:"
echo "   http://your-linode-ip:8001"
echo ""
echo "6. Configure firewall (if needed):"
echo "   sudo ufw allow 8001/tcp"
echo ""
echo "========================================"
echo ""
