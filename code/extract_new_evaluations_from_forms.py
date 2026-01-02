#!/usr/bin/env python3
"""
Extract COMPLETELY NEW evaluations from Coda form responses.

This script finds evaluations that exist in the academic/applied stream form
responses but are COMPLETELY MISSING from the rsx_evalr_rating table (not just
missing some values, but missing entirely).

This complements extract_missing_ratings_from_coda_forms.py which fills in
missing values for existing evaluations.

Usage:
    python3 code/extract_new_evaluations_from_forms.py
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


def fuzzy_match_paper(paper1, paper2):
    """Check if two paper titles match (handling trailing spaces, case differences)."""
    norm1 = normalize_text(paper1)
    norm2 = normalize_text(paper2)

    # Exact match
    if norm1 == norm2:
        return True

    # Partial match (first 40 chars)
    if len(norm1) >= 40 and len(norm2) >= 40:
        return norm1[:40] == norm2[:40]

    return False


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
    print("EXTRACTING NEW EVALUATIONS FROM CODA FORM RESPONSES")
    print("=" * 80)

    # Step 1: Load data from Coda API
    print("\n[1/5] Connecting to Coda and loading data...")

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

    # Step 2: Identify evaluations in forms but missing from ratings table
    print("\n[2/5] Identifying missing evaluations...")

    # Get existing evaluations from ratings table
    existing_evals = set()
    for _, row in ratings_df.iterrows():
        paper = normalize_text(row['research'])
        evaluator = normalize_text(row['evaluator'])
        existing_evals.add((paper, evaluator))

    print(f"  Current evaluations in rsx_evalr_rating: {len(existing_evals)}")

    # Find NEW evaluations in forms
    missing_evals = []

    # Check academic stream
    for _, row in academic_df.iterrows():
        paper = row.get('Name of the paper or project', '')
        evaluator = row.get('Code', '')

        if pd.isna(paper) or pd.isna(evaluator) or str(evaluator).strip() == '':
            continue

        paper_norm = normalize_text(paper)
        eval_norm = normalize_text(evaluator)

        # Check if this evaluation exists in ratings table using fuzzy matching
        found = False
        for existing_paper, existing_eval in existing_evals:
            # Must match both paper AND evaluator
            if eval_norm == existing_eval:
                # Check if papers match (fuzzy)
                if paper_norm == existing_paper or \
                   (len(paper_norm) >= 30 and len(existing_paper) >= 30 and paper_norm[:30] == existing_paper[:30]):
                    found = True
                    break

        if not found:
            missing_evals.append({
                'stream': 'academic',
                'paper': paper,
                'evaluator': evaluator,
                'row': row
            })

    # Check applied stream
    for _, row in applied_df.iterrows():
        paper = row.get('Title of the paper or project', '')
        evaluator = row.get('Code', '')

        if pd.isna(paper) or pd.isna(evaluator) or str(evaluator).strip() == '':
            continue

        paper_norm = normalize_text(paper)
        eval_norm = normalize_text(evaluator)

        # Check if this evaluation exists in ratings table using fuzzy matching
        found = False
        for existing_paper, existing_eval in existing_evals:
            if eval_norm == existing_eval:
                if paper_norm == existing_paper or \
                   (len(paper_norm) >= 30 and len(existing_paper) >= 30 and paper_norm[:30] == existing_paper[:30]):
                    found = True
                    break

        if not found:
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

    # Step 3: Extract all criteria for missing evaluations
    print("\n[3/5] Extracting rating criteria for missing evaluations...")

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
                    'confidence_level': None,  # Not in forms
                    'row_created_date': datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
                })
                criteria_count += 1

                # Show what we found
                middle_str = f"{middle}"
                lower_str = f"{lower}" if lower is not None else "N/A"
                upper_str = f"{upper}" if upper is not None else "N/A"
                print(f"      ✓ {criteria_name}: {middle_str} ({lower_str}-{upper_str})")

        print(f"    Total criteria extracted: {criteria_count}")

    print(f"\n  Summary: Extracted {len(results)} rating rows from {len(missing_evals)} evaluations")

    # Step 4: Create output DataFrame
    print("\n[4/5] Creating output table...")

    if not results:
        print("  ✗ No data to export!")
        return None

    output_df = pd.DataFrame(results)

    # Sort by paper and evaluator
    output_df = output_df.sort_values(['research', 'evaluator', 'criteria'])

    print(f"  ✓ Created table with {len(output_df)} rows")

    # Step 5: Save to CSV
    print("\n[5/5] Saving output...")

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
    print("4. After import, verify:")
    print("   - Overall ratings should increase from 94 to ~105")
    print("   - Total rows should increase by ~110")
    print("   - Unique papers should increase from 49 to ~55")
    print("=" * 80)

    return output_df


if __name__ == "__main__":
    df = main()
