
# import-unjournal-data.py
# standalone script to import data via the coda.io api
# should be run from the project root

from codaio import Coda, Document
from dotenv import load_dotenv
import os
import pandas as pd

# We share API variables with .Renviron, which uses a similar format
# Note that on github the .Renviron path *should not* be there. Instead,
# environment variables are set by github actions from github secrets.
if os.path.isfile(".Renviron"):
  load_dotenv(dotenv_path = ".Renviron")
  
coda_api_key = os.environ["CODA_API_KEY"]

coda = Coda(coda_api_key)

# This is the file of evaluations
doc = Document("0KBG3dSZCs", coda = coda)
research = doc.get_table("grid-Iru9Fra3tE")

research = pd.DataFrame(research.to_dict())
research.to_csv("data/evals.csv")
