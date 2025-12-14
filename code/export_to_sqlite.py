#!/usr/bin/env python3
"""
Export Unjournal data from Coda to SQLite database.

This script exports all relevant Unjournal tables from Coda to a SQLite database,
suitable for running on a Linode server as a daily cron job.

Tables exported:
1. Research papers (from research/eval doc)
2. Evaluator ratings (from research/eval doc)
3. Paper authors (from research/eval doc)
4. Survey responses - academic stream (from research/eval doc)
5. Survey responses - applied stream (from research/eval doc)
6. Evaluator-paper combined dataset (generated)
7. Researchers & Evaluators pool (from team management doc)

Usage:
    python3 export_to_sqlite.py [--db-path /path/to/database.db]

Environment Variables Required:
    CODA_API_KEY - API key for Coda access
"""

import sqlite3
import pandas as pd
import os
import sys
from datetime import datetime
from pathlib import Path
import argparse
import logging
from codaio import Coda, Document
from dotenv import load_dotenv

# Configure logging
LOG_DIR = '/var/log/unjournal'
handlers = [logging.StreamHandler(sys.stdout)]

# Add file handler only if log directory exists
if os.path.exists(LOG_DIR):
    handlers.append(logging.FileHandler(os.path.join(LOG_DIR, 'sqlite_export.log')))

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=handlers
)
logger = logging.getLogger(__name__)


def setup_database(db_path):
    """Create database and tables with proper schema."""
    logger.info(f"Setting up database at {db_path}")

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create schema
    schema = """
    -- Research papers table
    CREATE TABLE IF NOT EXISTS research (
        label_paper_title TEXT PRIMARY KEY,
        status TEXT,
        research_url TEXT,
        doi TEXT,
        main_cause_cat TEXT,
        main_cause_cat_abbrev TEXT,
        secondary_cause_cat TEXT,
        evaluations_url TEXT,
        source_url TEXT,
        overall_mean_score REAL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    -- Evaluator ratings table (long format)
    CREATE TABLE IF NOT EXISTS evaluator_ratings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        research TEXT,
        evaluator TEXT,
        criteria TEXT,
        middle_rating REAL,
        lower_CI REAL,
        upper_CI REAL,
        confidence_level TEXT,
        row_created_date TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (research) REFERENCES research(label_paper_title),
        UNIQUE(research, evaluator, criteria)
    );

    -- Paper authors table
    CREATE TABLE IF NOT EXISTS paper_authors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        research TEXT,
        author TEXT,
        author_emails TEXT,
        corresponding TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (research) REFERENCES research(label_paper_title)
    );

    -- Survey responses (combined academic + applied)
    CREATE TABLE IF NOT EXISTS survey_responses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        paper_title TEXT,
        evaluation_stream TEXT,
        years_in_field TEXT,
        papers_reviewed TEXT,
        time_spent TEXT,
        field_expertise TEXT,
        research_link_coda TEXT,
        status TEXT,
        date_entered TEXT,
        hours_spent_manual_impute REAL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    -- Evaluator-paper level dataset (wide format)
    CREATE TABLE IF NOT EXISTS evaluator_paper_level (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        evaluator TEXT,
        paper_title TEXT,
        evaluation_stream TEXT,
        years_in_field TEXT,
        papers_reviewed TEXT,
        time_spent TEXT,
        field_expertise TEXT,
        -- Rating criteria (middle ratings)
        adv_knowledge_rating REAL,
        claims_rating REAL,
        gp_relevance_rating REAL,
        journal_predict_rating REAL,
        logic_comms_rating REAL,
        merits_journal_rating REAL,
        methods_rating REAL,
        open_sci_rating REAL,
        overall_rating REAL,
        real_world_rating REAL,
        -- Confidence intervals (lower)
        adv_knowledge_lower REAL,
        claims_lower REAL,
        gp_relevance_lower REAL,
        journal_predict_lower REAL,
        logic_comms_lower REAL,
        merits_journal_lower REAL,
        methods_lower REAL,
        open_sci_lower REAL,
        overall_lower REAL,
        real_world_lower REAL,
        -- Confidence intervals (upper)
        adv_knowledge_upper REAL,
        claims_upper REAL,
        gp_relevance_upper REAL,
        journal_predict_upper REAL,
        logic_comms_upper REAL,
        merits_journal_upper REAL,
        methods_upper REAL,
        open_sci_upper REAL,
        overall_upper REAL,
        real_world_upper REAL,
        -- Metadata
        research_link_coda TEXT,
        status TEXT,
        date_entered TEXT,
        hours_spent REAL,
        research_url TEXT,
        doi TEXT,
        main_cause_cat TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        UNIQUE(paper_title, evaluator)
    );

    -- Researchers & Evaluators pool
    CREATE TABLE IF NOT EXISTS researchers_evaluators (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name_text TEXT UNIQUE,
        email TEXT,
        expertise TEXT,
        affiliated_organization TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    -- Export metadata
    CREATE TABLE IF NOT EXISTS export_metadata (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        table_name TEXT,
        row_count INTEGER,
        export_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        status TEXT,
        error_message TEXT
    );

    -- Create indexes for better query performance
    CREATE INDEX IF NOT EXISTS idx_ratings_research ON evaluator_ratings(research);
    CREATE INDEX IF NOT EXISTS idx_ratings_evaluator ON evaluator_ratings(evaluator);
    CREATE INDEX IF NOT EXISTS idx_ratings_criteria ON evaluator_ratings(criteria);
    CREATE INDEX IF NOT EXISTS idx_authors_research ON paper_authors(research);
    CREATE INDEX IF NOT EXISTS idx_eval_paper_evaluator ON evaluator_paper_level(evaluator);
    CREATE INDEX IF NOT EXISTS idx_eval_paper_paper ON evaluator_paper_level(paper_title);
    """

    cursor.executescript(schema)
    conn.commit()
    conn.close()
    logger.info("Database schema created successfully")


def export_table(conn, df, table_name, unique_columns=None):
    """
    Export dataframe to SQLite with upsert logic.

    Args:
        conn: SQLite connection
        df: Pandas DataFrame to export
        table_name: Name of table to export to
        unique_columns: List of columns that define uniqueness (for upsert)
    """
    if df.empty:
        logger.warning(f"Skipping {table_name} - no data")
        return 0

    logger.info(f"Exporting {len(df)} rows to {table_name}")

    try:
        # Add timestamps
        df['updated_at'] = datetime.now().isoformat()
        if 'created_at' not in df.columns:
            df['created_at'] = datetime.now().isoformat()

        if unique_columns:
            # Upsert: update if exists, insert if not
            cursor = conn.cursor()
            for _, row in df.iterrows():
                # Build WHERE clause for unique columns
                where_parts = [f"{col} = ?" for col in unique_columns]
                where_clause = " AND ".join(where_parts)
                where_values = [row[col] for col in unique_columns]

                # Check if row exists
                query = f"SELECT COUNT(*) FROM {table_name} WHERE {where_clause}"
                cursor.execute(query, where_values)
                exists = cursor.fetchone()[0] > 0

                if exists:
                    # Update existing row
                    set_parts = [f"{col} = ?" for col in df.columns if col not in unique_columns]
                    set_clause = ", ".join(set_parts)
                    set_values = [row[col] for col in df.columns if col not in unique_columns]

                    update_query = f"UPDATE {table_name} SET {set_clause} WHERE {where_clause}"
                    cursor.execute(update_query, set_values + where_values)
                else:
                    # Insert new row
                    df_single = pd.DataFrame([row])
                    df_single.to_sql(table_name, conn, if_exists='append', index=False)

            conn.commit()
        else:
            # Simple replace (for tables without unique constraints)
            df.to_sql(table_name, conn, if_exists='replace', index=False)

        row_count = len(df)
        logger.info(f"Successfully exported {row_count} rows to {table_name}")
        return row_count

    except Exception as e:
        logger.error(f"Error exporting to {table_name}: {str(e)}")
        raise


def main(db_path=None):
    """Main export function."""
    start_time = datetime.now()
    logger.info("="*80)
    logger.info("Starting Coda to SQLite export")
    logger.info("="*80)

    # Load environment variables
    if os.path.isfile(".Renviron"):
        load_dotenv(dotenv_path=".Renviron")

    # Default database path
    if db_path is None:
        db_path = "/var/lib/unjournal/unjournal_data.db"

    # Ensure directory exists
    Path(db_path).parent.mkdir(parents=True, exist_ok=True)

    # Setup database
    setup_database(db_path)

    # Connect to database
    conn = sqlite3.connect(db_path)

    try:
        # Initialize Coda
        coda_api_key = os.environ.get("CODA_API_KEY")
        if not coda_api_key:
            raise ValueError("CODA_API_KEY environment variable not set")

        coda = Coda(coda_api_key)

        # Connect to research/evaluation document
        logger.info("Connecting to research/evaluation Coda document...")
        research_doc = Document("0KBG3dSZCs", coda=coda)

        export_stats = {}

        # ========================================
        # 1. EXPORT RESEARCH PAPERS
        # ========================================
        logger.info("\n1. Exporting research papers...")
        research_table = research_doc.get_table("grid-Iru9Fra3tE")
        research_df = pd.DataFrame(research_table.to_dict())

        # Select columns
        research_cols = ['label_paper_title', 'status', 'research_url', 'doi',
                        'main_cause_cat', 'main_cause_cat_abbrev', 'secondary_cause_cat',
                        'evaluations_url', 'source_url', 'overall_mean_score']
        research_df = research_df[[c for c in research_cols if c in research_df.columns]]

        export_stats['research'] = export_table(
            conn, research_df, 'research',
            unique_columns=['label_paper_title']
        )

        # ========================================
        # 2. EXPORT EVALUATOR RATINGS
        # ========================================
        logger.info("\n2. Exporting evaluator ratings...")
        ratings_table = research_doc.get_table("grid-pcJr9ZM3wT")
        ratings_df = pd.DataFrame(ratings_table.to_dict())

        ratings_cols = ['research', 'evaluator', 'criteria', 'middle_rating',
                       'lower_CI', 'upper_CI', 'confidence_level', 'row_created_date']
        ratings_df = ratings_df[[c for c in ratings_cols if c in ratings_df.columns]]

        export_stats['evaluator_ratings'] = export_table(
            conn, ratings_df, 'evaluator_ratings',
            unique_columns=['research', 'evaluator', 'criteria']
        )

        # ========================================
        # 3. EXPORT PAPER AUTHORS
        # ========================================
        logger.info("\n3. Exporting paper authors...")
        authors_table = research_doc.get_table("grid-bJ5HubGR8H")
        authors_df = pd.DataFrame(authors_table.to_dict())

        authors_cols = ['research', 'author', 'author_emails', 'corresponding']
        authors_df = authors_df[[c for c in authors_cols if c in authors_df.columns]]

        export_stats['paper_authors'] = export_table(
            conn, authors_df, 'paper_authors',
            unique_columns=None  # No unique constraint, allow duplicates
        )

        # ========================================
        # 4. EXPORT SURVEY RESPONSES
        # ========================================
        logger.info("\n4. Exporting survey responses...")

        # Academic stream
        academic_survey = research_doc.get_table("grid-aDSyEIerdL")
        academic_df = pd.DataFrame(academic_survey.to_dict())
        academic_df['evaluation_stream'] = 'academic'

        # Applied stream
        applied_survey = research_doc.get_table("grid-znNSTj_xX3")
        applied_df = pd.DataFrame(applied_survey.to_dict())
        applied_df['evaluation_stream'] = 'applied'

        # Standardize column names
        academic_df = academic_df.rename(columns={'Name of the paper or project': 'paper_title'})
        applied_df = applied_df.rename(columns={'Title of the paper or project': 'paper_title'})

        # Combine
        survey_df = pd.concat([academic_df, applied_df], ignore_index=True)

        # Select public columns only (exclude confidential data)
        survey_cols = [
            'paper_title',
            'evaluation_stream',
            'How long have you been in this field?',
            'How many proposals, papers, and projects have you evaluated/reviewed (for journals, grants, or other peer-review)?',
            'Approximately how long did you spend completing this evaluation?',
            'Field/expertise',
            'research_link_coda',
            'status',
            'Date entered (includes transfer from PubPub)',
            'hours_spent_manual_impute'
        ]

        survey_df = survey_df[[c for c in survey_cols if c in survey_df.columns]]

        # Rename for database
        survey_df = survey_df.rename(columns={
            'How long have you been in this field?': 'years_in_field',
            'How many proposals, papers, and projects have you evaluated/reviewed (for journals, grants, or other peer-review)?': 'papers_reviewed',
            'Approximately how long did you spend completing this evaluation?': 'time_spent',
            'Field/expertise': 'field_expertise',
            'Date entered (includes transfer from PubPub)': 'date_entered'
        })

        export_stats['survey_responses'] = export_table(
            conn, survey_df, 'survey_responses',
            unique_columns=None
        )

        # ========================================
        # 5. EXPORT EVALUATOR-PAPER LEVEL DATASET
        # ========================================
        logger.info("\n5. Exporting evaluator-paper level dataset...")

        # Read from the CSV file we generate
        eval_paper_path = "data/evaluator_paper_level.csv"
        if os.path.exists(eval_paper_path):
            eval_paper_df = pd.read_csv(eval_paper_path)

            # Rename columns to match database schema (remove special characters)
            rename_map = {}
            for col in eval_paper_df.columns:
                if '_middle_rating' in col:
                    new_col = col.replace('_middle_rating', '_rating')
                    rename_map[col] = new_col
                elif '_lower_CI' in col:
                    new_col = col.replace('_lower_CI', '_lower')
                    rename_map[col] = new_col
                elif '_upper_CI' in col:
                    new_col = col.replace('_upper_CI', '_upper')
                    rename_map[col] = new_col
                elif col == 'How long have you been in this field?':
                    rename_map[col] = 'years_in_field'
                elif col == 'How many proposals, papers, and projects have you evaluated/reviewed (for journals, grants, or other peer-review)?':
                    rename_map[col] = 'papers_reviewed'
                elif col == 'Approximately how long did you spend completing this evaluation?':
                    rename_map[col] = 'time_spent'
                elif col == 'Field/expertise':
                    rename_map[col] = 'field_expertise'
                elif col == 'Date entered (includes transfer from PubPub)':
                    rename_map[col] = 'date_entered'
                elif col == 'hours_spent_manual_impute':
                    rename_map[col] = 'hours_spent'

            eval_paper_df = eval_paper_df.rename(columns=rename_map)

            # Drop confidence_level columns (deprecated in favor of credible intervals)
            confidence_cols = [col for col in eval_paper_df.columns if 'confidence_level' in col.lower()]
            if confidence_cols:
                eval_paper_df = eval_paper_df.drop(columns=confidence_cols)
                logger.info(f"Dropped deprecated confidence_level columns: {confidence_cols}")

            # Drop duplicate/merge columns (status_x, status_y, etc.) - keep only non-suffixed versions
            duplicate_cols = [col for col in eval_paper_df.columns if col.endswith('_x') or col.endswith('_y')]
            if duplicate_cols:
                eval_paper_df = eval_paper_df.drop(columns=duplicate_cols)
                logger.info(f"Dropped duplicate merge columns: {duplicate_cols}")

            # Select only columns that exist in the database schema
            schema_columns = [
                'evaluator', 'paper_title', 'evaluation_stream',
                'years_in_field', 'papers_reviewed', 'time_spent', 'field_expertise',
                'adv_knowledge_rating', 'claims_rating', 'gp_relevance_rating',
                'journal_predict_rating', 'logic_comms_rating', 'merits_journal_rating',
                'methods_rating', 'open_sci_rating', 'overall_rating', 'real_world_rating',
                'adv_knowledge_lower', 'claims_lower', 'gp_relevance_lower',
                'journal_predict_lower', 'logic_comms_lower', 'merits_journal_lower',
                'methods_lower', 'open_sci_lower', 'overall_lower', 'real_world_lower',
                'adv_knowledge_upper', 'claims_upper', 'gp_relevance_upper',
                'journal_predict_upper', 'logic_comms_upper', 'merits_journal_upper',
                'methods_upper', 'open_sci_upper', 'overall_upper', 'real_world_upper',
                'research_link_coda', 'status', 'date_entered', 'hours_spent',
                'research_url', 'doi', 'main_cause_cat'
            ]

            # Keep only schema columns that exist in the dataframe
            available_cols = [col for col in schema_columns if col in eval_paper_df.columns]
            eval_paper_df = eval_paper_df[available_cols]
            logger.info(f"Selected {len(available_cols)} columns matching database schema")

            export_stats['evaluator_paper_level'] = export_table(
                conn, eval_paper_df, 'evaluator_paper_level',
                unique_columns=['paper_title', 'evaluator']
            )
        else:
            logger.warning(f"Evaluator-paper level CSV not found at {eval_paper_path}")
            export_stats['evaluator_paper_level'] = 0

        # ========================================
        # 6. EXPORT RESEARCHERS & EVALUATORS (PUBLIC FIELDS ONLY)
        # ========================================
        logger.info("\n6. Exporting researchers & evaluators (public fields only)...")

        try:
            # Same document as research/eval doc
            researchers_table = research_doc.get_table("grid-GuykkYMrcn")
            researchers_df = pd.DataFrame(researchers_table.to_dict())

            # PRIVACY: Export ONLY public, non-sensitive fields
            # NEVER export: emails, CV, ORCID, comments, consent, personal details
            public_columns = [
                'Name',
                'expertise_text',
                'Affiliation',
                'Position',
                'Expertise Field',
                'Expertise Methods'
            ]

            # Filter to available public columns
            available_cols = [col for col in public_columns if col in researchers_df.columns]
            researchers_df = researchers_df[available_cols]

            # Rename for database consistency
            researchers_df = researchers_df.rename(columns={
                'Name': 'name_text',
                'Affiliation': 'affiliated_organization'
            })

            # Drop rows with no name
            researchers_df = researchers_df[researchers_df['name_text'].notna()]

            logger.info(f"Exporting {len(researchers_df)} researchers/evaluators (PUBLIC fields only)")
            logger.info(f"Excluded columns: Email, CV, ORCID, Country, Comments, Consent")

            export_stats['researchers_evaluators'] = export_table(
                conn, researchers_df, 'researchers_evaluators',
                unique_columns=['name_text']
            )
        except Exception as e:
            logger.warning(f"Could not export researchers_evaluators: {e}")
            export_stats['researchers_evaluators'] = 0

        # ========================================
        # 7. RECORD EXPORT METADATA
        # ========================================
        logger.info("\n7. Recording export metadata...")

        cursor = conn.cursor()
        for table_name, row_count in export_stats.items():
            cursor.execute("""
                INSERT INTO export_metadata (table_name, row_count, export_timestamp, status)
                VALUES (?, ?, ?, ?)
            """, (table_name, row_count, datetime.now().isoformat(), 'success'))

        conn.commit()

        # ========================================
        # SUMMARY
        # ========================================
        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds()

        logger.info("\n" + "="*80)
        logger.info("EXPORT SUMMARY")
        logger.info("="*80)
        logger.info(f"Duration: {duration:.2f} seconds")
        logger.info(f"Database: {db_path}")
        logger.info(f"Database size: {Path(db_path).stat().st_size / 1024 / 1024:.2f} MB")
        logger.info("\nRows exported:")
        for table_name, row_count in export_stats.items():
            logger.info(f"  {table_name}: {row_count}")
        logger.info("="*80)

        return 0

    except Exception as e:
        logger.error(f"Export failed: {str(e)}", exc_info=True)

        # Record failure in metadata
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO export_metadata (table_name, export_timestamp, status, error_message)
            VALUES (?, ?, ?, ?)
        """, ('ALL', datetime.now().isoformat(), 'failed', str(e)))
        conn.commit()

        return 1

    finally:
        conn.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Export Unjournal data from Coda to SQLite")
    parser.add_argument("--db-path", help="Path to SQLite database file",
                       default="/var/lib/unjournal/unjournal_data.db")
    args = parser.parse_args()

    sys.exit(main(args.db_path))
