"""
Analysis script to identify high-quality Unjournal papers since January 2024.

This script:
1. Loads and filters Unjournal data for papers evaluated since Jan 2024
2. Calculates quality metrics (merit scores, confidence-adjusted ratings, diamond scores)
3. Matches papers to evaluation markdown files and extracts excerpts
4. Identifies author responses and assesses engagement quality
5. Generates visualizations and exports summary data for blog post

Output:
- Top papers summary CSV
- Evaluation excerpts JSON
- Visualization plots
"""

import pandas as pd
import numpy as np
from datetime import datetime
from pathlib import Path
import yaml
import json
import re
import logging
from typing import Dict, List, Tuple, Optional
import matplotlib.pyplot as plt
import seaborn as sns
from fuzzywuzzy import fuzz, process

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('analysis.log'),
        logging.StreamHandler()
    ]
)

# Define paths
DATA_DIR = Path("/Users/yosemite/githubs/unjournaldatafix/data")
EVAL_DIR = Path("/Users/yosemite/githubs/unjournaldatafix/unjournal_evaluations")
OUTPUT_DIR = Path("/Users/yosemite/githubs/unjournaldatafix/website/posts/high-quality-papers-2024")
VIZ_DIR = OUTPUT_DIR / "visualizations"

# Create output directories
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
VIZ_DIR.mkdir(parents=True, exist_ok=True)

# Set plot style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 11


def load_data() -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Load all core datasets."""
    logging.info("Loading data files...")

    research_df = pd.read_csv(DATA_DIR / "research.csv")
    ratings_df = pd.read_csv(DATA_DIR / "rsx_evalr_rating.csv")
    evaluator_paper_df = pd.read_csv(DATA_DIR / "evaluator_paper_level.csv")
    authors_df = pd.read_csv(DATA_DIR / "paper_authors.csv")

    logging.info(f"Loaded: {len(research_df)} papers, {len(ratings_df)} ratings, "
                f"{len(evaluator_paper_df)} evaluator-paper combinations")

    return research_df, ratings_df, evaluator_paper_df, authors_df


def filter_2024_papers(research_df: pd.DataFrame, ratings_df: pd.DataFrame) -> pd.DataFrame:
    """Filter for papers evaluated since 2024-01-01 (based on rating submission dates)."""
    logging.info("Filtering for papers evaluated in 2024-2025...")

    # Convert rating dates to datetime
    ratings_df['eval_date'] = pd.to_datetime(
        ratings_df['row_created_date'],
        errors='coerce',
        utc=True
    )

    # Get papers with ratings from 2024 onwards
    cutoff_date = pd.to_datetime('2024-01-01', utc=True)
    ratings_2024_2025 = ratings_df[ratings_df['eval_date'] >= cutoff_date]

    # Get unique paper titles evaluated in 2024-2025
    papers_titles = ratings_2024_2025['research'].unique()

    # Filter research_df to these papers
    papers_filtered = research_df[research_df['label_paper_title'].isin(papers_titles)].copy()

    logging.info(f"Found {len(papers_filtered)} papers evaluated in 2024-2025")

    return papers_filtered


def calculate_merit_scores(ratings_df: pd.DataFrame) -> pd.DataFrame:
    """Calculate mean merit scores per paper."""
    logging.info("Calculating merit scores...")

    merit_ratings = ratings_df[ratings_df['criteria'] == 'merits_journal'].copy()

    merit_summary = merit_ratings.groupby('research').agg({
        'middle_rating': ['mean', 'std', 'count'],
        'lower_CI': 'mean',
        'upper_CI': 'mean'
    }).reset_index()

    merit_summary.columns = ['paper_title', 'merit_mean', 'merit_std',
                              'num_evaluators', 'merit_lower_ci', 'merit_upper_ci']

    return merit_summary


def calculate_overall_scores(ratings_df: pd.DataFrame) -> pd.DataFrame:
    """Calculate mean overall scores per paper."""
    logging.info("Calculating overall scores...")

    overall_ratings = ratings_df[ratings_df['criteria'] == 'overall'].copy()

    overall_summary = overall_ratings.groupby('research').agg({
        'middle_rating': ['mean', 'std'],
        'lower_CI': 'mean',
        'upper_CI': 'mean'
    }).reset_index()

    overall_summary.columns = ['paper_title', 'overall_mean', 'overall_std',
                                'overall_lower_ci', 'overall_upper_ci']

    return overall_summary


def calculate_diamond_scores(ratings_df: pd.DataFrame) -> pd.DataFrame:
    """Calculate diamond scores (merit - predicted journal tier)."""
    logging.info("Calculating diamond scores...")

    # Get merit and predict scores
    merit = ratings_df[ratings_df['criteria'] == 'merits_journal'].groupby('research')['middle_rating'].mean()
    predict = ratings_df[ratings_df['criteria'] == 'journal_predict'].groupby('research')['middle_rating'].mean()

    # Create dataframes and merge to handle papers with only one score
    merit_df = merit.reset_index()
    merit_df.columns = ['paper_title', 'merit_mean']

    predict_df = predict.reset_index()
    predict_df.columns = ['paper_title', 'predict_mean']

    diamond_df = merit_df.merge(predict_df, on='paper_title', how='outer')

    diamond_df['diamond_score'] = diamond_df['merit_mean'] - diamond_df['predict_mean']

    logging.info(f"Found {len(diamond_df[diamond_df['diamond_score'] > 0])} papers "
                f"with positive diamond scores")

    return diamond_df


def calculate_confidence_scores(ratings_df: pd.DataFrame) -> pd.DataFrame:
    """Calculate confidence-adjusted scores (narrower CI = higher confidence)."""
    logging.info("Calculating confidence-adjusted scores...")

    # Focus on key criteria
    key_criteria = ['merits_journal', 'overall', 'adv_knowledge']

    confidence_scores = []

    for criterion in key_criteria:
        criterion_data = ratings_df[ratings_df['criteria'] == criterion].copy()

        # Calculate CI width (handle missing CIs)
        criterion_data['ci_width'] = criterion_data['upper_CI'] - criterion_data['lower_CI']
        criterion_data['ci_width'] = criterion_data['ci_width'].replace(0, np.nan)

        # Confidence score: inverse of CI width (normalized by rating)
        # Higher score = narrower CI = more confident
        criterion_data['confidence_score'] = criterion_data['middle_rating'] / (criterion_data['ci_width'] + 0.1)

        # Average per paper
        paper_confidence = criterion_data.groupby('research')['confidence_score'].mean().reset_index()
        paper_confidence.columns = ['paper_title', f'{criterion}_confidence']

        confidence_scores.append(paper_confidence)

    # Merge all criteria
    result = confidence_scores[0]
    for df in confidence_scores[1:]:
        result = result.merge(df, on='paper_title', how='outer')

    return result


def calculate_aggregate_score(merged_df: pd.DataFrame) -> pd.DataFrame:
    """Calculate weighted aggregate quality score."""
    logging.info("Calculating aggregate quality scores...")

    # Weights
    weights = {
        'merit_mean': 0.30,
        'overall_mean': 0.25,
        'merits_journal_confidence': 0.20,
        'adv_knowledge_mean': 0.10,
        'hours_spent': 0.15
    }

    # Normalize scores to 0-1 scale
    for col in ['merit_mean', 'overall_mean', 'adv_knowledge_mean']:
        if col in merged_df.columns:
            max_val = merged_df[col].max()
            if max_val > 0:
                merged_df[f'{col}_norm'] = merged_df[col] / max_val

    # Normalize confidence scores
    if 'merits_journal_confidence' in merged_df.columns:
        max_conf = merged_df['merits_journal_confidence'].max()
        if max_conf > 0:
            merged_df['merits_journal_confidence_norm'] = merged_df['merits_journal_confidence'] / max_conf

    # Normalize hours spent
    if 'hours_spent' in merged_df.columns:
        max_hours = merged_df['hours_spent'].max()
        if max_hours > 0:
            merged_df['hours_spent_norm'] = merged_df['hours_spent'] / max_hours

    # Calculate aggregate score
    merged_df['aggregate_score'] = 0

    if 'merit_mean_norm' in merged_df.columns:
        merged_df['aggregate_score'] += weights['merit_mean'] * merged_df['merit_mean_norm'].fillna(0)
    if 'overall_mean_norm' in merged_df.columns:
        merged_df['aggregate_score'] += weights['overall_mean'] * merged_df['overall_mean_norm'].fillna(0)
    if 'merits_journal_confidence_norm' in merged_df.columns:
        merged_df['aggregate_score'] += weights['merits_journal_confidence'] * merged_df['merits_journal_confidence_norm'].fillna(0)
    if 'adv_knowledge_mean_norm' in merged_df.columns:
        merged_df['aggregate_score'] += weights['adv_knowledge_mean'] * merged_df['adv_knowledge_mean_norm'].fillna(0)
    if 'hours_spent_norm' in merged_df.columns:
        merged_df['aggregate_score'] += weights['hours_spent'] * merged_df['hours_spent_norm'].fillna(0)

    return merged_df


def get_adv_knowledge_scores(ratings_df: pd.DataFrame) -> pd.DataFrame:
    """Get advancing knowledge scores."""
    adv_know = ratings_df[ratings_df['criteria'] == 'adv_knowledge'].copy()

    adv_know_summary = adv_know.groupby('research').agg({
        'middle_rating': 'mean'
    }).reset_index()

    adv_know_summary.columns = ['paper_title', 'adv_knowledge_mean']

    return adv_know_summary


def parse_markdown_frontmatter(file_path: Path) -> Dict:
    """Parse YAML frontmatter from markdown file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract YAML frontmatter
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                yaml_content = parts[1]
                frontmatter = yaml.safe_load(yaml_content)
                markdown_body = parts[2]
                return {
                    'frontmatter': frontmatter,
                    'body': markdown_body,
                    'full_content': content
                }
    except Exception as e:
        logging.warning(f"Error parsing {file_path.name}: {e}")

    return {'frontmatter': {}, 'body': '', 'full_content': ''}


def match_papers_to_evaluations(papers_2024: pd.DataFrame) -> Dict[str, List[Path]]:
    """Match each paper to its evaluation markdown files."""
    logging.info("Matching papers to evaluation files...")

    # Get all evaluation markdown files
    eval_files = list(EVAL_DIR.glob("*.md"))
    # Filter out manifest and metadata files
    eval_files = [f for f in eval_files if f.stem not in ['manifest', 'state', 'compiledevaluations']]
    logging.info(f"Found {len(eval_files)} markdown files")

    # Parse all evaluation files and extract titles
    eval_file_map = {}
    for eval_file in eval_files:
        parsed = parse_markdown_frontmatter(eval_file)
        frontmatter = parsed['frontmatter']

        # Extract title from frontmatter
        if 'title' in frontmatter:
            # Remove "Evaluation 1 of ", "Evaluation 2 of ", etc. to get paper title
            title = frontmatter['title']
            # Remove evaluation prefix and quotes
            title = re.sub(r'^Evaluation \d+ of\s*["\']?', '', title, flags=re.IGNORECASE)
            title = re.sub(r'^Authors["\']?\s*response to.*evaluations of\s*["\']?', '', title, flags=re.IGNORECASE)
            title = title.strip('"\'')
            eval_file_map[eval_file] = title

    # Match papers to evaluation files
    paper_eval_map = {}

    for paper_title in papers_2024['label_paper_title'].dropna():
        matches = []

        # Normalize paper title for matching
        paper_norm = re.sub(r'[^a-z0-9\s]', '', paper_title.lower())
        paper_words = set(paper_norm.split())

        for eval_file, eval_title in eval_file_map.items():
            # Skip author response files for now (we'll match them separately)
            if 'authorsresponse' in eval_file.stem.lower() or 'ar_' in eval_file.stem.lower():
                continue

            # Normalize evaluation title
            eval_norm = re.sub(r'[^a-z0-9\s]', '', eval_title.lower())
            eval_words = set(eval_norm.split())

            # Calculate word overlap
            common_words = paper_words & eval_words
            # Require at least 3 common words or 50% overlap
            if len(common_words) >= 3 or (len(common_words) / min(len(paper_words), len(eval_words)) > 0.5):
                # Use fuzzy matching for final check
                similarity = fuzz.token_sort_ratio(paper_norm, eval_norm)
                if similarity > 60:  # Lower threshold since we have word overlap
                    matches.append(eval_file)
                    logging.debug(f"Matched '{paper_title[:50]}' to '{eval_file.name}' (similarity: {similarity})")

        if matches:
            paper_eval_map[paper_title] = matches
            logging.info(f"  Matched '{paper_title[:60]}' to {len(matches)} files")

    logging.info(f"Successfully matched {len(paper_eval_map)} papers to evaluation files")

    return paper_eval_map


def extract_evaluation_excerpts(eval_file: Path, max_excerpts: int = 5) -> List[str]:
    """Extract quality-related excerpts from evaluation."""
    parsed = parse_markdown_frontmatter(eval_file)
    body = parsed['body']

    if not body:
        return []

    excerpts = []

    # Split into paragraphs
    paragraphs = [p.strip() for p in body.split('\n\n') if p.strip()]

    # Keywords indicating quality praise
    quality_keywords = [
        'strong', 'rigorous', 'robust', 'novel', 'important', 'excellent',
        'well-designed', 'careful', 'thorough', 'impressive', 'compelling',
        'significant contribution', 'methodological', 'innovative'
    ]

    for para in paragraphs:
        # Skip very short paragraphs or headers
        if len(para) < 100 or para.startswith('#'):
            continue

        # Check if paragraph contains quality keywords
        para_lower = para.lower()
        if any(keyword in para_lower for keyword in quality_keywords):
            # Clean up the excerpt
            excerpt = para[:500]  # Limit length
            if len(para) > 500:
                excerpt += "..."
            excerpts.append(excerpt)

        if len(excerpts) >= max_excerpts:
            break

    return excerpts


def find_author_responses(paper_title: str, all_eval_files: List[Path]) -> Optional[Path]:
    """Find author response file for a given paper."""
    # Normalize paper title for matching
    paper_norm = re.sub(r'[^a-z0-9\s]', '', paper_title.lower())
    paper_words = set(paper_norm.split())

    for eval_file in all_eval_files:
        filename = eval_file.stem.lower()

        # Check if it's an author response file
        if 'authorsresponse' in filename or filename.startswith('ar_'):
            # Try to extract paper title from frontmatter
            parsed = parse_markdown_frontmatter(eval_file)
            frontmatter = parsed.get('frontmatter', {})

            if 'title' in frontmatter:
                # Remove "Authors' response..." prefix
                title = frontmatter['title']
                title = re.sub(r'^Authors["\']?\s*response to.*evaluations of\s*["\']?', '', title, flags=re.IGNORECASE)
                title = re.sub(r'^Authors["\']?\s*response.*["\']?', '', title, flags=re.IGNORECASE)
                title = title.strip('"\'')

                # Normalize and compare
                title_norm = re.sub(r'[^a-z0-9\s]', '', title.lower())
                title_words = set(title_norm.split())

                # Calculate word overlap
                common_words = paper_words & title_words
                if len(common_words) >= 3 or (len(common_words) / min(len(paper_words), len(title_words)) > 0.5):
                    similarity = fuzz.token_sort_ratio(paper_norm, title_norm)
                    if similarity > 60:
                        return eval_file

    return None


def assess_author_response_quality(response_file: Path) -> Dict:
    """Assess the quality of author response."""
    parsed = parse_markdown_frontmatter(response_file)
    body = parsed['body']

    if not body:
        return {'has_response': False}

    word_count = len(body.split())

    # Look for indicators of substantive engagement
    engagement_indicators = [
        'we have added', 'we have revised', 'we now include',
        'additional analysis', 'robustness check', 'we agree',
        'thank you for', 'in response to', 'we have updated'
    ]

    body_lower = body.lower()
    num_indicators = sum(1 for indicator in engagement_indicators if indicator in body_lower)

    return {
        'has_response': True,
        'response_length': word_count,
        'substantive': word_count > 500 and num_indicators >= 2,
        'response_file': response_file.name,
        'engagement_indicators': num_indicators
    }


def extract_pubpub_url(paper_title: str, eval_files: List[Path], research_df: pd.DataFrame) -> str:
    """Extract PubPub URL for a paper from evaluation files or CSV data."""
    # Try to find evaluation summary file
    for eval_file in eval_files:
        if 'evalsum' in eval_file.stem.lower():
            parsed = parse_markdown_frontmatter(eval_file)
            frontmatter = parsed.get('frontmatter', {})

            # Check for uri field in frontmatter
            if 'uri' in frontmatter:
                return frontmatter['uri']

            # Check for article.elocation-id
            if 'article' in frontmatter and isinstance(frontmatter['article'], dict):
                if 'elocation-id' in frontmatter['article']:
                    eloc_id = frontmatter['article']['elocation-id']
                    return f"https://unjournal.pubpub.org/pub/{eloc_id}"

    # Fallback: check research_url in research.csv
    paper_data = research_df[research_df['label_paper_title'] == paper_title]
    if len(paper_data) > 0 and 'research_url' in paper_data.columns:
        research_url = paper_data.iloc[0]['research_url']
        if pd.notna(research_url) and 'pubpub.org' in str(research_url):
            return str(research_url)

    # If no URL found, return empty string
    return ''


def get_hours_spent(evaluator_paper_df: pd.DataFrame, paper_title: str) -> float:
    """Get total hours spent evaluating a paper."""
    paper_evals = evaluator_paper_df[evaluator_paper_df['paper_title'] == paper_title]

    if len(paper_evals) == 0:
        return 0.0

    hours = paper_evals['hours_spent_manual_impute'].sum()
    return hours if pd.notna(hours) else 0.0


def main():
    """Main analysis workflow."""
    logging.info("="*60)
    logging.info("Starting High-Quality Papers Analysis")
    logging.info("="*60)

    # 1. Load data
    research_df, ratings_df, evaluator_paper_df, authors_df = load_data()

    # 2. Filter for papers evaluated in 2024
    papers_2024 = filter_2024_papers(research_df, ratings_df)

    # 3. Calculate quality metrics
    merit_scores = calculate_merit_scores(ratings_df)
    overall_scores = calculate_overall_scores(ratings_df)
    diamond_scores = calculate_diamond_scores(ratings_df)
    confidence_scores = calculate_confidence_scores(ratings_df)
    adv_knowledge_scores = get_adv_knowledge_scores(ratings_df)

    # 4. Merge all metrics
    logging.info("Merging all quality metrics...")

    merged = papers_2024[['label_paper_title', 'doi', 'research_url',
                           'publication_status', 'main_cause_cat',
                           'topic_subfield', 'working_paper_release_date']].copy()

    merged = merged.merge(merit_scores, left_on='label_paper_title',
                          right_on='paper_title', how='left')
    merged = merged.merge(overall_scores, left_on='label_paper_title',
                          right_on='paper_title', how='left', suffixes=('', '_y'))
    merged = merged.merge(diamond_scores[['paper_title', 'diamond_score', 'predict_mean']],
                          left_on='label_paper_title', right_on='paper_title',
                          how='left', suffixes=('', '_z'))
    merged = merged.merge(confidence_scores, left_on='label_paper_title',
                          right_on='paper_title', how='left', suffixes=('', '_conf'))
    merged = merged.merge(adv_knowledge_scores, left_on='label_paper_title',
                          right_on='paper_title', how='left', suffixes=('', '_adv'))

    # Clean up duplicate columns
    merged = merged.loc[:, ~merged.columns.str.endswith('_y')]
    merged = merged.loc[:, ~merged.columns.str.endswith('_z')]
    merged = merged.loc[:, ~merged.columns.str.endswith('_conf')]
    merged = merged.loc[:, ~merged.columns.str.endswith('_adv')]

    # Remove duplicate paper_title columns
    paper_title_cols = [col for col in merged.columns if col.startswith('paper_title')]
    if len(paper_title_cols) > 1:
        merged = merged.drop(columns=paper_title_cols[1:])

    # Add hours spent
    merged['hours_spent'] = merged['label_paper_title'].apply(
        lambda x: get_hours_spent(evaluator_paper_df, x)
    )

    # 5. Calculate aggregate scores
    merged = calculate_aggregate_score(merged)

    # 6. Match to evaluation files and extract excerpts
    paper_eval_map = match_papers_to_evaluations(papers_2024)

    all_eval_files = list(EVAL_DIR.glob("*.md"))

    evaluation_data = []
    for paper_title in merged['label_paper_title']:
        if pd.isna(paper_title):
            continue

        eval_files = paper_eval_map.get(paper_title, [])

        # Extract excerpts from all evaluation files
        all_excerpts = []
        for eval_file in eval_files:
            if 'authorsresponse' not in eval_file.stem.lower():
                excerpts = extract_evaluation_excerpts(eval_file)
                all_excerpts.extend(excerpts)

        # Find author response
        response_file = find_author_responses(paper_title, all_eval_files)
        response_quality = {}
        if response_file:
            response_quality = assess_author_response_quality(response_file)
        else:
            response_quality = {'has_response': False}

        # Extract PubPub URL
        pubpub_url = extract_pubpub_url(paper_title, eval_files, research)

        evaluation_data.append({
            'paper_title': paper_title,
            'eval_files': [f.name for f in eval_files],
            'num_eval_files': len([f for f in eval_files if 'authorsresponse' not in f.stem.lower()]),
            'excerpts': all_excerpts[:5],  # Top 5 excerpts
            'pubpub_url': pubpub_url,
            **response_quality
        })

    eval_df = pd.DataFrame(evaluation_data)
    merged = merged.merge(eval_df, left_on='label_paper_title', right_on='paper_title',
                          how='left', suffixes=('', '_eval'))

    # Clean up duplicate columns again
    if 'paper_title_eval' in merged.columns:
        merged = merged.drop(columns=['paper_title_eval'])

    # 7. Sort by aggregate score and filter top papers
    merged_sorted = merged.sort_values('aggregate_score', ascending=False)

    # Filter for papers with actual evaluations
    top_papers = merged_sorted[merged_sorted['num_evaluators'] >= 1].copy()

    logging.info(f"Identified {len(top_papers)} papers with evaluations")
    logging.info(f"Top 20 papers by aggregate score:")
    for idx, row in top_papers.head(20).iterrows():
        logging.info(f"  - {row['label_paper_title'][:60]}: {row['aggregate_score']:.3f}")

    # 8. Export results
    logging.info("Exporting results...")

    # Save top papers summary
    output_cols = [
        'label_paper_title', 'aggregate_score', 'merit_mean', 'merit_std',
        'overall_mean', 'diamond_score', 'predict_mean', 'num_evaluators',
        'hours_spent', 'has_response', 'response_length', 'substantive',
        'doi', 'research_url', 'pubpub_url', 'publication_status', 'main_cause_cat',
        'working_paper_release_date', 'num_eval_files'
    ]

    # Only include columns that exist
    output_cols = [col for col in output_cols if col in top_papers.columns]

    top_papers[output_cols].to_csv(OUTPUT_DIR / 'top_papers_summary.csv', index=False)
    logging.info(f"Saved top papers summary to {OUTPUT_DIR / 'top_papers_summary.csv'}")

    # Save evaluation excerpts as JSON
    excerpts_data = {}
    for _, row in top_papers.head(20).iterrows():
        if pd.notna(row.get('label_paper_title')) and 'excerpts' in row:
            # Handle NaN values properly for JSON
            response_file = row.get('response_file', '')
            if pd.isna(response_file):
                response_file = ''

            excerpts_data[row['label_paper_title']] = {
                'excerpts': row.get('excerpts', []),
                'eval_files': row.get('eval_files', []),
                'has_response': bool(row.get('has_response', False)),
                'response_file': str(response_file)
            }

    with open(OUTPUT_DIR / 'evaluation_excerpts.json', 'w') as f:
        json.dump(excerpts_data, f, indent=2)

    logging.info(f"Saved evaluation excerpts to {OUTPUT_DIR / 'evaluation_excerpts.json'}")

    # 9. Generate visualizations
    logging.info("Generating visualizations...")

    # Quality scatter plot
    fig, ax = plt.subplots(figsize=(12, 8))
    scatter = ax.scatter(
        top_papers['merit_mean'],
        top_papers['overall_mean'],
        s=top_papers['num_evaluators'] * 100,
        alpha=0.6,
        c=top_papers['aggregate_score'],
        cmap='viridis'
    )
    ax.set_xlabel('Merit Score (1-5)', fontsize=12)
    ax.set_ylabel('Overall Score (0-100)', fontsize=12)
    ax.set_title('Quality Distribution: Papers Evaluated in 2024-2025', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)

    # Add colorbar
    cbar = plt.colorbar(scatter, ax=ax)
    cbar.set_label('Aggregate Quality Score', fontsize=11)

    # Add annotation for top papers
    for idx, row in top_papers.head(5).iterrows():
        if pd.notna(row['merit_mean']) and pd.notna(row['overall_mean']):
            ax.annotate(
                row['label_paper_title'][:40] + '...',
                (row['merit_mean'], row['overall_mean']),
                xytext=(5, 5),
                textcoords='offset points',
                fontsize=10,
                fontweight='bold',
                alpha=0.7
            )

    plt.tight_layout()
    plt.savefig(VIZ_DIR / 'quality_scatter.png', dpi=300, bbox_inches='tight')
    plt.close()
    logging.info(f"  Saved quality scatter plot")

    # Diamond score plot
    diamonds = top_papers[top_papers['diamond_score'].notna()].copy()
    if len(diamonds) > 0:
        fig, ax = plt.subplots(figsize=(12, 8))

        # Plot diagonal line (merit = predict)
        min_val = min(diamonds['predict_mean'].min(), diamonds['merit_mean'].min())
        max_val = max(diamonds['predict_mean'].max(), diamonds['merit_mean'].max())
        ax.plot([min_val, max_val], [min_val, max_val], 'k--', alpha=0.3, label='Merit = Predict')

        # Scatter plot - only highlight diamonds with >= 0.5 difference
        colors = ['red' if x >= 0.5 else 'blue' for x in diamonds['diamond_score']]
        scatter = ax.scatter(
            diamonds['predict_mean'],
            diamonds['merit_mean'],
            s=150,
            alpha=0.6,
            c=colors
        )

        ax.set_xlabel('Predicted Journal Tier (1-5)', fontsize=12)
        ax.set_ylabel('Merited Journal Tier (1-5)', fontsize=12)
        ax.set_title('Diamonds in the Rough: Merit vs. Predicted Publication Tier', fontsize=14, fontweight='bold')
        ax.grid(True, alpha=0.3)
        ax.legend()

        # Annotate top diamonds (only those with >= 0.5 difference)
        significant_diamonds = diamonds[diamonds['diamond_score'] >= 0.5].nlargest(5, 'diamond_score')
        for idx, row in significant_diamonds.iterrows():
            ax.annotate(
                row['label_paper_title'][:35] + '...',
                (row['predict_mean'], row['merit_mean']),
                xytext=(5, 5),
                textcoords='offset points',
                fontsize=10,
                fontweight='bold',
                alpha=0.7
            )

        plt.tight_layout()
        plt.savefig(VIZ_DIR / 'diamond_plot.png', dpi=300, bbox_inches='tight')
        plt.close()
        logging.info(f"  Saved diamond plot")

    logging.info("="*60)
    logging.info("Analysis complete!")
    logging.info("="*60)

    return top_papers


if __name__ == "__main__":
    top_papers = main()
    print(f"\nAnalysis complete. Found {len(top_papers)} papers with evaluations.")
    print(f"Results saved to {OUTPUT_DIR}")
