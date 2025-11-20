#!/usr/bin/env python3
"""
Extract ratings for specific missing evaluations from form responses.
"""

import pandas as pd
import numpy as np

# Mapping from criteria to form columns
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


def extract_ratings_wide(form_row, mapping):
    """Extract all ratings from a form row into wide format."""
    result = {}

    for criteria, col_mapping in mapping.items():
        result[f'{criteria}_middle_rating'] = extract_value(form_row, col_mapping['middle'])
        result[f'{criteria}_lower_CI'] = extract_value(form_row, col_mapping['lower'])
        result[f'{criteria}_upper_CI'] = extract_value(form_row, col_mapping['upper'])

    return result


# Target papers (what we're looking for)
TARGET_PAPERS = [
    'A review of GiveWell\'s discount rate',
    'A systematic review and meta-analysis of the impact of cash transfers on subjective well-being and mental health in low- and middle-income countries',
    'Adjusting for Scale-Use Heterogeneity in Self-Reported Well-Being',
    'Deadweight Losses or Gains from In-kind Transfers? Experimental Evidence from India',
    'Does Conservation Work in General Equilibrium?',
    'Does online fundraising increase charitable giving? A nationwide field experiment on Facebook',
    'Ends versus Means: Kantians, Utilitarians, and Moral Decisions',
    'Forecasts estimate limited cultured meat production through 2050',
    'How Effective Is (More) Money? Randomizing Unconditional Cash Transfer Amounts in the US',
    'Irrigation Strengthens Climate Resilience: Long-term Evidence from Mali using Satellites and Surveys',
    'Maternal cash transfers for gender equity and child development: Experimental evidence from India',
    'Mental Health Therapy as a Core Strategy for Increasing Human Capital: Evidence from Ghana',
    'Population ethical intuitions',
    'PUBPUB submission - E2 - The Effect of Public Science on Corporate R&D',
    'The animal welfare cost of meat: evidence from a survey of hypothetical scenarios among Belgian consumers',
    'The wellbeing cost-effectiveness of StrongMinds and Friendship Bench',
    'When Celebrities Speak: A Nationwide Twitter Experiment Promoting Vaccination In Indonesia',
    'Yellow Vests, Pessimistic Beliefs, and Carbon Tax Aversion',
]

# Load data
academic_df = pd.read_csv('data/academic_stream_responses.csv')
applied_df = pd.read_csv('data/applied_stream_responses.csv')

results = []

# Search academic stream
for idx, row in academic_df.iterrows():
    paper = row.get('Name of the paper or project', '')
    evaluator = row.get('Code', '')

    # Check if this matches any of our targets
    for target in TARGET_PAPERS:
        if target.lower() in paper.lower() or paper.lower() in target.lower():
            # Extract ratings
            ratings = extract_ratings_wide(row, ACADEMIC_MAPPING)

            result_row = {
                'paper_title': paper,
                'evaluator': evaluator,
                'evaluation_stream': 'academic'
            }
            result_row.update(ratings)
            results.append(result_row)

            print(f'Found: {paper[:60]}... / {evaluator}')
            break

# Search applied stream
for idx, row in applied_df.iterrows():
    paper = row.get('Title of the paper or project', '')
    evaluator = row.get('Code', '')

    # Check if this matches any of our targets
    for target in TARGET_PAPERS:
        if target.lower() in paper.lower() or paper.lower() in target.lower():
            # Extract ratings
            ratings = extract_ratings_wide(row, APPLIED_MAPPING)

            result_row = {
                'paper_title': paper,
                'evaluator': evaluator,
                'evaluation_stream': 'applied'
            }
            result_row.update(ratings)
            results.append(result_row)

            print(f'Found: {paper[:60]}... / {evaluator}')
            break

# Create DataFrame
output_df = pd.DataFrame(results)

# Reorder columns to match evaluator_paper_level format
col_order = ['paper_title', 'evaluator', 'evaluation_stream']

# Add rating columns in order
criteria = ['adv_knowledge', 'claims', 'gp_relevance', 'journal_predict',
           'logic_comms', 'merits_journal', 'methods', 'open_sci', 'overall', 'real_world']

for criterion in criteria:
    for suffix in ['_lower_CI', '_middle_rating', '_upper_CI']:
        col = f'{criterion}{suffix}'
        if col in output_df.columns:
            col_order.append(col)

# Select and reorder columns
output_df = output_df[[col for col in col_order if col in output_df.columns]]

# Save
output_file = 'data/specific_missing_ratings_found.csv'
output_df.to_csv(output_file, index=False)

print(f'\nTotal found: {len(output_df)}')
print(f'Saved to: {output_file}')
print('\nSummary by paper:')
for paper in output_df['paper_title'].unique():
    count = len(output_df[output_df['paper_title'] == paper])
    print(f'  {paper[:60]}...: {count} evaluations')
