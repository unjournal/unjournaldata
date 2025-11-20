#!/usr/bin/env python3
"""
Integrate ratings from academic/applied stream form responses into evaluator_paper_level.csv

This script:
1. Loads the existing evaluator_paper_level.csv (wide format)
2. Loads academic and applied stream form responses
3. Transforms form responses into wide format
4. Updates missing values in evaluator_paper_level
5. Creates an updated file for Coda import
"""

import pandas as pd
import numpy as np

# Mapping from criteria names to column prefixes in evaluator_paper_level
CRITERIA_PREFIXES = {
    'overall': 'overall',
    'adv_knowledge': 'adv_knowledge',
    'claims': 'claims',
    'methods': 'methods',
    'logic_comms': 'logic_comms',
    'open_sci': 'open_sci',
    'real_world': 'real_world',
    'gp_relevance': 'gp_relevance',
    'merits_journal': 'merits_journal',
    'journal_predict': 'journal_predict'
}

# Mapping from form response columns to criteria
# Academic stream
ACADEMIC_MAPPING = {
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
}

# Applied stream (some columns differ)
APPLIED_MAPPING = {
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


def normalize_text(text):
    """Normalize text for matching."""
    if pd.isna(text):
        return ""
    return str(text).strip().lower()


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


def transform_form_response_to_wide(form_row, mapping, paper_col, evaluator_col):
    """Transform a single form response row into wide format."""

    result = {
        'paper_title': form_row.get(paper_col, ''),
        'evaluator': form_row.get(evaluator_col, '')
    }

    # Extract all criteria values
    for criteria, col_mapping in mapping.items():
        prefix = CRITERIA_PREFIXES[criteria]

        result[f'{prefix}_middle_rating'] = extract_value(form_row, col_mapping['middle'])
        result[f'{prefix}_lower_CI'] = extract_value(form_row, col_mapping['lower'])
        result[f'{prefix}_upper_CI'] = extract_value(form_row, col_mapping['upper'])

    return result


def main():
    print("="*80)
    print("INTEGRATING FORM RESPONSES INTO EVALUATOR_PAPER_LEVEL (WIDE FORMAT)")
    print("="*80)

    # Step 1: Load data
    print("\n[1/6] Loading data...")
    evaluator_paper_df = pd.read_csv('data/evaluator_paper_level.csv')
    academic_df = pd.read_csv('data/academic_stream_responses.csv')
    applied_df = pd.read_csv('data/applied_stream_responses.csv')

    print(f"  - evaluator_paper_level: {len(evaluator_paper_df)} rows, {len(evaluator_paper_df.columns)} columns")
    print(f"  - academic_stream_responses: {len(academic_df)} rows")
    print(f"  - applied_stream_responses: {len(applied_df)} rows")

    # Step 2: Transform form responses to wide format
    print("\n[2/6] Transforming form responses to wide format...")

    wide_rows = []

    # Process academic stream
    for idx, row in academic_df.iterrows():
        wide_row = transform_form_response_to_wide(
            row,
            ACADEMIC_MAPPING,
            'Name of the paper or project',
            'Code'
        )
        wide_row['evaluation_stream'] = 'academic'
        wide_rows.append(wide_row)

    # Process applied stream
    for idx, row in applied_df.iterrows():
        wide_row = transform_form_response_to_wide(
            row,
            APPLIED_MAPPING,
            'Title of the paper or project',
            'Code'
        )
        wide_row['evaluation_stream'] = 'applied'
        wide_rows.append(wide_row)

    form_wide_df = pd.DataFrame(wide_rows)
    print(f"  - Transformed {len(form_wide_df)} form responses to wide format")

    # Step 3: Identify missing values in evaluator_paper_level
    print("\n[3/6] Identifying missing values in evaluator_paper_level...")

    rating_columns = [col for col in evaluator_paper_df.columns
                     if '_lower_CI' in col or '_middle_rating' in col or '_upper_CI' in col]

    missing_count = evaluator_paper_df[rating_columns].isna().sum().sum()
    total_cells = len(evaluator_paper_df) * len(rating_columns)

    print(f"  - Rating columns: {len(rating_columns)}")
    print(f"  - Missing values: {missing_count} out of {total_cells} ({100*missing_count/total_cells:.1f}%)")

    # Step 4: Match and update
    print("\n[4/6] Matching form responses to evaluator_paper_level...")

    updated_count = 0
    matched_count = 0

    # Create a copy for updates
    updated_df = evaluator_paper_df.copy()

    for idx, eval_row in updated_df.iterrows():
        eval_paper = normalize_text(eval_row['paper_title'])
        eval_evaluator = normalize_text(eval_row['evaluator'])

        # Try to find matching form response
        matched_form = None

        for _, form_row in form_wide_df.iterrows():
            form_paper = normalize_text(form_row['paper_title'])
            form_evaluator = normalize_text(form_row['evaluator'])

            # Check if they match
            if (eval_paper in form_paper or form_paper in eval_paper) and \
               (eval_evaluator in form_evaluator or form_evaluator in eval_evaluator):
                matched_form = form_row
                matched_count += 1
                break

        if matched_form is None:
            continue

        # Update missing values
        row_updates = 0
        for criteria in CRITERIA_PREFIXES.values():
            for suffix in ['_middle_rating', '_lower_CI', '_upper_CI']:
                col = f'{criteria}{suffix}'
                if col in updated_df.columns and col in matched_form.index:
                    # Only update if current value is missing and form has a value
                    if pd.isna(eval_row[col]) and pd.notna(matched_form[col]):
                        updated_df.at[idx, col] = matched_form[col]
                        updated_count += 1
                        row_updates += 1

        if row_updates > 0:
            print(f"  ✓ Updated {row_updates} values for: {eval_row['paper_title'][:50]}... / {eval_row['evaluator']}")

    print(f"\n  Summary:")
    print(f"    - Matched evaluations: {matched_count}")
    print(f"    - Total values updated: {updated_count}")

    # Step 5: Create output
    print("\n[5/6] Creating output file...")

    output_file = 'data/evaluator_paper_level_updated.csv'
    updated_df.to_csv(output_file, index=False)

    print(f"  ✓ Saved to: {output_file}")

    # Step 6: Summary statistics
    print("\n[6/6] Summary statistics...")

    # Count missing values before and after
    missing_before = evaluator_paper_df[rating_columns].isna().sum().sum()
    missing_after = updated_df[rating_columns].isna().sum().sum()

    print(f"\n  Missing values:")
    print(f"    - Before: {missing_before}")
    print(f"    - After:  {missing_after}")
    print(f"    - Filled: {missing_before - missing_after}")
    print(f"    - Reduction: {100*(missing_before - missing_after)/missing_before:.1f}%")

    # Show which criteria were updated most
    print(f"\n  Values updated by criterion:")
    for criteria in CRITERIA_PREFIXES.values():
        middle_col = f'{criteria}_middle_rating'
        lower_col = f'{criteria}_lower_CI'
        upper_col = f'{criteria}_upper_CI'

        middle_filled = 0
        lower_filled = 0
        upper_filled = 0

        if middle_col in evaluator_paper_df.columns:
            middle_filled = (evaluator_paper_df[middle_col].isna() & updated_df[middle_col].notna()).sum()
        if lower_col in evaluator_paper_df.columns:
            lower_filled = (evaluator_paper_df[lower_col].isna() & updated_df[lower_col].notna()).sum()
        if upper_col in evaluator_paper_df.columns:
            upper_filled = (evaluator_paper_df[upper_col].isna() & updated_df[upper_col].notna()).sum()

        total = middle_filled + lower_filled + upper_filled
        if total > 0:
            print(f"    - {criteria}: {total} values (middle:{middle_filled}, lower:{lower_filled}, upper:{upper_filled})")

    print("\n" + "="*80)
    print("NEXT STEPS:")
    print("="*80)
    print("1. Review the updated file: data/evaluator_paper_level_updated.csv")
    print("2. Compare with original to verify updates")
    print("3. Import into Coda's evaluator_paper_level table")
    print("4. Match on: paper_title + evaluator")
    print("5. Update all rating columns")
    print("="*80)

    return updated_df


if __name__ == "__main__":
    df = main()
