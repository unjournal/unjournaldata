#!/usr/bin/env python3
# explore_coda_tables.py
# Script to explore available tables and columns in Coda database

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

# List all tables in the document
print("Available tables in Coda document:")
print("=" * 80)

tables = doc.list_tables()
for i, table_info in enumerate(tables):
    print(f"\n[{i+1}] Table: {table_info.name}")
    print(f"    ID: {table_info.id}")

    # Try to get a sample of columns from each table
    try:
        table_obj = doc.get_table(table_info.id)
        df = pd.DataFrame(table_obj.to_dict())
        if not df.empty:
            print(f"    Columns ({len(df.columns)}): {list(df.columns)}")
            print(f"    Rows: {len(df)}")
        else:
            print("    (empty table)")
    except Exception as e:
        print(f"    Error accessing table: {e}")
