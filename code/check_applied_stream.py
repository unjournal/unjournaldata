#!/usr/bin/env python3
from codaio import Coda, Document
from dotenv import load_dotenv
import os
import pandas as pd

if os.path.isfile(".Renviron"):
    load_dotenv(dotenv_path=".Renviron")

coda_api_key = os.environ["CODA_API_KEY"]
coda = Coda(coda_api_key)
doc = Document("0KBG3dSZCs", coda=coda)

# Check applied stream evaluations table
print("Applied stream evaluations table:")
applied = doc.get_table("grid-znNSTj_xX3")
df = pd.DataFrame(applied.to_dict())
print(f"Rows: {len(df)}")
print(f"Columns: {list(df.columns)[:20]}")  # First 20 columns
