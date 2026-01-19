
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
  'main_cause_cat', 'main_cause_cat_abbrev', 'secondary_cause_cat',
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

# Robust handling: accept either 'author_email' or 'author_emails' from Coda
cols = list(paper_authors.columns)
if 'author_email' in cols:
    author_email_col = 'author_email'
elif 'author_emails' in cols:
    author_email_col = 'author_emails'
else:
    raise KeyError("Coda table missing 'author_email' or 'author_emails' column")

columns = ['research', 'author', author_email_col, 'corresponding']
paper_authors = paper_authors[columns]

# Normalize to 'author_email' for consistent downstream usage
if author_email_col != 'author_email':
    paper_authors = paper_authors.rename(columns={author_email_col: 'author_email'})

paper_authors.to_csv("data/paper_authors.csv", index = False)

# Evaluator survey responses (PUBLIC COLUMNS ONLY - NO CONFIDENTIAL DATA)
# Combines responses from both academic and applied stream evaluations
# Academic stream
academic_survey = doc.get_table("grid-aDSyEIerdL")
academic_survey = pd.DataFrame(academic_survey.to_dict())

# Applied stream
applied_survey = doc.get_table("grid-znNSTj_xX3")
applied_survey = pd.DataFrame(applied_survey.to_dict())

# Standardize column names between the two tables
academic_survey = academic_survey.rename(columns={'Name of the paper or project': 'paper_title'})
applied_survey = applied_survey.rename(columns={'Title of the paper or project': 'paper_title'})

# Combine both streams
evaluator_survey = pd.concat([academic_survey, applied_survey], ignore_index=True)

# Only export PUBLIC-SAFE columns - exclude confidential comments, COI info, and evaluator codes
public_columns = [
  'paper_title',
  # 'Code' excluded - evaluator pseudonyms kept private
  'How long have you been in this field?',
  'How many proposals, papers, and projects have you evaluated/reviewed (for journals, grants, or other peer-review)?',
  'Approximately how long did you spend completing this evaluation?',
  'How would you rate this template and process?',
  'Would you be willing to consider evaluating a revised version of this work?',
  'Do you have any other suggestions or questions about this process or The Unjournal? (We will try to respond, and incorporate your suggestions.)',
  'Field/expertise',
  'research_link_coda',
  'status',
  'Date entered (includes transfer from PubPub)',
  'hours_spent_manual_impute'
]

# Filter to only include columns that exist in the dataframe
available_columns = [col for col in public_columns if col in evaluator_survey.columns]
evaluator_survey = evaluator_survey[available_columns]
evaluator_survey.to_csv("data/evaluator_survey_responses.csv", index = False)
