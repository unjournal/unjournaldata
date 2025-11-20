#!/usr/bin/env python3
"""
Extract missing ratings AND CI values from Coda evaluation form responses.

This script:
1. Identifies evaluations with missing rating/CI values in rsx_evalr_rating table
2. Looks up those evaluations in academic/applied stream response tables
3. Extracts ALL missing values (middle_rating, lower_CI, upper_CI)
4. Creates a CSV that can be imported into Coda to fill gaps
"""

import pandas as pd
import numpy as np

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
    """Normalize text for matching."""
    if pd.isna(text):
        return ""
    return str(text).strip().lower()


def find_matching_evaluation(paper_title, evaluator_code, academic_df, applied_df):
    """
    Find a matching evaluation in academic or applied stream responses.

    Returns: (stream_type, row_data) or (None, None) if not found
    """
    paper_norm = normalize_text(paper_title)
    eval_norm = normalize_text(evaluator_code)

    # Try academic stream
    for idx, row in academic_df.iterrows():
        row_paper = normalize_text(row.get('Name of the paper or project', ''))
        row_eval = normalize_text(row.get('Code', ''))

        if paper_norm in row_paper or row_paper in paper_norm:
            if eval_norm in row_eval or row_eval in eval_norm:
                return ('academic', row)

    # Try applied stream
    for idx, row in applied_df.iterrows():
        row_paper = normalize_text(row.get('Title of the paper or project', ''))
        row_eval = normalize_text(row.get('Code', ''))

        if paper_norm in row_paper or row_paper in paper_norm:
            if eval_norm in row_eval or row_eval in eval_norm:
                return ('applied', row)

    return (None, None)


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
    print("="*80)
    print("EXTRACTING MISSING RATINGS AND CI VALUES FROM CODA FORM RESPONSES")
    print("="*80)

    # Step 1: Load data
    print("\n[1/5] Loading data...")
    ratings_df = pd.read_csv('data/rsx_evalr_rating.csv')
    academic_df = pd.read_csv('data/academic_stream_responses.csv')
    applied_df = pd.read_csv('data/applied_stream_responses.csv')

    print(f"  - Current ratings table: {len(ratings_df)} rows")
    print(f"  - Academic stream responses: {len(academic_df)} rows")
    print(f"  - Applied stream responses: {len(applied_df)} rows")

    # Step 2: Identify missing values
    print("\n[2/5] Identifying missing rating and CI values...")

    # Missing any value (middle_rating OR lower_CI OR upper_CI)
    missing_any = ratings_df[
        (ratings_df['middle_rating'].isna()) |
        (ratings_df['lower_CI'].isna()) |
        (ratings_df['upper_CI'].isna())
    ].copy()

    print(f"  - Found {len(missing_any)} ratings with missing values")
    print(f"    • Missing middle_rating: {missing_any['middle_rating'].isna().sum()}")
    print(f"    • Missing lower_CI: {missing_any['lower_CI'].isna().sum()}")
    print(f"    • Missing upper_CI: {missing_any['upper_CI'].isna().sum()}")
    print(f"  - Across {missing_any['research'].nunique()} papers")
    print(f"  - Across {missing_any.groupby(['research', 'evaluator']).ngroups} evaluations")

    # Step 3: Extract missing values
    print("\n[3/5] Extracting missing values from form responses...")

    results = []
    found_count = 0
    not_found_count = 0

    # Process each unique evaluation (paper + evaluator combination)
    for (paper, evaluator), group in missing_any.groupby(['research', 'evaluator']):
        print(f"\n  Processing: {paper[:50]}... / {evaluator}")

        # Find matching evaluation in form responses
        stream_type, eval_row = find_matching_evaluation(paper, evaluator, academic_df, applied_df)

        if stream_type is None:
            print(f"    ✗ Not found in form responses")
            not_found_count += 1
            continue

        print(f"    ✓ Found in {stream_type} stream")
        found_count += 1

        # Extract values for each criterion in the group
        for idx, row in group.iterrows():
            criteria = row['criteria']

            # Get column mapping for this stream and criteria
            if criteria not in CRITERIA_MAPPING[stream_type]:
                print(f"      - {criteria}: No mapping available")
                continue

            col_map = CRITERIA_MAPPING[stream_type][criteria]

            # Extract ALL values from form response
            middle = extract_value(eval_row, col_map['middle'])
            lower = extract_value(eval_row, col_map['lower'])
            upper = extract_value(eval_row, col_map['upper'])

            # Only add if we found at least one value
            if middle is not None or lower is not None or upper is not None:
                results.append({
                    'research': paper,
                    'evaluator': evaluator,
                    'criteria': criteria,
                    'middle_rating': middle,
                    'lower_CI': lower,
                    'upper_CI': upper
                })

                # Show what we found
                middle_str = f"{middle}" if middle is not None else "N/A"
                lower_str = f"{lower}" if lower is not None else "N/A"
                upper_str = f"{upper}" if upper is not None else "N/A"
                print(f"      ✓ {criteria}: {middle_str} ({lower_str}-{upper_str})")
            else:
                print(f"      - {criteria}: No values found in form")

    print(f"\n  Summary:")
    print(f"    - Evaluations found: {found_count}")
    print(f"    - Evaluations not found: {not_found_count}")
    print(f"    - Total criteria values extracted: {len(results)}")

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

    output_file = 'data/missing_ratings_from_forms.csv'
    output_df.to_csv(output_file, index=False)

    print(f"  ✓ Saved to: {output_file}")

    # Print summary statistics
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    print(f"Total rows to import: {len(output_df)}")
    print(f"\nBy criterion:")
    for criteria in sorted(output_df['criteria'].unique()):
        count = len(output_df[output_df['criteria'] == criteria])
        has_middle = output_df[output_df['criteria'] == criteria]['middle_rating'].notna().sum()
        has_lower = output_df[output_df['criteria'] == criteria]['lower_CI'].notna().sum()
        has_upper = output_df[output_df['criteria'] == criteria]['upper_CI'].notna().sum()
        print(f"  {criteria}: {count} rows (middle:{has_middle}, lower:{has_lower}, upper:{has_upper})")

    print(f"\nColumns in output file:")
    for col in output_df.columns:
        non_null = output_df[col].notna().sum()
        print(f"  {col}: {non_null} non-null values")

    print("\n" + "="*80)
    print("NEXT STEPS:")
    print("="*80)
    print("1. Review the output file: data/missing_ratings_from_forms.csv")
    print("2. Import this data into Coda's 'rsx_evalr_rating' table")
    print("3. Match on: research + evaluator + criteria")
    print("4. Update: middle_rating, lower_CI, upper_CI")
    print("="*80)

    return output_df


if __name__ == "__main__":
    df = main()
