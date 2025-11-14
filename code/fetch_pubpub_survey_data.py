#!/usr/bin/env python3
"""
Fetch evaluator survey responses from PubPub evaluations.

This script queries the PubPub API to extract survey responses that may be
missing from the Coda import, particularly:
- How long have you been in this field?
- How many papers have you reviewed?
- Time spent on evaluation
- Process feedback

Output: CSV file that can be imported into Coda to fill gaps.
"""

import requests
import json
import pandas as pd
from typing import Dict, List, Any
import re

# PubPub GraphQL endpoint
PUBPUB_API = "https://unjournal.pubpub.org/api/graphql"

def fetch_all_pubs() -> List[Dict[str, Any]]:
    """Fetch all pubs from the Unjournal community."""

    query = """
    query GetPubs {
      community(subdomain: "unjournal") {
        pubs {
          nodes {
            id
            slug
            title
            doi
            reviews {
              id
              title
              text
              createdAt
            }
          }
        }
      }
    }
    """

    response = requests.post(
        PUBPUB_API,
        json={"query": query},
        headers={"Content-Type": "application/json"}
    )

    if response.status_code != 200:
        raise Exception(f"GraphQL query failed: {response.status_code}")

    data = response.json()

    if "errors" in data:
        raise Exception(f"GraphQL errors: {data['errors']}")

    pubs = data.get("data", {}).get("community", {}).get("pubs", {}).get("nodes", [])
    return pubs

def extract_survey_from_text(text: str) -> Dict[str, str]:
    """Extract survey responses from evaluation text using pattern matching."""

    survey_data = {}

    # Pattern for "How long have you been in this field?"
    field_pattern = r"How long have you been in this field[?\s]*:?\s*([^\n]+)"
    match = re.search(field_pattern, text, re.IGNORECASE)
    if match:
        survey_data['years_in_field'] = match.group(1).strip()

    # Pattern for papers reviewed
    papers_pattern = r"How many (?:proposals, )?papers[,\s]+and projects have you (?:evaluated/)?reviewed[?\s]*:?\s*([^\n]+)"
    match = re.search(papers_pattern, text, re.IGNORECASE)
    if match:
        survey_data['papers_reviewed'] = match.group(1).strip()

    # Pattern for time spent
    time_pattern = r"(?:Approximately )?how long did you spend completing this evaluation[?\s]*:?\s*([^\n]+)"
    match = re.search(time_pattern, text, re.IGNORECASE)
    if match:
        survey_data['time_spent'] = match.group(1).strip()

    # Pattern for process rating
    process_pattern = r"How would you rate this template and process[?\s]*:?\s*([^\n]+)"
    match = re.search(process_pattern, text, re.IGNORECASE)
    if match:
        survey_data['process_rating'] = match.group(1).strip()

    # Pattern for field/expertise
    expertise_pattern = r"Field[/\s]*expertise[?\s]*:?\s*([^\n]+)"
    match = re.search(expertise_pattern, text, re.IGNORECASE)
    if match:
        survey_data['field_expertise'] = match.group(1).strip()

    return survey_data

def main():
    print("Fetching pubs from PubPub...")
    pubs = fetch_all_pubs()
    print(f"Found {len(pubs)} pubs")

    all_survey_data = []

    for pub in pubs:
        paper_title = pub.get('title', '')
        reviews = pub.get('reviews', [])

        print(f"\nProcessing: {paper_title}")
        print(f"  Found {len(reviews)} reviews")

        for review in reviews:
            review_text = review.get('text', '')
            review_title = review.get('title', '')

            if not review_text:
                continue

            # Extract survey data from review text
            survey = extract_survey_from_text(review_text)

            if survey:  # Only include if we found some survey data
                survey['paper_title'] = paper_title
                survey['review_title'] = review_title
                survey['review_id'] = review.get('id', '')
                survey['created_at'] = review.get('createdAt', '')
                survey['doi'] = pub.get('doi', '')
                survey['pub_slug'] = pub.get('slug', '')

                all_survey_data.append(survey)
                print(f"  ✓ Extracted survey data from: {review_title}")
                print(f"    Fields found: {list(survey.keys())}")

    # Convert to DataFrame
    df = pd.DataFrame(all_survey_data)

    print(f"\n{'='*80}")
    print(f"Total evaluations with survey data: {len(df)}")
    print(f"\nColumns extracted:")
    for col in df.columns:
        non_null = df[col].notna().sum()
        print(f"  {col}: {non_null} non-null values")

    # Save to CSV
    output_file = "data/pubpub_survey_data.csv"
    df.to_csv(output_file, index=False)
    print(f"\n✓ Saved to: {output_file}")

    # Also save a sample for inspection
    if len(df) > 0:
        sample_file = "data/pubpub_survey_sample.csv"
        df.head(10).to_csv(sample_file, index=False)
        print(f"✓ Sample saved to: {sample_file}")

    return df

if __name__ == "__main__":
    df = main()
