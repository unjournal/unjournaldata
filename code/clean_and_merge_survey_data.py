#!/usr/bin/env python3
"""
Clean scraped PubPub data and create import file for Coda.

This script:
1. Cleans the scraped survey data
2. Compares with existing Coda data
3. Produces a clean CSV for importing missing data into Coda
"""

import pandas as pd
import re

def clean_field(text, field_type='general'):
    """Clean HTML and extra text from scraped fields."""
    if pd.isna(text) or not text:
        return ""

    # Remove common HTML/navigation junk
    junk_patterns = [
        r'Skip to main content.*?Login/signup',
        r'The Unjournal.*?(?:Publi|Prize|Search|Login)',
        r'Summary and Metrics:.*?"',
        r'Connections\d+ of \d+children and siblings.*',
        r'filter.*?Supplement to',
        r'References\[.*?\]',
        r'How many proposals.*?\?',
        r'How long.*?\?',
        r'of expertise\?',
        r'years?How many',
        r'\(for journals.*?\)',
        r'\.How many proposals.*',
        r'\.How long.*',
        r'The authors.*',
        r'I have compiled.*',
        r'publications and regulatory.*',
        r'experiment.*(?:shows|to test).*',
        r's, with these gains.*',
        r'less likely to achieve.*',
        r'of public economics.*',
        r'but of great interest.*',
        r'expertiseThe authors.*',
        r'scripts publicly available.*',
        r'would help the reader.*',
        r'where consumer.*',
    ]

    cleaned = text
    for pattern in junk_patterns:
        cleaned = re.sub(pattern, '', cleaned, flags=re.IGNORECASE | re.DOTALL)

    # Field-specific cleaning
    if field_type == 'years':
        # For years in field: extract number + "years" or standalone number
        # Try to find the cleanest answer
        matches = re.findall(r'(\d+[\+\-]?\s*(?:years?)?)', cleaned)
        if matches:
            return matches[0].strip()

        # Try "More than X"
        match = re.search(r'((?:More than|Over|About)\s+\d+)', cleaned, re.IGNORECASE)
        if match:
            return match.group(1).strip()

    elif field_type == 'papers':
        # For papers reviewed: extract number or range
        matches = re.findall(r'(\d+[\+\-]?)', cleaned)
        if matches:
            return matches[0].strip()

    # For other fields, clean up and truncate
    # Remove leading/trailing junk
    cleaned = re.sub(r'^[^a-zA-Z0-9]+', '', cleaned)
    cleaned = re.sub(r'[^a-zA-Z0-9\s\-\+,\.]+$', '', cleaned)
    cleaned = cleaned.strip()

    # If still too long or contains obvious junk, truncate more aggressively
    if len(cleaned) > 150 or 'Summary and Metrics' in cleaned:
        # Try to get first sentence
        first_sentence = re.split(r'[\.!?]\s', cleaned)
        if first_sentence and len(first_sentence[0]) > 0:
            cleaned = first_sentence[0]

    return cleaned[:150].strip()

def main():
    print("Loading scraped PubPub data...")
    pubpub = pd.read_csv("data/pubpub_scraped_survey_data.csv")

    print(f"Found {len(pubpub)} scraped evaluations")

    # Clean the fields
    print("\nCleaning scraped data...")
    pubpub['years_in_field_clean'] = pubpub['years_in_field'].apply(lambda x: clean_field(x, 'years'))
    pubpub['papers_reviewed_clean'] = pubpub['papers_reviewed'].apply(lambda x: clean_field(x, 'papers'))
    pubpub['field_expertise_clean'] = pubpub['field_expertise'].apply(lambda x: clean_field(x, 'general'))
    pubpub['time_spent_clean'] = pubpub['time_spent'].apply(lambda x: clean_field(x, 'general'))
    pubpub['process_rating_clean'] = pubpub['process_rating'].apply(lambda x: clean_field(x, 'general'))

    # Create a clean subset
    clean_data = pubpub[['paper_title', 'years_in_field_clean', 'papers_reviewed_clean',
                         'field_expertise_clean', 'time_spent_clean', 'process_rating_clean', 'eval_url']].copy()

    clean_data = clean_data.rename(columns={
        'years_in_field_clean': 'How long have you been in this field?',
        'papers_reviewed_clean': 'How many proposals, papers, and projects have you evaluated/reviewed?',
        'field_expertise_clean': 'Field/expertise',
        'time_spent_clean': 'Approximately how long did you spend completing this evaluation?',
        'process_rating_clean': 'How would you rate this template and process?',
        'paper_title': 'Name of the paper or project'
    })

    # Load existing Coda data to see what we're missing
    print("\nLoading existing Coda survey data...")
    try:
        coda_data = pd.read_csv("data/evaluator_survey_responses.csv")
        print(f"Existing Coda data: {len(coda_data)} responses")

        # Count non-null values in each column
        print("\nExisting Coda data coverage:")
        for col in ['How long have you been in this field?',
                    'How many proposals, papers, and projects have you evaluated/reviewed (for journals, grants, or other peer-review)?']:
            if col in coda_data.columns:
                non_null = coda_data[col].notna().sum()
                print(f"  {col}: {non_null} non-null")

    except FileNotFoundError:
        print("  (No existing Coda data found)")
        coda_data = None

    # Save cleaned PubPub data
    output_file = "data/pubpub_survey_CLEANED_for_coda_import.csv"
    clean_data.to_csv(output_file, index=False)
    print(f"\n✓ Saved cleaned data to: {output_file}")
    print(f"  {len(clean_data)} evaluations")

    # Show sample
    print("\n=== SAMPLE OF CLEANED DATA ===")
    print(clean_data[['Name of the paper or project',
                      'How long have you been in this field?',
                      'How many proposals, papers, and projects have you evaluated/reviewed?']].head(10).to_string())

    # Create summary
    print("\n=== COVERAGE SUMMARY ===")
    for col in clean_data.columns:
        if col != 'eval_url':
            non_null = clean_data[col].notna().sum()
            non_empty = (clean_data[col] != "").sum() if clean_data[col].dtype == 'object' else non_null
            print(f"{col}: {non_empty} non-empty values")

    return clean_data

if __name__ == "__main__":
    df = main()
