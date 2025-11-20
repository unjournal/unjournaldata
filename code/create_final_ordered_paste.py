#!/usr/bin/env python3
"""
Create final paste-ready file with correct matches.
"""

import pandas as pd
import numpy as np

# Target papers in exact order
TARGET_PAPERS = [
    'A review of GiveWell\'s discount rate',
    'A systematic review and meta-analysis of the impact of cash transfers on subjective well-being and mental health in low- and middle-income countries',
    'Adjusting for Scale-Use Heterogeneity in Self-Reported Well-Being',
    'Adjusting for Scale-Use Heterogeneity in Self-Reported Well-Being',
    'Deadweight Losses or Gains from In-kind Transfers? Experimental Evidence from India',
    'Does Conservation Work in General Equilibrium?',
    'Does online fundraising increase charitable giving? A nationwide field experiment on Facebook',
    'Does online fundraising increase charitable giving? A nationwide field experiment on Facebook',
    'Ends versus Means: Kantians, Utilitarians, and Moral Decisions',
    'Ends versus Means: Kantians, Utilitarians, and Moral Decisions',
    'Forecasts estimate limited cultured meat production through 2050 (EA forum post)',
    'Forecasts estimate limited cultured meat production through 2050 (EA forum post)',
    'How Effective Is (More) Money? Randomizing Unconditional Cash Transfer Amounts in the US',
    'Irrigation Strengthens Climate Resilience: Long-term Evidence from Mali using Satellites and Surveys',
    'Irrigation Strengthens Climate Resilience: Long-term Evidence from Mali using Satellites and Surveys',
    'Maternal cash transfers for gender equity and child development: Experimental evidence from India',
    'Maternal cash transfers for gender equity and child development: Experimental evidence from India',
    'Mental Health Therapy as a Core Strategy for Increasing Human Capital: Evidence from Ghana',
    'Mental Health Therapy as a Core Strategy for Increasing Human Capital: Evidence from Ghana',
    'Population ethical intuitions.',
    'PUBPUB submission - E2 - The Effect of Public Science on Corporate R&D',
    'The animal welfare cost of meat: evidence from a survey of hypothetical scenarios among Belgian consumers',
    'The wellbeing cost-effectiveness of StrongMinds and Friendship Bench: Combining a systematic review and meta-analysis with charity-related data',
    'When Celebrities Speak: A Nationwide Twitter Experiment Promoting Vaccination In Indonesia',
    'When Celebrities Speak: A Nationwide Twitter Experiment Promoting Vaccination In Indonesia',
    'Yellow Vests, Pessimistic Beliefs, and Carbon Tax Aversion',
]

# Column order
COLUMN_ORDER = [
    'paper_title', 'evaluator',
    'adv_knowledge_lower_CI', 'claims_lower_CI', 'gp_relevance_lower_CI', 'journal_predict_lower_CI',
    'logic_comms_lower_CI', 'merits_journal_lower_CI', 'methods_lower_CI', 'open_sci_lower_CI',
    'overall_lower_CI', 'real_world_lower_CI',
    'adv_knowledge_middle_rating', 'claims_middle_rating', 'gp_relevance_middle_rating', 'journal_predict_middle_rating',
    'logic_comms_middle_rating', 'merits_journal_middle_rating', 'methods_middle_rating', 'open_sci_middle_rating',
    'overall_middle_rating', 'real_world_middle_rating',
    'adv_knowledge_upper_CI', 'claims_upper_CI', 'gp_relevance_upper_CI', 'journal_predict_upper_CI',
    'logic_comms_upper_CI', 'merits_journal_upper_CI', 'methods_upper_CI', 'open_sci_upper_CI',
    'overall_upper_CI', 'real_world_upper_CI'
]

# Load found data
found_df = pd.read_csv('data/specific_missing_ratings_found.csv')

# Create blank row template
def blank_row(paper_title):
    row = {'paper_title': paper_title, 'evaluator': ''}
    for col in COLUMN_ORDER[2:]:
        row[col] = np.nan
    return row

# Create mapping of found data by normalized title
found_map = {}
for idx, row in found_df.iterrows():
    title_norm = str(row['paper_title']).lower().strip().rstrip('.')
    evaluator = str(row['evaluator'])
    key = (title_norm, evaluator)
    found_map[key] = row

output_rows = []

# Process each target paper
for i, target_paper in enumerate(TARGET_PAPERS):
    target_norm = target_paper.lower().strip().rstrip('.')

    # Try to find match
    found = False
    for (found_title, found_eval), found_row in found_map.items():
        # Check various matching conditions
        match = False

        # Exact match
        if target_norm == found_title:
            match = True
        # Contains match
        elif target_norm in found_title or found_title in target_norm:
            match = True
        # Remove '(EA forum post)' and try again
        elif target_norm.replace('(ea forum post)', '').strip() in found_title:
            match = True
        elif found_title in target_norm.replace('(ea forum post)', '').strip():
            match = True

        if match:
            # Found a match - create row
            row_data = {
                'paper_title': target_paper,
                'evaluator': found_eval
            }
            for col in COLUMN_ORDER[2:]:
                row_data[col] = found_row.get(col, np.nan)

            output_rows.append(row_data)
            # Remove from map so it won't be reused
            del found_map[(found_title, found_eval)]
            found = True
            break

    if not found:
        # No match - add blank row
        output_rows.append(blank_row(target_paper))

# Create DataFrame
output_df = pd.DataFrame(output_rows)
output_df = output_df[COLUMN_ORDER]

# Save
output_df.to_csv('data/ratings_for_paste_ordered.csv', index=False)

print('Created: data/ratings_for_paste_ordered.csv')
print(f'Total rows: {len(output_df)}')
print(f'\nRows:')
for i, (idx, row) in enumerate(output_df.iterrows(), 1):
    paper = row['paper_title'][:50]
    evaluator = str(row['evaluator'])[:15]
    non_null = row.drop(['paper_title', 'evaluator']).notna().sum()
    status = '✓' if non_null > 0 else '✗'
    print(f'{i:2d}. {status} {paper:<50} | {evaluator:<15} | {non_null}/30')
