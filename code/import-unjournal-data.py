
# import-unjournal-data.py
# standalone script to import data via the coda.io api
# should be run from the project root

# THIS SCRIPT IMPORTS DATA FROM THE UNJOURNAL DATABASE INTO A **PUBLIC** 
# REPOSITORY.
# Check with management before adding columns and/or tables!

from codaio import Coda, Document
from dotenv import load_dotenv
import os
import pandas as pd
import re

# We share API variables with .Renviron, which uses a similar format
# Note that the .Renviron file *must not* be on github. Instead,
# environment variables are set by github actions from github secrets.
if os.path.isfile(".Renviron"):
  load_dotenv(dotenv_path = ".Renviron")
  
coda_api_key = os.environ["CODA_API_KEY"]
coda = Coda(coda_api_key)
doc = Document("0KBG3dSZCs", coda = coda)

# This is the file of evaluations
research = doc.get_table("grid-Iru9Fra3tE")
research = pd.DataFrame(research.to_dict())
columns = ['label_paper_title', 'status', 'research_url', 'doi', 
  'main_cause_cat', 'secondary_cause_cat',
  'publication_status', 'working_paper_release_date', 'topic_subfield',
  'source_main']
research = research[columns]
research.to_csv("data/research.csv", index = False)

# Evaluator ratings
rsx_evalr_rating = doc.get_table("grid-pcJr9ZM3wT")
rsx_evalr_rating = pd.DataFrame(rsx_evalr_rating.to_dict())
columns = ['research', 'evaluator', 'criteria', 'middle_rating', 
  'lower_CI', 'upper_CI', 'confidence_level', 'row_created_date']
rsx_evalr_rating = rsx_evalr_rating[columns]
rsx_evalr_rating.to_csv("data/rsx_evalr_rating.csv", index = False)

paper_authors = doc.get_table("grid-bJ5HubGR8H")
paper_authors = pd.DataFrame(paper_authors.to_dict())
columns = ['research', 'author', 'author_emails', 'corresponding']
paper_authors = paper_authors[columns]
paper_authors.to_csv("data/paper_authors.csv", index = False)
