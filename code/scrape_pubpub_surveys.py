#!/usr/bin/env python3
"""
Scrape evaluator survey responses from individual PubPub evaluation pages.

This fetches survey data that may be missing from the Coda import by:
1. Getting the RSS feed to list all evaluation summaries
2. Parsing each summary page for individual evaluation links
3. Scraping survey responses from each individual evaluation
4. Outputting a CSV for import into Coda
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from typing import Dict, List, Optional
import time
import xml.etree.ElementTree as ET

def get_all_pub_urls() -> List[str]:
    """Get all evaluation summary URLs from RSS feed."""

    rss_url = "https://unjournal.pubpub.org/rss.xml"
    response = requests.get(rss_url)
    response.raise_for_status()

    root = ET.fromstring(response.content)
    urls = []

    for item in root.findall('.//item'):
        link = item.find('link')
        if link is not None and link.text:
            # Only include evaluation summaries (evalsumXXX)
            if '/pub/evalsum' in link.text:
                urls.append(link.text)

    return urls

def extract_individual_eval_links(summary_url: str) -> List[Dict[str, str]]:
    """Extract individual evaluation links from a summary page."""

    response = requests.get(summary_url)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'html.parser')

    evals = []

    # Find all links that look like individual evaluations
    for link in soup.find_all('a', href=True):
        href = link['href']
        if '/pub/e' in href and 'evalsum' not in href:
            # Get evaluator name from link text if available
            evaluator = link.get_text(strip=True)

            # Make sure it's a full URL
            if not href.startswith('http'):
                href = 'https://unjournal.pubpub.org' + href

            evals.append({
                'eval_url': href,
                'evaluator_hint': evaluator
            })

    # Also try to extract from structured data
    # Look for evaluation links in specific patterns
    article_links = soup.find_all('a', href=re.compile(r'/pub/e\d'))
    for link in article_links:
        href = link['href']
        if not href.startswith('http'):
            href = 'https://unjournal.pubpub.org' + href

        # Avoid duplicates
        if not any(e['eval_url'] == href for e in evals):
            evals.append({
                'eval_url': href,
                'evaluator_hint': link.get_text(strip=True)
            })

    return evals

def scrape_survey_from_evaluation(eval_url: str) -> Optional[Dict[str, str]]:
    """Scrape survey responses from an individual evaluation page."""

    try:
        response = requests.get(eval_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        # Get the page text
        text = soup.get_text()

        # Extract paper title
        title_elem = soup.find('h1')
        paper_title = title_elem.get_text(strip=True) if title_elem else ''

        survey_data = {
            'eval_url': eval_url,
            'paper_title': paper_title
        }

        # Extract field/expertise
        field_match = re.search(
            r'(?:Field|Research field|Expertise)[\s:]*([^\n]{10,200})',
            text, re.IGNORECASE
        )
        if field_match:
            survey_data['field_expertise'] = field_match.group(1).strip()

        # Extract years in field - look for patterns
        years_patterns = [
            r'(?:How long have you been in|Years in).*?field.*?[:\s]([^\n]{5,200})',
            r'(\d+\s*(?:years?|yrs).*?(?:field|experience|working))',
            r'((?:More than|Over|About)\s+\d+\s*years)',
        ]

        for pattern in years_patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                survey_data['years_in_field'] = match.group(1).strip()
                break

        # Extract papers reviewed
        papers_patterns = [
            r'(?:How many|Number of).*?(?:papers|proposals).*?reviewed.*?[:\s]([^\n]{5,150})',
            r'(?:reviewed|evaluated).*?(\d+[\+\-\s]*(?:papers|proposals|projects))',
            r'([Aa]round\s+\d+|[Pp]robably.*?\d+|[Cc]lose to\s+\d+).*?(?:reviews|papers)',
        ]

        for pattern in papers_patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                survey_data['papers_reviewed'] = match.group(1).strip()
                break

        # Extract time spent on this evaluation
        time_patterns = [
            r'(?:How long|time).*?(?:spend|spent).*?(?:this|completing).*?evaluation.*?[:\s]([^\n]{3,100})',
            r'(\d+[\s\-]*(?:hours?|days?|hrs)).*?(?:on|completing|spent)',
        ]

        for pattern in time_patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                survey_data['time_spent'] = match.group(1).strip()
                break

        # Extract process rating
        rating_patterns = [
            r'(?:How would you rate|rating).*?(?:template|process).*?[:\s]([^\n]{3,200})',
            r'(?:template|process).*?(?:rating|score).*?[:\s]([^\n]{3,100})',
        ]

        for pattern in rating_patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                survey_data['process_rating'] = match.group(1).strip()
                break

        # Only return if we found at least some survey data
        if len(survey_data) > 2:  # More than just URL and title
            return survey_data

        return None

    except Exception as e:
        print(f"  Error scraping {eval_url}: {e}")
        return None

def main():
    print("Fetching evaluation summaries from RSS feed...")
    summary_urls = get_all_pub_urls()
    print(f"Found {len(summary_urls)} evaluation summaries")

    all_survey_data = []

    for i, summary_url in enumerate(summary_urls, 1):
        print(f"\n[{i}/{len(summary_urls)}] Processing: {summary_url}")

        # Get individual evaluation links
        try:
            eval_links = extract_individual_eval_links(summary_url)
            print(f"  Found {len(eval_links)} individual evaluations")

            for eval_info in eval_links:
                eval_url = eval_info['eval_url']
                print(f"    Scraping: {eval_url}")

                survey = scrape_survey_from_evaluation(eval_url)

                if survey:
                    all_survey_data.append(survey)
                    fields_found = [k for k in survey.keys() if k not in ['eval_url', 'paper_title']]
                    print(f"      ✓ Found: {', '.join(fields_found)}")
                else:
                    print(f"      - No survey data found")

                # Be nice to the server
                time.sleep(0.5)

        except Exception as e:
            print(f"  Error processing summary: {e}")
            continue

    # Convert to DataFrame
    df = pd.DataFrame(all_survey_data)

    print(f"\n{'='*80}")
    print(f"Total evaluations scraped: {len(df)}")

    if len(df) > 0:
        print(f"\nColumns extracted:")
        for col in df.columns:
            non_null = df[col].notna().sum()
            print(f"  {col}: {non_null} non-null values ({100*non_null/len(df):.1f}%)")

        # Save to CSV
        output_file = "data/pubpub_scraped_survey_data.csv"
        df.to_csv(output_file, index=False)
        print(f"\n✓ Saved to: {output_file}")

        # Save summary stats
        summary = df.describe(include='all').to_csv("data/pubpub_survey_summary_stats.txt")

    else:
        print("\n⚠ No survey data found!")

    return df

if __name__ == "__main__":
    df = main()
