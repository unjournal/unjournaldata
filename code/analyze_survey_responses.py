#!/usr/bin/env python3
# analyze_survey_responses.py
# Analyze evaluator survey responses for blog post

import pandas as pd
import numpy as np
import re

# Load the survey data
df = pd.read_csv("data/evaluator_survey_responses.csv")

print("=" * 80)
print("EVALUATOR SURVEY RESPONSES - SUMMARY STATISTICS")
print("=" * 80)
print(f"\nTotal responses: {len(df)}")
print(f"Non-empty responses (with some data): {df.dropna(how='all').shape[0]}")

# ==============================================================================
# TIME SPENT ON EVALUATIONS
# ==============================================================================
print("\n" + "=" * 80)
print("TIME SPENT ON EVALUATIONS")
print("=" * 80)

time_col = 'Approximately how long did you spend completing this evaluation?'
time_responses = df[time_col].dropna()
print(f"\nResponses to 'How long did you spend?': {len(time_responses)}")
print("\nExamples of responses:")
for i, response in enumerate(time_responses.head(10), 1):
    print(f"  {i}. {response}")

# Analyze manually imputed hours
hours_col = 'hours_spent_manual_impute'
hours_data = df[hours_col].dropna()
if len(hours_data) > 0:
    print(f"\n\nManually imputed hours (numeric):")
    print(f"  Count: {len(hours_data)}")
    print(f"  Mean: {hours_data.mean():.1f} hours")
    print(f"  Median: {hours_data.median():.1f} hours")
    print(f"  Min: {hours_data.min():.1f} hours")
    print(f"  Max: {hours_data.max():.1f} hours")
    print(f"  Std Dev: {hours_data.std():.1f} hours")

# ==============================================================================
# EVALUATOR EXPERIENCE
# ==============================================================================
print("\n" + "=" * 80)
print("EVALUATOR EXPERIENCE")
print("=" * 80)

field_exp_col = 'How long have you been in this field?'
field_exp = df[field_exp_col].dropna()
print(f"\nResponses to 'How long in field?': {len(field_exp)}")
print("\nExamples:")
for i, response in enumerate(field_exp.head(10), 1):
    print(f"  {i}. {response}")

review_exp_col = 'How many proposals, papers, and projects have you evaluated/reviewed (for journals, grants, or other peer-review)?'
review_exp = df[review_exp_col].dropna()
print(f"\n\nResponses to 'How many papers reviewed?': {len(review_exp)}")
print("\nExamples:")
for i, response in enumerate(review_exp.head(10), 1):
    print(f"  {i}. {response}")

# ==============================================================================
# FEEDBACK ON PROCESS
# ==============================================================================
print("\n" + "=" * 80)
print("FEEDBACK ON THE UNJOURNAL PROCESS")
print("=" * 80)

process_rating_col = 'How would you rate this template and process?'
process_ratings = df[process_rating_col].dropna()
print(f"\nResponses to 'Rate this template/process': {len(process_ratings)}")
print("\nAll responses:")
for i, response in enumerate(process_ratings, 1):
    if pd.notna(response) and response.strip():
        print(f"\n  [{i}] {response}")

# ==============================================================================
# WILLINGNESS TO RE-EVALUATE
# ==============================================================================
print("\n" + "=" * 80)
print("WILLINGNESS TO RE-EVALUATE")
print("=" * 80)

reevaluate_col = 'Would you be willing to consider evaluating a revised version of this work?'
reevaluate = df[reevaluate_col].dropna()
print(f"\nResponses to 'Willing to re-evaluate?': {len(reevaluate)}")

# Count yes/no responses
yes_count = reevaluate.str.lower().str.contains('yes', na=False).sum()
no_count = reevaluate.str.lower().str.contains('no', na=False).sum()
print(f"  Contains 'Yes': {yes_count}")
print(f"  Contains 'No': {no_count}")

print("\nSample responses:")
for i, response in enumerate(reevaluate.head(10), 1):
    if pd.notna(response) and response.strip():
        print(f"  {i}. {response}")

# ==============================================================================
# ADDITIONAL SUGGESTIONS
# ==============================================================================
print("\n" + "=" * 80)
print("SUGGESTIONS & QUESTIONS")
print("=" * 80)

suggestions_col = 'Do you have any other suggestions or questions about this process or The Unjournal? (We will try to respond, and incorporate your suggestions.)'
suggestions = df[suggestions_col].dropna()
suggestions = suggestions[suggestions.str.strip() != '']
print(f"\nNon-empty responses: {len(suggestions)}")
print("\nAll suggestions:")
for i, response in enumerate(suggestions, 1):
    if pd.notna(response) and response.strip():
        print(f"\n  [{i}] {response}")

# ==============================================================================
# FIELD/EXPERTISE
# ==============================================================================
print("\n" + "=" * 80)
print("FIELDS OF EXPERTISE")
print("=" * 80)

expertise_col = 'Field/expertise'
expertise = df[expertise_col].dropna()
expertise = expertise[expertise.str.strip() != '']
print(f"\nNon-empty responses: {len(expertise)}")
print("\nFields represented:")
for i, field in enumerate(expertise.head(20), 1):
    if pd.notna(field) and field.strip():
        print(f"  {i}. {field}")

print("\n" + "=" * 80)
print("END OF ANALYSIS")
print("=" * 80)
