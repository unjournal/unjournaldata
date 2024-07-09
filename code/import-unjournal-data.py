
# import-unjournal-data.py
# standalone script to import data via the coda.io api
# should be run from the project root

from codaio import Coda, Document
from dotenv import load_dotenv
import os
import pandas as pd
import re

def strip_columns_with_space(df):
  cols = df.columns
  cols_with_space = [col for col in cols if re.search(" ", col) is not None]
  df = df.drop(columns = cols_with_space)
  return df

# We share API variables with .Renviron, which uses a similar format
# Note that on github the .Renviron path *should not* be there. Instead,
# environment variables are set by github actions from github secrets.
if os.path.isfile(".Renviron"):
  load_dotenv(dotenv_path = ".Renviron")
  
coda_api_key = os.environ["CODA_API_KEY"]

coda = Coda(coda_api_key)

doc = Document("0KBG3dSZCs", coda = coda)

# This is the file of evaluations
research = doc.get_table("grid-Iru9Fra3tE")
research = pd.DataFrame(research.to_dict())
research = strip_columns_with_space(research)
research.to_csv("data/research.csv")

# Evaluator ratings
rsx_evalr_rating = doc.get_table("grid-pcJr9ZM3wT")
rsx_evalr_rating = pd.DataFrame(rsx_evalr_rating.to_dict())
rsx_evalr_rating = strip_columns_with_space(rsx_evalr_rating)
rsx_evalr_rating.to_csv("data/rsx_evalr_rating.csv")