#!/usr/bin/env python3
# list_coda_tables.py
# Quick script to just list table names and IDs

from codaio import Coda, Document
from dotenv import load_dotenv
import os

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
    print(f"[{i+1}] {table_info.name}")
    print(f"    ID: {table_info.id}")
