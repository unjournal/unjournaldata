#!/usr/bin/env python3
"""
Update bibliometric data for Unjournal papers from OpenAlex.

This script fetches paper-level bibliometric data from OpenAlex API and updates:
1. Coda database (source of truth)
2. CSV files (for analysis)
3. SQLite database (via export_to_sqlite.py)

Data collected:
- Citation counts (cited_by_count, fwci)
- Publication venue (journal name, type)
- Funder information
- Author affiliations
- Open access status

Runs weekly on Linode server as a cron job.

Usage:
    python3 update_bibliometrics.py [--dry-run] [--skip-coda]

Environment Variables Required:
    CODA_API_KEY - API key for Coda access (only needed if updating Coda)
"""

import os
import sys
import argparse
import logging
from datetime import datetime, timedelta
from pathlib import Path
import pandas as pd
import pyalex
from pyalex import Works
from codaio import Coda, Document
from dotenv import load_dotenv

# Configure pyalex
pyalex.config.email = "contact@unjournal.org"

# Configure logging
LOG_DIR = '/var/log/unjournal'
handlers = [logging.StreamHandler(sys.stdout)]

if os.path.exists(LOG_DIR):
    handlers.append(logging.FileHandler(os.path.join(LOG_DIR, 'bibliometrics.log')))

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=handlers
)
logger = logging.getLogger(__name__)

# File paths
DATA_DIR = Path(__file__).parent.parent / "data"
BIBLIOMETRICS_CSV = DATA_DIR / "bibliometrics.csv"
BIBLIOMETRICS_HISTORY_CSV = DATA_DIR / "bibliometrics_history.csv"
RESEARCH_CSV = DATA_DIR / "research.csv"
JQL_ENRICHED_CSV = DATA_DIR / "jql-enriched.csv"

# Coda configuration
CODA_DOC_ID = "0KBG3dSZCs"
RESEARCH_TABLE_ID = "grid-Iru9Fra3tE"


def load_journal_tiers():
    """Load journal tier mappings from jql-enriched.csv."""
    if not JQL_ENRICHED_CSV.exists():
        logger.warning(f"Journal tiers file not found: {JQL_ENRICHED_CSV}")
        return {}

    try:
        jql_df = pd.read_csv(JQL_ENRICHED_CSV)
        # Create mapping of journal name (lowercase) to tier
        tier_map = {}
        for _, row in jql_df.iterrows():
            if pd.notna(row.get('Journal')) and pd.notna(row.get('unjournal_tier')):
                tier_map[row['Journal'].lower().strip()] = int(row['unjournal_tier'])
        logger.info(f"Loaded {len(tier_map)} journal tier mappings")
        return tier_map
    except Exception as e:
        logger.error(f"Error loading journal tiers: {e}")
        return {}


def get_papers_with_dois():
    """Read papers from research.csv that have DOIs."""
    if not RESEARCH_CSV.exists():
        logger.error(f"Research CSV not found: {RESEARCH_CSV}")
        return pd.DataFrame()

    df = pd.read_csv(RESEARCH_CSV)

    # Filter to papers with DOIs
    df = df[df['doi'].notna() & (df['doi'] != '')]

    # Clean DOI field - extract just the DOI if it's a URL
    def clean_doi(doi):
        if pd.isna(doi):
            return None
        doi = str(doi).strip()
        # Remove URL prefixes
        for prefix in ['https://doi.org/', 'http://doi.org/', 'doi.org/', 'doi:']:
            if doi.lower().startswith(prefix):
                doi = doi[len(prefix):]
        return doi.strip()

    df['doi_clean'] = df['doi'].apply(clean_doi)
    df = df[df['doi_clean'].notna()]

    logger.info(f"Found {len(df)} papers with DOIs")
    return df


def fetch_openalex_data(doi):
    """
    Fetch bibliometric data from OpenAlex for a single DOI.

    Returns dict with:
        - openalex_id
        - cited_by_count
        - fwci (field-weighted citation impact)
        - published_journal
        - journal_type
        - funders (comma-separated string)
        - author_count
        - institution_count
        - countries (comma-separated)
        - is_open_access
        - publication_date
    """
    try:
        # Query OpenAlex by DOI
        work = Works()[f"https://doi.org/{doi}"]

        if not work:
            logger.debug(f"No OpenAlex result for DOI: {doi}")
            return None

        # Extract data
        result = {
            'openalex_id': work.get('id', ''),
            'cited_by_count': work.get('cited_by_count', 0),
            'fwci': work.get('fwci'),
            'publication_date': work.get('publication_date'),
            'is_open_access': work.get('open_access', {}).get('is_oa', False),
        }

        # Publication venue
        primary_location = work.get('primary_location', {}) or {}
        source = primary_location.get('source', {}) or {}
        result['published_journal'] = source.get('display_name', '')
        result['journal_type'] = source.get('type', '')

        # Funders
        funders = work.get('funders', []) or []
        funder_names = [f.get('display_name', '') for f in funders if f.get('display_name')]
        result['funders'] = '; '.join(funder_names) if funder_names else ''

        # Authors and affiliations
        authorships = work.get('authorships', []) or []
        result['author_count'] = len(authorships)

        institutions = set()
        countries = set()
        for authorship in authorships:
            for inst in authorship.get('institutions', []) or []:
                if inst.get('display_name'):
                    institutions.add(inst['display_name'])
                if inst.get('country_code'):
                    countries.add(inst['country_code'])

        result['institution_count'] = len(institutions)
        result['institutions'] = '; '.join(sorted(institutions)) if institutions else ''
        result['countries'] = ', '.join(sorted(countries)) if countries else ''

        return result

    except Exception as e:
        logger.debug(f"Error fetching OpenAlex data for DOI {doi}: {e}")
        return None


def fetch_all_bibliometrics(papers_df, tier_map, update_threshold_days=7):
    """
    Fetch bibliometric data for all papers.

    Args:
        papers_df: DataFrame with paper info including doi_clean column
        tier_map: Dict mapping journal names to tiers
        update_threshold_days: Skip papers updated within this many days

    Returns:
        DataFrame with bibliometric data
    """
    results = []

    # Load existing bibliometrics to check last updated
    existing_df = pd.DataFrame()
    if BIBLIOMETRICS_CSV.exists():
        try:
            existing_df = pd.read_csv(BIBLIOMETRICS_CSV)
            existing_df['last_updated'] = pd.to_datetime(existing_df['last_updated'])
        except Exception as e:
            logger.warning(f"Could not load existing bibliometrics: {e}")

    cutoff_date = datetime.now() - timedelta(days=update_threshold_days)

    for idx, row in papers_df.iterrows():
        doi = row['doi_clean']
        paper_title = row['label_paper_title']

        # Check if recently updated
        if not existing_df.empty:
            existing_row = existing_df[existing_df['doi'] == doi]
            if not existing_row.empty:
                last_updated = existing_row.iloc[0]['last_updated']
                if pd.notna(last_updated) and last_updated > cutoff_date:
                    logger.debug(f"Skipping recently updated: {paper_title[:50]}...")
                    # Keep existing data
                    results.append(existing_row.iloc[0].to_dict())
                    continue

        logger.info(f"Fetching: {paper_title[:60]}...")

        # Fetch from OpenAlex
        data = fetch_openalex_data(doi)

        if data:
            data['paper_title'] = paper_title
            data['doi'] = doi

            # Look up journal tier
            journal_name = data.get('published_journal', '')
            if journal_name:
                tier = tier_map.get(journal_name.lower().strip())
                data['journal_tier'] = tier
            else:
                data['journal_tier'] = None

            data['last_updated'] = datetime.now().isoformat()
            results.append(data)
        else:
            # Keep basic info even if OpenAlex lookup failed
            results.append({
                'paper_title': paper_title,
                'doi': doi,
                'last_updated': datetime.now().isoformat(),
                'fetch_status': 'not_found'
            })

    return pd.DataFrame(results)


def save_bibliometrics_csv(df):
    """Save current bibliometrics to CSV."""
    # Define column order
    columns = [
        'paper_title', 'doi', 'openalex_id',
        'cited_by_count', 'fwci',
        'published_journal', 'journal_type', 'journal_tier',
        'funders',
        'author_count', 'institution_count', 'institutions', 'countries',
        'is_open_access', 'publication_date',
        'last_updated', 'fetch_status'
    ]

    # Keep only columns that exist
    existing_cols = [c for c in columns if c in df.columns]
    df = df[existing_cols]

    df.to_csv(BIBLIOMETRICS_CSV, index=False)
    logger.info(f"Saved {len(df)} rows to {BIBLIOMETRICS_CSV}")


def append_history_csv(df):
    """Append current snapshot to history CSV for time series tracking."""
    snapshot_date = datetime.now().date().isoformat()

    # Select columns for history
    history_cols = ['paper_title', 'doi', 'cited_by_count', 'fwci']
    history_df = df[history_cols].copy()
    history_df['snapshot_date'] = snapshot_date

    # Append to existing history
    if BIBLIOMETRICS_HISTORY_CSV.exists():
        existing_history = pd.read_csv(BIBLIOMETRICS_HISTORY_CSV)

        # Remove any existing entries for today (in case of re-run)
        existing_history = existing_history[existing_history['snapshot_date'] != snapshot_date]

        history_df = pd.concat([existing_history, history_df], ignore_index=True)

    history_df.to_csv(BIBLIOMETRICS_HISTORY_CSV, index=False)
    logger.info(f"Saved history snapshot to {BIBLIOMETRICS_HISTORY_CSV}")


def update_coda(df, dry_run=False):
    """
    Update Coda database with bibliometric data.

    Uses existing Coda column names:
    - "citation count (NB - we can automate this with DOI)" for citations
    - "citation count update date" for timestamp
    - "Funded by (DOI)" for funders
    - "Journal publication title (DOI)" for journal name
    """
    if dry_run:
        logger.info("[DRY RUN] Would update Coda with bibliometric data")
        return

    coda_api_key = os.environ.get("CODA_API_KEY")
    if not coda_api_key:
        logger.warning("CODA_API_KEY not set, skipping Coda update")
        return

    try:
        coda = Coda(coda_api_key)
        doc = Document(CODA_DOC_ID, coda=coda)
        table = doc.get_table(RESEARCH_TABLE_ID)

        # Get all rows to find matching paper titles
        rows = list(table.rows())
        logger.info(f"Found {len(rows)} rows in Coda research table")

        updated_count = 0
        skipped_count = 0
        for _, bib_row in df.iterrows():
            paper_title = bib_row.get('paper_title')
            if not paper_title or bib_row.get('fetch_status') == 'not_found':
                skipped_count += 1
                continue

            # Find matching row in Coda
            matching_row = None
            for row in rows:
                if row.values.get('label_paper_title') == paper_title:
                    matching_row = row
                    break

            if not matching_row:
                logger.debug(f"No Coda row found for: {paper_title[:50]}...")
                skipped_count += 1
                continue

            # Prepare update data using EXISTING Coda column names
            update_data = {}

            # Citation count
            if pd.notna(bib_row.get('cited_by_count')):
                update_data['citation count (NB - we can automate this with DOI)'] = int(bib_row['cited_by_count'])

            # Update timestamp
            update_data['citation count update date'] = datetime.now().strftime('%Y-%m-%d')

            # Journal name
            if bib_row.get('published_journal'):
                update_data['Journal publication title (DOI)'] = bib_row['published_journal']

            # Funders
            if bib_row.get('funders'):
                update_data['Funded by (DOI)'] = bib_row['funders']

            if update_data:
                try:
                    matching_row.update(update_data)
                    updated_count += 1
                    if updated_count % 10 == 0:
                        logger.info(f"Updated {updated_count} rows so far...")
                except Exception as e:
                    logger.warning(f"Could not update Coda row for {paper_title[:50]}: {e}")

        logger.info(f"Updated {updated_count} rows in Coda (skipped {skipped_count})")

    except Exception as e:
        logger.error(f"Error updating Coda: {e}", exc_info=True)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Update bibliometric data from OpenAlex")
    parser.add_argument("--dry-run", action="store_true",
                       help="Don't write to Coda, only update CSV files")
    parser.add_argument("--skip-coda", action="store_true",
                       help="Skip Coda update entirely")
    parser.add_argument("--force", action="store_true",
                       help="Force update all papers regardless of last_updated")
    args = parser.parse_args()

    start_time = datetime.now()
    logger.info("="*80)
    logger.info("Starting bibliometrics update")
    logger.info(f"Dry run: {args.dry_run}")
    logger.info("="*80)

    # Load environment variables
    if os.path.isfile(".Renviron"):
        load_dotenv(dotenv_path=".Renviron")
    if os.path.isfile("/var/lib/unjournal/.env"):
        load_dotenv(dotenv_path="/var/lib/unjournal/.env")

    # Load journal tier mappings
    tier_map = load_journal_tiers()

    # Get papers with DOIs
    papers_df = get_papers_with_dois()
    if papers_df.empty:
        logger.warning("No papers with DOIs found")
        return 1

    # Fetch bibliometric data
    update_threshold = 0 if args.force else 7  # days
    bib_df = fetch_all_bibliometrics(papers_df, tier_map, update_threshold)

    if bib_df.empty:
        logger.warning("No bibliometric data fetched")
        return 1

    # Save to CSV
    save_bibliometrics_csv(bib_df)

    # Append to history
    # Only include rows that have citation data (successful fetches)
    success_df = bib_df[bib_df['cited_by_count'].notna()]
    if not success_df.empty:
        append_history_csv(success_df)

    # Update Coda
    if not args.skip_coda:
        update_coda(bib_df, dry_run=args.dry_run)
    else:
        logger.info("Skipping Coda update (--skip-coda)")

    # Summary
    end_time = datetime.now()
    duration = (end_time - start_time).total_seconds()

    logger.info("\n" + "="*80)
    logger.info("BIBLIOMETRICS UPDATE SUMMARY")
    logger.info("="*80)
    logger.info(f"Duration: {duration:.2f} seconds")
    logger.info(f"Papers processed: {len(papers_df)}")
    logger.info(f"Successful fetches: {len(success_df)}")
    logger.info(f"CSV saved to: {BIBLIOMETRICS_CSV}")
    logger.info(f"History saved to: {BIBLIOMETRICS_HISTORY_CSV}")
    logger.info("="*80)

    return 0


if __name__ == "__main__":
    sys.exit(main())
