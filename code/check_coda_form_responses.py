#!/usr/bin/env python3
"""
Check Coda evaluation form response tables for missing CI values.

This script queries the academic and applied stream evaluation response tables
to find CI values that are missing from the aggregated rsx_evalr_rating table.
"""

from codaio import Coda, Document
from dotenv import load_dotenv
import os
import pandas as pd

# Load environment variables
if os.path.isfile(".Renviron"):
    load_dotenv(dotenv_path=".Renviron")

coda_api_key = os.environ["CODA_API_KEY"]
coda = Coda(coda_api_key)
doc = Document("0KBG3dSZCs", coda=coda)

print("Fetching academic stream evaluation responses...")
# Academic stream: grid-aDSyEIerdL
academic_survey = doc.get_table("grid-aDSyEIerdL")
academic_survey_df = pd.DataFrame(academic_survey.to_dict())

print(f"Academic stream columns ({len(academic_survey_df.columns)}):")
for col in sorted(academic_survey_df.columns):
    print(f"  - {col}")

print(f"\nAcademic stream rows: {len(academic_survey_df)}")

print("\n" + "="*80)
print("Fetching applied stream evaluation responses...")
# Applied stream: grid-znNSTj_xX3
applied_survey = doc.get_table("grid-znNSTj_xX3")
applied_survey_df = pd.DataFrame(applied_survey.to_dict())

print(f"Applied stream columns ({len(applied_survey_df.columns)}):")
for col in sorted(applied_survey_df.columns):
    print(f"  - {col}")

print(f"\nApplied stream rows: {len(applied_survey_df)}")

# Save both to CSV for inspection
academic_survey_df.to_csv("data/academic_stream_responses.csv", index=False)
print(f"\nSaved academic stream to: data/academic_stream_responses.csv")

applied_survey_df.to_csv("data/applied_stream_responses.csv", index=False)
print(f"Saved applied stream to: data/applied_stream_responses.csv")

# Now let's check if these tables have CI columns
print("\n" + "="*80)
print("Looking for CI-related columns...")

ci_columns_academic = [col for col in academic_survey_df.columns if 'CI' in col or 'confidence' in col.lower()]
print(f"\nAcademic stream CI columns ({len(ci_columns_academic)}):")
for col in ci_columns_academic:
    non_null = academic_survey_df[col].notna().sum()
    print(f"  - {col}: {non_null} non-null values")

ci_columns_applied = [col for col in applied_survey_df.columns if 'CI' in col or 'confidence' in col.lower()]
print(f"\nApplied stream CI columns ({len(ci_columns_applied)}):")
for col in ci_columns_applied:
    non_null = applied_survey_df[col].notna().sum()
    print(f"  - {col}: {non_null} non-null values")

# Look for rating columns
print("\n" + "="*80)
print("Looking for rating-related columns...")

rating_columns_academic = [col for col in academic_survey_df.columns if 'rating' in col.lower() or 'score' in col.lower()]
print(f"\nAcademic stream rating columns ({len(rating_columns_academic)}):")
for col in rating_columns_academic[:20]:  # Show first 20
    non_null = academic_survey_df[col].notna().sum()
    print(f"  - {col}: {non_null} non-null values")

rating_columns_applied = [col for col in applied_survey_df.columns if 'rating' in col.lower() or 'score' in col.lower()]
print(f"\nApplied stream rating columns ({len(rating_columns_applied)}):")
for col in rating_columns_applied[:20]:  # Show first 20
    non_null = applied_survey_df[col].notna().sum()
    print(f"  - {col}: {non_null} non-null values")
