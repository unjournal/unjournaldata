#!/usr/bin/env python3
"""
Extract COMPLETELY NEW evaluations from Coda form responses.

CORRECTED VERSION: Uses proper evaluator identification logic:
- "Identification as an author" field for evaluator name
- Assigns "Evaluator 1", "Evaluator 2", etc. when identification is blank,
  based on submission date order per paper

This script finds evaluations that exist in the academic/applied stream form
responses but are COMPLETELY MISSING from the rsx_evalr_rating table.

Usage:
    python3 code/extract_new_evaluations_from_forms_v2.py
"""

from codaio import Coda, Document
from dotenv import load_dotenv
import os
import pandas as pd
from datetime import datetime

# Load environment
if os.path.isfile(".Renviron"):
    load_dotenv(dotenv_path=".Renviron")

# Mapping from criteria names to column names in form responses
CRITERIA_MAPPING = {
    # Academic stream columns
    'academic': {
        'overall': {
            'middle': 'Overall assessment ranking',
            'lower': 'Lower Cl Overall assessment ranking',
            'upper': 'Upper Cl - Overall assessment ranking'
        },
        'adv_knowledge': {
            'middle': 'Advancing Knowledge ranking',
            'lower': 'Lower Cl - Advancing Knowledge',
            'upper': 'Upper Cl - Advancing Knowledge'
        },
        'claims': {
            'middle': 'Claims - midpoint ranking',
            'lower': 'Lower Cl - Claims',
            'upper': 'Upper Cl - Claims'
        },
        'methods': {
            'middle': 'Methods:  - midpoint ranking',
            'lower': 'Lower Cl - Methods',
            'upper': 'Upper Cl - Methods'
        },
        'logic_comms': {
            'middle': 'Logic & communication - ranking',
            'lower': 'Lower Cl - Logic & communication',
            'upper': 'Upper Cl - Logic & communication'
        },
        'open_sci': {
            'middle': 'Open, collaborative, replicable - ranking',
            'lower': 'Lower Cl - Open, collaborative, replicable',
            'upper': 'Upper Cl - Open, collaborative, replicable'
        },
        'real_world': {
            'middle': 'Relevance to global priorities, usefulness for practitioners - ranking',
            'lower': 'Lower Cl - Relevance',
            'upper': 'Upper Cl - Relevance'
        },
        'gp_relevance': {
            'middle': 'Relevance to global priorities, usefulness for practitioners - ranking',
            'lower': 'Lower Cl - Relevance',
            'upper': 'Upper Cl - Relevance'
        },
        'merits_journal': {
            'middle': 'midpoint_normative_journal',
            'lower': 'lower_ci_normative_journal',
            'upper': 'upper_ci_normative_journal'
        },
        'journal_predict': {
            'middle': 'midpoint_predicted_journal',
            'lower': 'lower_ci_predicted_journal',
            'upper': 'upper_ci_predicted_journal'
        }
    },
    # Applied stream columns
    'applied': {
        'overall': {
            'middle': 'Overall assessment ranking',
            'lower': 'Lower Cl Overall assessment ranking',
            'upper': 'Upper Cl - Overall assessment ranking'
        },
        'adv_knowledge': {
            'middle': 'Advancing Knowledge ranking',
            'lower': 'Lower Cl - Advancing Knowledge',
            'upper': 'Upper Cl - Advancing Knowledge'
        },
        'claims': {
            'middle': 'Claims - midpoint ranking',
            'lower': 'Lower Cl - Claims',
            'upper': 'Upper Cl - Claims'
        },
        'methods': {
            'middle': 'Methods:  - midpoint ranking',
            'lower': 'Lower Cl - Methods',
            'upper': 'Upper Cl - Methods'
        },
        'logic_comms': {
            'middle': 'midpoint_logic_comms',
            'lower': 'lower_ci_logic_comms',
            'upper': 'upper_ci_logic_comms'
        },
        'open_sci': {
            'middle': 'midpoint_ci_replicable',
            'lower': 'lower_ci_replicable',
            'upper': 'upper_ci_replicable'
        },
        'real_world': {
            'middle': 'midpoint_relevance',
            'lower': 'lower_ci_relevance',
            'upper': 'upper_ci_relevance'
        },
        'gp_relevance': {
            'middle': 'midpoint_relevance',
            'lower': 'lower_ci_relevance',
            'upper': 'upper_ci_relevance'
        },
        'merits_journal': {
            'middle': 'midpoint_normative_journal',
            'lower': 'lower_ci_normative_journal',
            'upper': 'upper_ci_normative_journal'
        },
        'journal_predict': {
            'middle': 'midpoint_predicted_journal',
            'lower': 'lower_ci_predicted_journal',
            'upper': 'upper_ci_predicted_journal'
        }
    }
}


def normalize_text(text):
    """Normalize text for matching - handles newlines, extra spaces, case."""
    if pd.isna(text):
        return ""
    # Replace newlines and multiple spaces with single space
    normalized = str(text).replace('\n', ' ').replace('\r', ' ')
    # Collapse multiple spaces into one
    normalized = ' '.join(normalized.split())
    return normalized.strip().lower()


def assign_evaluator_names(form_df, paper_col, date_col, ident_col):
    """
    Assign evaluator names following Unjournal convention:
    - Use "Identification as an author" if provided
    - Otherwise assign "Evaluator 1", "Evaluator 2", etc. based on date order

    Returns DataFrame with 'evaluator_name' column added
    """
    df = form_df.copy()
    df['evaluator_name'] = None

    # Process each paper separately
    for paper in df[paper_col].unique():
        if pd.isna(paper):
            continue

        paper_evals = df[df[paper_col] == paper].copy()

        # Sort by date
        if date_col in paper_evals.columns:
            paper_evals = paper_evals.sort_values(date_col)

        evaluator_num = 1
        for idx in paper_evals.index:
            ident = paper_evals.loc[idx, ident_col]

            # Use identification if provided and not just whitespace or "No" or "N/A"
            ident_lower = str(ident).strip().lower() if pd.notna(ident) else ''
            if pd.notna(ident) and str(ident).strip() and ident_lower not in ['no', 'n/a']:
                evaluator_name = str(ident).strip()
            else:
                # Assign sequential number
                evaluator_name = f"Evaluator {evaluator_num}"
                evaluator_num += 1

            df.loc[idx, 'evaluator_name'] = evaluator_name

    return df


def extract_value(row, column_name):
    """Extract a numeric value from a row, handling NaN."""
    if column_name not in row.index:
        return None
    val = row[column_name]
    if pd.isna(val):
        return None
    try:
        return float(val)
    except (ValueError, TypeError):
        return None


def main():
    print("=" * 80)
    print("EXTRACTING NEW EVALUATIONS FROM CODA FORM RESPONSES (v2)")
    print("=" * 80)

    # Step 1: Load data from Coda API
    print("\n[1/6] Connecting to Coda and loading data...")

    coda_api_key = os.environ.get("CODA_API_KEY")
    if not coda_api_key:
        print("ERROR: CODA_API_KEY environment variable not set!")
        return None

    coda = Coda(coda_api_key)
    doc = Document("0KBG3dSZCs", coda=coda)

    # Load ratings table
    print("  Loading rsx_evalr_rating table...")
    ratings_table = doc.get_table("grid-pcJr9ZM3wT")
    ratings_df = pd.DataFrame(ratings_table.to_dict())
    print(f"  ✓ Loaded {len(ratings_df)} rows from rsx_evalr_rating")

    # Load academic stream responses
    print("  Loading academic stream responses...")
    academic_table = doc.get_table("grid-aDSyEIerdL")
    academic_df = pd.DataFrame(academic_table.to_dict())
    print(f"  ✓ Loaded {len(academic_df)} academic stream responses")

    # Load applied stream responses
    print("  Loading applied stream responses...")
    applied_table = doc.get_table("grid-znNSTj_xX3")
    applied_df = pd.DataFrame(applied_table.to_dict())
    print(f"  ✓ Loaded {len(applied_df)} applied stream responses")

    # Step 2: Assign evaluator names following Unjournal convention
    print("\n[2/6] Assigning evaluator names...")

    academic_df = assign_evaluator_names(
        academic_df,
        'Name of the paper or project',
        'Date entered (includes transfer from PubPub)',
        'Identification as an author'
    )

    applied_df = assign_evaluator_names(
        applied_df,
        'Title of the paper or project',
        'Date entered (includes transfer from PubPub)',
        'Identification as an author'
    )

    print(f"  ✓ Assigned evaluator names to academic stream")
    print(f"  ✓ Assigned evaluator names to applied stream")

    # Step 3: Normalize paper titles in ratings table for matching
    print("\n[3/6] Normalizing paper titles for matching...")

    ratings_df['paper_normalized'] = ratings_df['research'].apply(normalize_text)
    ratings_df['evaluator_normalized'] = ratings_df['evaluator'].apply(normalize_text)

    # Create set of existing evaluations
    existing_evals = set(zip(ratings_df['paper_normalized'], ratings_df['evaluator_normalized']))
    print(f"  Current evaluations in rsx_evalr_rating: {len(existing_evals)}")

    # Step 4: Find missing evaluations
    print("\n[4/6] Identifying missing evaluations...")

    missing_evals = []

    # Check academic stream
    for _, row in academic_df.iterrows():
        paper = row.get('Name of the paper or project', '')
        evaluator = row.get('evaluator_name', '')

        if pd.isna(paper) or not paper or pd.isna(evaluator) or not evaluator:
            continue

        paper_norm = normalize_text(paper)
        eval_norm = normalize_text(evaluator)

        if (paper_norm, eval_norm) not in existing_evals:
            missing_evals.append({
                'stream': 'academic',
                'paper': paper,
                'evaluator': evaluator,
                'row': row
            })

    # Check applied stream
    for _, row in applied_df.iterrows():
        paper = row.get('Title of the paper or project', '')
        evaluator = row.get('evaluator_name', '')

        if pd.isna(paper) or not paper or pd.isna(evaluator) or not evaluator:
            continue

        paper_norm = normalize_text(paper)
        eval_norm = normalize_text(evaluator)

        if (paper_norm, eval_norm) not in existing_evals:
            missing_evals.append({
                'stream': 'applied',
                'paper': paper,
                'evaluator': evaluator,
                'row': row
            })

    print(f"  ✓ Found {len(missing_evals)} evaluations in forms that are MISSING from rsx_evalr_rating")

    if len(missing_evals) == 0:
        print("\n  No missing evaluations found! All form responses are already in rsx_evalr_rating.")
        return None

    # Step 5: Extract all criteria for missing evaluations
    print("\n[5/6] Extracting rating criteria for missing evaluations...")

    results = []

    for eval_info in missing_evals:
        stream = eval_info['stream']
        paper = eval_info['paper']
        evaluator = eval_info['evaluator']
        row = eval_info['row']

        print(f"\n  Processing: {paper[:60]}... / {evaluator}")
        print(f"    Stream: {stream}")

        criteria_count = 0

        # Extract all 10 criteria
        for criteria_name, col_map in CRITERIA_MAPPING[stream].items():
            middle = extract_value(row, col_map['middle'])
            lower = extract_value(row, col_map['lower'])
            upper = extract_value(row, col_map['upper'])

            # Only include if we have at least the middle rating
            if middle is not None:
                results.append({
                    'research': paper,
                    'evaluator': evaluator,
                    'criteria': criteria_name,
                    'middle_rating': middle,
                    'lower_CI': lower,
                    'upper_CI': upper,
                    'confidence_level': None,
                    'row_created_date': datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
                })
                criteria_count += 1

        print(f"    Total criteria extracted: {criteria_count}")

    print(f"\n  Summary: Extracted {len(results)} rating rows from {len(missing_evals)} evaluations")

    # Step 6: Create output DataFrame and save
    print("\n[6/6] Creating output table and saving...")

    if not results:
        print("  ✗ No data to export!")
        return None

    output_df = pd.DataFrame(results)
    output_df = output_df.sort_values(['research', 'evaluator', 'criteria'])

    output_file = 'data/new_evaluations_from_forms.csv'
    output_df.to_csv(output_file, index=False)

    print(f"  ✓ Saved to: {output_file}")

    # Print summary statistics
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Total rows to import: {len(output_df)}")
    print(f"Total NEW evaluations: {len(missing_evals)}")
    print(f"\nEvaluations by stream:")
    academic_count = sum(1 for e in missing_evals if e['stream'] == 'academic')
    applied_count = sum(1 for e in missing_evals if e['stream'] == 'applied')
    print(f"  Academic stream: {academic_count}")
    print(f"  Applied stream: {applied_count}")

    print(f"\nBy criterion:")
    for criteria in sorted(output_df['criteria'].unique()):
        count = len(output_df[output_df['criteria'] == criteria])
        has_middle = output_df[output_df['criteria'] == criteria]['middle_rating'].notna().sum()
        has_lower = output_df[output_df['criteria'] == criteria]['lower_CI'].notna().sum()
        has_upper = output_df[output_df['criteria'] == criteria]['upper_CI'].notna().sum()
        print(f"  {criteria}: {count} rows (middle:{has_middle}, lower:{has_lower}, upper:{has_upper})")

    print(f"\nUnique papers being added:")
    unique_papers = output_df['research'].unique()
    for i, paper in enumerate(sorted(unique_papers), 1):
        evals_for_paper = output_df[output_df['research'] == paper]['evaluator'].nunique()
        print(f"  {i}. {paper[:70]}... ({evals_for_paper} evaluations)")

    print("\n" + "=" * 80)
    print("NEXT STEPS:")
    print("=" * 80)
    print("1. Review the output file: data/new_evaluations_from_forms.csv")
    print("2. Import this data into Coda's 'rsx_evalr_rating' table")
    print("3. Use Coda's 'Add rows from CSV' feature (these are NEW evaluations)")
    print("4. After import, verify the new row counts match expectations")
    print("=" * 80)

    return output_df


if __name__ == "__main__":
    df = main()
