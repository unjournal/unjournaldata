#!/usr/bin/env python3
"""
Create a paste-ready file with rows in the exact order specified,
with blanks for missing evaluations.
"""

import pandas as pd
import numpy as np

# Exact order of papers as specified by user
TARGET_PAPERS_ORDERED = [
    "A review of GiveWell's discount rate",
    "A systematic review and meta-analysis of the impact of cash transfers on subjective well-being and mental health in low- and middle-income countries",
    "Adjusting for Scale-Use Heterogeneity in Self-Reported Well-Being",
    "Adjusting for Scale-Use Heterogeneity in Self-Reported Well-Being",
    "Deadweight Losses or Gains from In-kind Transfers? Experimental Evidence from India",
    "Does Conservation Work in General Equilibrium?",
    "Does online fundraising increase charitable giving? A nationwide field experiment on Facebook",
    "Does online fundraising increase charitable giving? A nationwide field experiment on Facebook",
    "Ends versus Means: Kantians, Utilitarians, and Moral Decisions",
    "Ends versus Means: Kantians, Utilitarians, and Moral Decisions",
    "Forecasts estimate limited cultured meat production through 2050 (EA forum post)",
    "Forecasts estimate limited cultured meat production through 2050 (EA forum post)",
    "How Effective Is (More) Money? Randomizing Unconditional Cash Transfer Amounts in the US",
    "Irrigation Strengthens Climate Resilience: Long-term Evidence from Mali using Satellites and Surveys",
    "Irrigation Strengthens Climate Resilience: Long-term Evidence from Mali using Satellites and Surveys",
    "Maternal cash transfers for gender equity and child development: Experimental evidence from India",
    "Maternal cash transfers for gender equity and child development: Experimental evidence from India",
    "Mental Health Therapy as a Core Strategy for Increasing Human Capital: Evidence from Ghana",
    "Mental Health Therapy as a Core Strategy for Increasing Human Capital: Evidence from Ghana",
    "Population ethical intuitions.",
    "PUBPUB submission - E2 - The Effect of Public Science on Corporate R&D",
    "The animal welfare cost of meat: evidence from a survey of hypothetical scenarios among Belgian consumers",
    "The wellbeing cost-effectiveness of StrongMinds and Friendship Bench: Combining a systematic review and meta-analysis with charity-related data",
    "When Celebrities Speak: A Nationwide Twitter Experiment Promoting Vaccination In Indonesia",
    "When Celebrities Speak: A Nationwide Twitter Experiment Promoting Vaccination In Indonesia",
    "Yellow Vests, Pessimistic Beliefs, and Carbon Tax Aversion",
]

# Column order as specified
COLUMN_ORDER = [
    'paper_title',
    'evaluator',
    'adv_knowledge_lower_CI',
    'claims_lower_CI',
    'gp_relevance_lower_CI',
    'journal_predict_lower_CI',
    'logic_comms_lower_CI',
    'merits_journal_lower_CI',
    'methods_lower_CI',
    'open_sci_lower_CI',
    'overall_lower_CI',
    'real_world_lower_CI',
    'adv_knowledge_middle_rating',
    'claims_middle_rating',
    'gp_relevance_middle_rating',
    'journal_predict_middle_rating',
    'logic_comms_middle_rating',
    'merits_journal_middle_rating',
    'methods_middle_rating',
    'open_sci_middle_rating',
    'overall_middle_rating',
    'real_world_middle_rating',
    'adv_knowledge_upper_CI',
    'claims_upper_CI',
    'gp_relevance_upper_CI',
    'journal_predict_upper_CI',
    'logic_comms_upper_CI',
    'merits_journal_upper_CI',
    'methods_upper_CI',
    'open_sci_upper_CI',
    'overall_upper_CI',
    'real_world_upper_CI'
]

# Load the data we found
found_df = pd.read_csv('data/specific_missing_ratings_found.csv')

def normalize_title(title):
    """Normalize title for fuzzy matching."""
    if pd.isna(title):
        return ""
    # Remove trailing periods, extra spaces, normalize case
    return str(title).strip().rstrip('.').lower()

def find_matching_row(target_title, found_df, used_indices):
    """Find matching row in found_df, excluding already used rows."""
    target_norm = normalize_title(target_title)

    # Try exact match first
    for idx, row in found_df.iterrows():
        if idx in used_indices:
            continue
        found_title = normalize_title(row['paper_title'])
        if target_norm == found_title:
            return idx, row

    # Try fuzzy match (contains or is contained)
    for idx, row in found_df.iterrows():
        if idx in used_indices:
            continue
        found_title = normalize_title(row['paper_title'])
        if target_norm in found_title or found_title in target_norm:
            return idx, row

    # Try keyword match (significant words)
    target_words = [w for w in target_norm.split() if len(w) > 4][:6]
    for idx, row in found_df.iterrows():
        if idx in used_indices:
            continue
        found_title = normalize_title(row['paper_title'])
        matches = sum(1 for word in target_words if word in found_title)
        if matches >= 3:  # At least 3 significant words match
            return idx, row

    return None, None

# Create ordered output
output_rows = []
used_indices = set()

print("Matching papers in specified order...")
print("="*80)

for i, target_paper in enumerate(TARGET_PAPERS_ORDERED, 1):
    idx, match = find_matching_row(target_paper, found_df, used_indices)

    if match is not None:
        # Found a match - use its data
        row_data = {
            'paper_title': target_paper,  # Use the target title
            'evaluator': match['evaluator']
        }
        # Copy all rating columns
        for col in COLUMN_ORDER[2:]:  # Skip paper_title and evaluator
            row_data[col] = match.get(col, np.nan)

        output_rows.append(row_data)
        used_indices.add(idx)
        print(f"{i:2d}. ✓ {target_paper[:60]:<60} | {str(match['evaluator'])[:15]}")
    else:
        # No match found - create blank row
        row_data = {
            'paper_title': target_paper,
            'evaluator': ''
        }
        # All rating columns blank
        for col in COLUMN_ORDER[2:]:
            row_data[col] = np.nan

        output_rows.append(row_data)
        print(f"{i:2d}. ✗ {target_paper[:60]:<60} | [NO DATA]")

# Create DataFrame with exact column order
output_df = pd.DataFrame(output_rows)
output_df = output_df[COLUMN_ORDER]

# Save to file
output_file = 'data/ratings_for_paste_ordered.csv'
output_df.to_csv(output_file, index=False)

print("\n" + "="*80)
print(f"Created: {output_file}")
print(f"Total rows: {len(output_df)}")
print(f"Rows with data: {sum(1 for idx, row in output_df.iterrows() if row['evaluator'] != '')}")
print(f"Blank rows: {sum(1 for idx, row in output_df.iterrows() if row['evaluator'] == '')}")
print("="*80)
