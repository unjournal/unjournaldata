#!/usr/bin/env python3
# explore_survey_responses.py
# Explore the "Responses: academic stream evaluations" table

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

# Get the survey responses table
print("Fetching 'Responses: academic stream evaluations' table...")
print("=" * 80)

survey_table = doc.get_table("grid-aDSyEIerdL")
df = pd.DataFrame(survey_table.to_dict())

if not df.empty:
    print(f"\nTable has {len(df)} rows and {len(df.columns)} columns\n")
    print("Column names:")
    print("-" * 80)
    for i, col in enumerate(df.columns, 1):
        # Show first few non-null values as examples
        sample_values = df[col].dropna().head(2).tolist()
        sample_str = str(sample_values)[:60] if sample_values else "(all null)"
        print(f"{i:3}. {col}")
        print(f"     Sample: {sample_str}")

    # Save to CSV for inspection
    df.to_csv("data/survey_responses_preview.csv", index=False)
    print(f"\n\nFull data saved to: data/survey_responses_preview.csv")
else:
    print("Table is empty")
