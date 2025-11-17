#!/bin/bash

# Unjournal SQLite Sync - Installation Script for Linode Server
# This script sets up everything needed for automated Coda → SQLite exports

set -e  # Exit on error

echo "========================================"
echo "Unjournal SQLite Sync - Installation"
echo "========================================"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Configuration
INSTALL_DIR="/opt/unjournal"
DATA_DIR="/var/lib/unjournal"
LOG_DIR="/var/log/unjournal"
DB_PATH="$DATA_DIR/unjournal_data.db"

# ========================================
# 1. CHECK PREREQUISITES
# ========================================
echo ""
echo "1. Checking prerequisites..."

# Check if running as root or with sudo
if [ "$EUID" -ne 0 ]; then
    echo -e "${YELLOW}This script should be run with sudo${NC}"
    echo "Run: sudo bash $0"
    exit 1
fi

# Check OS
if [ -f /etc/os-release ]; then
    . /etc/os-release
    echo "   OS: $NAME $VERSION"
else
    echo -e "${RED}Cannot determine OS version${NC}"
    exit 1
fi

# ========================================
# 2. INSTALL SQLITE3
# ========================================
echo ""
echo "2. Installing SQLite3..."

if command -v sqlite3 &> /dev/null; then
    SQLITE_VERSION=$(sqlite3 --version | awk '{print $1}')
    echo -e "   ${GREEN}✓ SQLite3 already installed: $SQLITE_VERSION${NC}"
else
    echo "   Installing SQLite3..."
    apt-get update -qq
    apt-get install -y sqlite3 libsqlite3-dev
    echo -e "   ${GREEN}✓ SQLite3 installed${NC}"
fi

# ========================================
# 3. INSTALL PYTHON DEPENDENCIES
# ========================================
echo ""
echo "3. Installing Python dependencies..."

# Check Python version
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version)
    echo "   $PYTHON_VERSION"
else
    echo -e "${RED}Python 3 not found. Please install Python 3.8+${NC}"
    exit 1
fi

# Check pip
if ! command -v pip3 &> /dev/null; then
    echo "   Installing pip..."
    apt-get install -y python3-pip
fi

# Install required Python packages
echo "   Installing Python packages (codaio, pandas, python-dotenv)..."
pip3 install --quiet codaio pandas python-dotenv

echo -e "   ${GREEN}✓ Python dependencies installed${NC}"

# ========================================
# 4. CREATE DIRECTORY STRUCTURE
# ========================================
echo ""
echo "4. Creating directory structure..."

# Create directories
mkdir -p "$INSTALL_DIR"
mkdir -p "$DATA_DIR"
mkdir -p "$DATA_DIR/backups"
mkdir -p "$LOG_DIR"

# Set permissions
chmod 755 "$INSTALL_DIR"
chmod 750 "$DATA_DIR"
chmod 750 "$LOG_DIR"

echo "   Created:"
echo "     $INSTALL_DIR (code repository)"
echo "     $DATA_DIR (database storage)"
echo "     $DATA_DIR/backups (automated backups)"
echo "     $LOG_DIR (logs)"

# ========================================
# 5. SETUP ENVIRONMENT FILE
# ========================================
echo ""
echo "5. Setting up environment file..."

ENV_FILE="$DATA_DIR/.env"

if [ -f "$ENV_FILE" ]; then
    echo -e "   ${YELLOW}Environment file already exists: $ENV_FILE${NC}"
    echo "   Skipping creation (won't overwrite existing API key)"
else
    echo "   Creating environment file template..."
    cat > "$ENV_FILE" << 'EOF'
# Coda API Key
# Get your API key from: https://coda.io/account
CODA_API_KEY=your-api-key-here
EOF

    chmod 600 "$ENV_FILE"
    echo -e "   ${YELLOW}⚠ IMPORTANT: Edit $ENV_FILE and add your Coda API key${NC}"
    echo "   Run: sudo nano $ENV_FILE"
fi

# ========================================
# 6. CLONE/UPDATE REPOSITORY
# ========================================
echo ""
echo "6. Setting up code repository..."

if [ -d "$INSTALL_DIR/.git" ]; then
    echo "   Repository already exists. Updating..."
    cd "$INSTALL_DIR"
    git pull origin main
else
    echo "   Cloning repository..."
    git clone https://github.com/unjournal/unjournaldata.git "$INSTALL_DIR"
fi

echo -e "   ${GREEN}✓ Repository ready at $INSTALL_DIR${NC}"

# ========================================
# 7. INITIALIZE DATABASE
# ========================================
echo ""
echo "7. Initializing SQLite database..."

# Create a symlink to .env in the repo directory
ln -sf "$ENV_FILE" "$INSTALL_DIR/.Renviron"

# Test database creation (will create schema)
if [ -f "$DB_PATH" ]; then
    echo "   Database already exists: $DB_PATH"
    SIZE=$(du -h "$DB_PATH" | cut -f1)
    echo "   Current size: $SIZE"
else
    echo "   Creating new database..."
    # The export script will create the schema on first run
    echo "   Schema will be created on first export"
fi

# ========================================
# 8. CREATE BACKUP SCRIPT
# ========================================
echo ""
echo "8. Creating backup script..."

BACKUP_SCRIPT="$DATA_DIR/backup_database.sh"
cat > "$BACKUP_SCRIPT" << 'EOF'
#!/bin/bash
# Backup Unjournal SQLite database

BACKUP_DIR="/var/lib/unjournal/backups"
DB_PATH="/var/lib/unjournal/unjournal_data.db"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_FILE="$BACKUP_DIR/unjournal_data_$TIMESTAMP.db"

# Create backup
sqlite3 "$DB_PATH" ".backup '$BACKUP_FILE'"

# Compress backup
gzip "$BACKUP_FILE"

# Delete backups older than 30 days
find "$BACKUP_DIR" -name "*.db.gz" -mtime +30 -delete

echo "Backup created: ${BACKUP_FILE}.gz"
EOF

chmod +x "$BACKUP_SCRIPT"
echo -e "   ${GREEN}✓ Backup script created: $BACKUP_SCRIPT${NC}"

# ========================================
# 9. TEST INSTALLATION
# ========================================
echo ""
echo "9. Testing installation..."

# Test SQLite
echo -n "   Testing SQLite... "
if sqlite3 --version &> /dev/null; then
    echo -e "${GREEN}✓${NC}"
else
    echo -e "${RED}✗ FAILED${NC}"
    exit 1
fi

# Test Python imports
echo -n "   Testing Python imports... "
if python3 -c "import codaio, pandas, dotenv" 2>/dev/null; then
    echo -e "${GREEN}✓${NC}"
else
    echo -e "${RED}✗ FAILED${NC}"
    echo "   Try: pip3 install codaio pandas python-dotenv"
    exit 1
fi

# Test repository
echo -n "   Testing repository... "
if [ -f "$INSTALL_DIR/code/export_to_sqlite.py" ]; then
    echo -e "${GREEN}✓${NC}"
else
    echo -e "${RED}✗ Export script not found${NC}"
    exit 1
fi

# ========================================
# 10. INSTALLATION COMPLETE
# ========================================
echo ""
echo "========================================"
echo -e "${GREEN}Installation Complete!${NC}"
echo "========================================"
echo ""
echo "Next steps:"
echo ""
echo "1. Add your Coda API key:"
echo "   sudo nano $ENV_FILE"
echo ""
echo "2. Test the export manually:"
echo "   cd $INSTALL_DIR"
echo "   sudo python3 code/export_to_sqlite.py --db-path $DB_PATH"
echo ""
echo "3. Set up automated sync (see LINODE_CRON_SETUP.md):"
echo "   sudo crontab -e"
echo "   Add: 0 2 * * * $INSTALL_DIR/linode_setup/sync_cron.sh"
echo ""
echo "4. Create weekly backups:"
echo "   sudo crontab -e"
echo "   Add: 0 3 * * 0 $BACKUP_SCRIPT"
echo ""
echo "Database location: $DB_PATH"
echo "Logs location: $LOG_DIR"
echo "Backups location: $DATA_DIR/backups"
echo ""
echo "For help, see: $INSTALL_DIR/LINODE_CRON_SETUP.md"
echo "========================================"
