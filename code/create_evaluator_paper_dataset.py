#!/usr/bin/env python3
"""
Create comprehensive evaluator-paper level dataset.

This script creates a dataset at the evaluator-paper level, combining:
1. Survey responses from Coda (academic + applied streams)
2. Quantitative ratings from Coda (pivoted from long to wide format)
3. Additional survey data scraped from PubPub
4. Paper metadata

Output: data/evaluator_paper_level.csv

Privacy protections - EXCLUDES:
- Confidential comments
- COI information
- Evaluator personal contact information
- Evaluator pseudonyms (private codes)
- Process feedback questions
- Re-evaluation willingness

Uses PUBLIC evaluator identifiers only:
- Names from ratings table (if evaluator chose to use their name)
- Generic "Evaluator 1", "Evaluator 2", etc. for anonymous evaluations
"""

from codaio import Coda, Document
import pandas as pd
import os
import numpy as np

def main():
    print("=" * 80)
    print("Creating Evaluator-Paper Level Dataset")
    print("=" * 80)

    # Initialize Coda
    from dotenv import load_dotenv
    if os.path.isfile(".Renviron"):
        load_dotenv(dotenv_path=".Renviron")

    coda_api_key = os.environ["CODA_API_KEY"]
    coda = Coda(coda_api_key)
    doc = Document("0KBG3dSZCs", coda=coda)

    # ========================================
    # 1. LOAD SURVEY RESPONSES (with evaluator codes)
    # ========================================
    print("\n1. Loading survey responses from Coda...")

    # Academic stream
    academic_survey = doc.get_table("grid-aDSyEIerdL")
    academic_df = pd.DataFrame(academic_survey.to_dict())

    # Applied stream
    applied_survey = doc.get_table("grid-znNSTj_xX3")
    applied_df = pd.DataFrame(applied_survey.to_dict())

    # Standardize column names
    academic_df = academic_df.rename(columns={'Name of the paper or project': 'paper_title'})
    applied_df = applied_df.rename(columns={'Title of the paper or project': 'paper_title'})

    # Add stream identifier
    academic_df['evaluation_stream'] = 'academic'
    applied_df['evaluation_stream'] = 'applied'

    # Combine
    survey_df = pd.concat([academic_df, applied_df], ignore_index=True)

    # Select PUBLIC columns (NO PSEUDONYMS - those are confidential)
    survey_columns = [
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

    # Filter to available columns
    available_survey_cols = [col for col in survey_columns if col in survey_df.columns]
    survey_df = survey_df[available_survey_cols].copy()

    # Add temporary index for assigning evaluator numbers per paper
    survey_df['_temp_idx'] = survey_df.groupby('paper_title').cumcount() + 1
    survey_df['evaluator'] = 'Evaluator ' + survey_df['_temp_idx'].astype(str)
    survey_df = survey_df.drop('_temp_idx', axis=1)

    print(f"   Loaded {len(survey_df)} survey responses")
    print(f"   Unique evaluators: {survey_df['evaluator'].nunique()}")
    print(f"   Unique papers: {survey_df['paper_title'].nunique()}")

    # ========================================
    # 2. LOAD RATINGS (pivot to wide format)
    # ========================================
    print("\n2. Loading and pivoting ratings data...")

    ratings = doc.get_table("grid-pcJr9ZM3wT")
    ratings_df = pd.DataFrame(ratings.to_dict())

    # Select relevant columns
    ratings_cols = ['research', 'evaluator', 'criteria', 'middle_rating',
                    'lower_CI', 'upper_CI', 'confidence_level']
    ratings_df = ratings_df[ratings_cols]

    print(f"   Loaded {len(ratings_df)} rating records")

    # Pivot ratings from long to wide format
    # Each criteria becomes a column with _rating, _lower, _upper suffixes
    rating_wide = ratings_df.pivot_table(
        index=['research', 'evaluator'],
        columns='criteria',
        values=['middle_rating', 'lower_CI', 'upper_CI', 'confidence_level'],
        aggfunc='first'  # Take first value if duplicates
    )

    # Flatten column names
    rating_wide.columns = [f'{criteria}_{metric}'
                          for metric, criteria in rating_wide.columns]
    rating_wide = rating_wide.reset_index()

    # Rename research to paper_title for merging
    rating_wide = rating_wide.rename(columns={'research': 'paper_title'})

    print(f"   Pivoted to {len(rating_wide)} evaluator-paper combinations")
    print(f"   Rating columns created: {len([c for c in rating_wide.columns if '_middle_rating' in c])}")

    # ========================================
    # 3. MERGE SURVEY + RATINGS
    # ========================================
    print("\n3. Merging survey responses with ratings...")

    # The ratings table has the public evaluator names
    # Survey responses will get generic "Evaluator 1, 2, 3" names
    # We merge on paper_title only, then try to match evaluators

    # For ratings-only rows: use the evaluator name from ratings (already public)
    # For survey-only rows: keep the assigned "Evaluator N" name
    # For matches: prefer the ratings evaluator name if it exists

    combined_df = pd.merge(
        survey_df,
        rating_wide,
        on='paper_title',
        how='outer',
        suffixes=('_survey', '_rating')
    )

    # Use rating evaluator name if available, otherwise survey evaluator name
    combined_df['evaluator'] = combined_df['evaluator_rating'].fillna(combined_df['evaluator_survey'])
    combined_df = combined_df.drop(['evaluator_survey', 'evaluator_rating'], axis=1, errors='ignore')

    print(f"   Combined dataset: {len(combined_df)} rows")
    print(f"   Unique evaluators: {combined_df['evaluator'].nunique()}")
    print(f"   Unique papers: {combined_df['paper_title'].nunique()}")

    # ========================================
    # 4. ADD PUBPUB SCRAPED DATA
    # ========================================
    print("\n4. Adding PubPub scraped survey data...")

    try:
        pubpub_df = pd.read_csv("data/pubpub_survey_CLEANED_for_coda_import.csv")

        # PubPub data doesn't have evaluator codes, so match by paper title
        # and fill in missing survey values where possible
        pubpub_cols_to_add = [
            'How long have you been in this field?',
            'How many proposals, papers, and projects have you evaluated/reviewed?',
            'Field/expertise'
        ]

        # Rename PubPub columns to match
        pubpub_rename = {
            'Name of the paper or project': 'paper_title',
            'How many proposals, papers, and projects have you evaluated/reviewed?':
                'How many proposals, papers, and projects have you evaluated/reviewed (for journals, grants, or other peer-review)?'
        }
        pubpub_df = pubpub_df.rename(columns=pubpub_rename)

        # For now, just note availability
        print(f"   PubPub data: {len(pubpub_df)} evaluations with survey responses")
        print(f"   Note: PubPub data doesn't have evaluator identifiers for direct merge")

    except FileNotFoundError:
        print("   No PubPub scraped data found (optional)")

    # ========================================
    # 5. ADD PAPER METADATA
    # ========================================
    print("\n5. Adding paper metadata...")

    research = doc.get_table("grid-Iru9Fra3tE")
    research_df = pd.DataFrame(research.to_dict())

    # Select useful paper-level fields
    paper_cols = [
        'label_paper_title',
        'status',
        'research_url',
        'doi',
        'main_cause_cat',
        'cause_description'
    ]

    available_paper_cols = [col for col in paper_cols if col in research_df.columns]
    research_df = research_df[available_paper_cols]
    research_df = research_df.rename(columns={'label_paper_title': 'paper_title'})

    # Merge paper metadata
    final_df = pd.merge(
        combined_df,
        research_df,
        on='paper_title',
        how='left'
    )

    print(f"   Final dataset: {len(final_df)} evaluator-paper rows")

    # ========================================
    # 6. CLEAN AND ORGANIZE COLUMNS
    # ========================================
    print("\n6. Organizing and removing sensitive columns...")

    # REMOVE SENSITIVE FEEDBACK COLUMNS (per user request)
    sensitive_columns = [
        'How would you rate this template and process?',
        'Would you be willing to consider evaluating a revised version of this work?',
        'Do you have any other suggestions or questions about this process or The Unjournal? (We will try to respond, and incorporate your suggestions.)',
        'status_y'  # Duplicate status column
    ]

    for col in sensitive_columns:
        if col in final_df.columns:
            final_df = final_df.drop(col, axis=1)
            print(f"   Removed: {col}")

    # Order columns logically: identifiers, then survey, then ratings, then metadata
    identifier_cols = ['evaluator', 'paper_title', 'evaluation_stream']

    survey_question_cols = [col for col in final_df.columns
                           if any(q in col for q in ['How long', 'How many', 'Field/expertise', 'Approximately how long'])]

    rating_cols = [col for col in final_df.columns
                  if any(x in col for x in ['_middle_rating', '_lower_CI', '_upper_CI', '_confidence_level'])]

    metadata_cols = [col for col in final_df.columns
                    if col not in identifier_cols + survey_question_cols + rating_cols]

    # Reorder
    column_order = identifier_cols + survey_question_cols + rating_cols + metadata_cols
    final_df = final_df[[col for col in column_order if col in final_df.columns]]

    # ========================================
    # 7. SAVE OUTPUT
    # ========================================
    output_file = "data/evaluator_paper_level.csv"
    final_df.to_csv(output_file, index=False)

    print(f"\n{'='*80}")
    print(f"✓ Saved to: {output_file}")
    print(f"  Total rows: {len(final_df)}")
    print(f"  Total columns: {len(final_df.columns)}")
    print(f"  Unique evaluators: {final_df['evaluator'].nunique()}")
    print(f"  Unique papers: {final_df['paper_title'].nunique()}")
    print(f"{'='*80}")

    # Summary statistics
    print("\n=== COLUMN COVERAGE ===")
    for col in survey_question_cols[:10]:  # Show first 10
        non_null = final_df[col].notna().sum()
        pct = 100 * non_null / len(final_df)
        print(f"  {col[:60]}: {non_null} ({pct:.1f}%)")

    return final_df

if __name__ == "__main__":
    df = main()
