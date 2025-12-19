# Unjournal Data - Documentation Index

Complete guide to all documentation in this repository.

## Quick Start

New to the project? Start here:
1. **[README.md](../README.md)** - Project overview and quick start guide
2. **[CLAUDE.md](../CLAUDE.md)** - Detailed architecture and developer guide

## Documentation by Category

### Core Documentation

- **[README.md](../README.md)** - Project overview, data pipeline, quick start
- **[CLAUDE.md](../CLAUDE.md)** - Complete architecture, key commands, data flow, directory structure

### Data & Privacy

- **[EVALUATOR_DATASET_README.md](../EVALUATOR_DATASET_README.md)** - Evaluator-paper dataset documentation and privacy protections
- **[data/IMPORT_INSTRUCTIONS.md](../data/IMPORT_INSTRUCTIONS.md)** - Data import instructions

### Linode Server & Database

Setup and management:
- **[LINODE_CRON_SETUP.md](../LINODE_CRON_SETUP.md)** - Complete setup guide for Linode server automation
- **[DATASETTE_GUI_SETUP.md](DATASETTE_GUI_SETUP.md)** - Datasette web GUI installation and configuration
- **[LINODE_SQLITE_INTERNAL_GUIDE.md](LINODE_SQLITE_INTERNAL_GUIDE.md)** - Internal guide for database management
- **[LINODE_SETUP_FAQ.md](LINODE_SETUP_FAQ.md)** - Frequently asked questions

Usage:
- **[SQLITE_QUERIES.md](SQLITE_QUERIES.md)** - Example SQL queries for data analysis

### Working Documentation

Analysis and development notes:
- **[MISSING_DATA_SUMMARY.md](../MISSING_DATA_SUMMARY.md)** - Analysis of missing data in evaluations
- **[PUBPUB_LOOKUP_NEEDED.md](../PUBPUB_LOOKUP_NEEDED.md)** - PubPub data lookup requirements
- **[WIDE_FORMAT_INTEGRATION_SUMMARY.md](../WIDE_FORMAT_INTEGRATION_SUMMARY.md)** - Wide-format dataset integration notes
- **[AGENTS.md](../AGENTS.md)** - Agent/automation configuration notes

## Documentation by Task

### Setting Up the Project Locally

1. Clone repository: See [README.md](../README.md)
2. Install Python dependencies: See [CLAUDE.md](../CLAUDE.md) → Python Environment
3. Install R dependencies: See [CLAUDE.md](../CLAUDE.md) → R Environment
4. Configure API keys: See [CLAUDE.md](../CLAUDE.md) → Security & Secrets

### Importing Data from Coda

1. Get CODA_API_KEY: See [CLAUDE.md](../CLAUDE.md) → Security & Secrets
2. Run import script: See [CLAUDE.md](../CLAUDE.md) → Data Import
3. Create evaluator-paper dataset: See [EVALUATOR_DATASET_README.md](../EVALUATOR_DATASET_README.md)

### Setting Up SQLite Database (Linode)

1. **[LINODE_CRON_SETUP.md](../LINODE_CRON_SETUP.md)** - Complete automated setup
2. **[DATASETTE_GUI_SETUP.md](DATASETTE_GUI_SETUP.md)** - Web interface setup
3. **[LINODE_SQLITE_INTERNAL_GUIDE.md](LINODE_SQLITE_INTERNAL_GUIDE.md)** - Management and maintenance

### Working with Data

1. **CSV format**: See [README.md](../README.md) → Data
2. **SQLite format**: See [SQLITE_QUERIES.md](SQLITE_QUERIES.md)
3. **Privacy considerations**: See [EVALUATOR_DATASET_README.md](../EVALUATOR_DATASET_README.md)

### Publishing Dashboards

1. **Shiny dashboard**: See [CLAUDE.md](../CLAUDE.md) → Dashboard Development
2. **Website/blog**: See [CLAUDE.md](../CLAUDE.md) → Website Publishing

### PubPub Integration

- **[README.md](../README.md)** → PubPub export utility
- Script: `code/harvest_pubpub_assets.py`

## File Organization

```
unjournaldata/
├── README.md                          # Project overview
├── CLAUDE.md                          # Architecture guide
├── EVALUATOR_DATASET_README.md        # Dataset documentation
├── LINODE_CRON_SETUP.md              # Linode setup
├── MISSING_DATA_SUMMARY.md           # Analysis notes
├── PUBPUB_LOOKUP_NEEDED.md           # PubPub notes
├── WIDE_FORMAT_INTEGRATION_SUMMARY.md # Integration notes
├── AGENTS.md                          # Automation notes
│
├── docs/                              # Operational guides
│   ├── INDEX.md                       # This file
│   ├── DATASETTE_GUI_SETUP.md        # Web GUI setup
│   ├── LINODE_SQLITE_INTERNAL_GUIDE.md # DB management
│   ├── LINODE_SETUP_FAQ.md           # FAQ
│   └── SQLITE_QUERIES.md             # Query examples
│
├── code/                              # Scripts
├── data/                              # CSV data files
├── linode_setup/                      # Linode scripts
├── shinyapp/                          # Shiny dashboards
└── website/                           # Quarto website
```

## Update History

- **2025-12-19**: Created comprehensive documentation index
- **2025-12-15**: Added Datasette GUI documentation
- **2025-11-17**: Added Linode setup guides
- **2025-11-14**: Added evaluator-paper dataset documentation

## Need Help?

- **Bug reports**: https://github.com/unjournal/unjournaldata/issues
- **Questions about data**: See [EVALUATOR_DATASET_README.md](../EVALUATOR_DATASET_README.md)
- **Linode/SQLite issues**: See [LINODE_SETUP_FAQ.md](LINODE_SETUP_FAQ.md)
