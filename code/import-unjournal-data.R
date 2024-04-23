
# standalone script to create data frame of unjournal reviews
# currently uses airtable. In future could use pubpub API.

# Environment variable AIRTABLE_API_KEY should be set to your 
# Personal Access Token; these function the same way as the old API keys.
# Your PAT needs only read access to tables and table structure.

library(dplyr)
library(airtabler)   
library(snakecase)
library(stringr)
library(here)
library(readr)

base_id <- "applDG6ifmUmeEJ7j" # new ID to cover "UJ - research & core members" base

pub_records <- air_select(base = base_id, table = "crucial_rsx")
all_pub_records <- pub_records
# 100 is the maximum length returned
while(nrow(pub_records) == 100) {
  # Get the ID of the last record in the list
  offset <- get_offset(pub_records)
  # Fetch the next records, starting after this ID
  pub_records <- air_select(base = base_id, table = "crucial_rsx", offset =  offset)
  # Append the records to the df
  all_pub_records <- bind_rows(all_pub_records, pub_records)
}
rm(pub_records)

evals_pub <- air_get(base = base_id, "output_eval") 
colnames(evals_pub) <- snakecase::to_snake_case(colnames(evals_pub))

evals_pub <- evals_pub %>% 
  dplyr::rename(stage_of_process = stage_of_process_todo_from_crucial_research_2) %>% 
  mutate(stage_of_process = unlist(stage_of_process)) %>% 
  dplyr::filter(grepl("published", stage_of_process)) %>% 
    select(id, 
           crucial_research, 
           paper_abbrev, 
           evaluator_name, 
           category, 
           source_main, 
           author_agreement, 
           overall, 
           lb_overall, 
           ub_overall, 
           conf_index_overall, 
           advancing_knowledge_and_practice, 
           lb_advancing_knowledge_and_practice, 
           ub_advancing_knowledge_and_practice, 
           conf_index_advancing_knowledge_and_practice,
           methods_justification_reasonableness_validity_robustness,
           lb_methods_justification_reasonableness_validity_robustness,
           ub_methods_justification_reasonableness_validity_robustness,
           conf_index_methods_justification_reasonableness_validity_robustness, 
           logic_communication, lb_logic_communication, ub_logic_communication, 
           conf_index_logic_communication,
           engaging_with_real_world_impact_quantification_practice_realism_and_relevance,
           lb_engaging_with_real_world_impact_quantification_practice_realism_and_relevance,
           ub_engaging_with_real_world_impact_quantification_practice_realism_and_relevance,
           conf_index_engaging_with_real_world_impact_quantification_practice_realism_and_relevance,
           relevance_to_global_priorities, 
           lb_relevance_to_global_priorities, 
           ub_relevance_to_global_priorities, 
           conf_index_relevance_to_global_priorities, 
           journal_quality_predict, 
           lb_journal_quality_predict, 
           ub_journal_quality_predict,
           conf_index_journal_quality_predict, 
           open_collaborative_replicable, 
           conf_index_open_collaborative_replicable, 
           lb_open_collaborative_replicable, 
           ub_open_collaborative_replicable, 
           merits_journal, 
           lb_merits_journal, 
           ub_merits_journal, 
           conf_index_merits_journal)

# shorten names (before you expand into columns)
new_names <- c(
  "eval_name" = "evaluator_name",
  "cat" = "category",
  "crucial_rsx" = "crucial_research",
  "conf_overall" = "conf_index_overall",
  "adv_knowledge" = "advancing_knowledge_and_practice",
  "lb_adv_knowledge" = "lb_advancing_knowledge_and_practice",
  "ub_adv_knowledge" = "ub_advancing_knowledge_and_practice",
  "conf_adv_knowledge" = "conf_index_advancing_knowledge_and_practice",
  "methods" = "methods_justification_reasonableness_validity_robustness",
  "lb_methods" = "lb_methods_justification_reasonableness_validity_robustness",
  "ub_methods" = "ub_methods_justification_reasonableness_validity_robustness",
  "conf_methods" = "conf_index_methods_justification_reasonableness_validity_robustness",
  "logic_comms" = "logic_communication",
  "lb_logic_comms" = "lb_logic_communication",
  "ub_logic_comms" = "ub_logic_communication",
  "conf_logic_comms" = "conf_index_logic_communication",
  "real_world" = "engaging_with_real_world_impact_quantification_practice_realism_and_relevance",
  "lb_real_world" = "lb_engaging_with_real_world_impact_quantification_practice_realism_and_relevance",
  "ub_real_world" = "ub_engaging_with_real_world_impact_quantification_practice_realism_and_relevance",
  "conf_real_world" = "conf_index_engaging_with_real_world_impact_quantification_practice_realism_and_relevance",
  "gp_relevance" = "relevance_to_global_priorities",
  "lb_gp_relevance" = "lb_relevance_to_global_priorities",
  "ub_gp_relevance" = "ub_relevance_to_global_priorities",
  "conf_gp_relevance" = "conf_index_relevance_to_global_priorities",
  "journal_predict" = "journal_quality_predict",
  "lb_journal_predict" = "lb_journal_quality_predict",
  "ub_journal_predict" = "ub_journal_quality_predict",
  "conf_journal_predict" = "conf_index_journal_quality_predict",
  "open_sci" = "open_collaborative_replicable",
  "conf_open_sci" = "conf_index_open_collaborative_replicable",
  "lb_open_sci" = "lb_open_collaborative_replicable",
  "ub_open_sci" = "ub_open_collaborative_replicable",
  "conf_merits_journal" = "conf_index_merits_journal"
)

evals_pub <- evals_pub %>%
  rename(!!!new_names)

#  Create a list of labels with the old, longer names
labels <- str_replace_all(new_names, "_", " ") %>% str_to_title()


# expand categories into columns, unlist everything
evals_pub %<>%
  tidyr::unnest_wider(cat, names_sep = "_") %>% # give each of these its own col
  mutate(across(everything(), unlist))  # maybe check why some of these are lists in the first place
  
# clean the Anonymous names
evals_pub$eval_name <- ifelse(
  grepl("^\\b\\w+\\b$|\\bAnonymous\\b", evals_pub$eval_name),
  paste0("Anonymous_", seq_along(evals_pub$eval_name)),
  evals_pub$eval_name
)

# only these variables are publicly shareable
all_papers_p <- all_pub_records %>% 
  dplyr::select(
    id,
    category,
   # these columns seem no longer to exist:
   # cfdc_DR,
   # 'confidence -- user entered',
   # cfdc_assessor,
   # avg_cfdc,
    category,
    cause_cat_1_text,
    cause_cat_2_text,
    topic_subfield_text,
    eval_manager_text,
    'publication status',
    'Contacted author?',
    'stage of process/todo',
    'source_main',  
    'author permission?',
'Direct Kotahi Prize Submission?',
    'createdTime'         
  )


saveRDS(all_papers_p, file = here("data", "all_papers_p.Rdata"))
write_csv(all_papers_p, file = here("data", "all_papers_p.csv"))

saveRDS(evals_pub, file = here("data", "evals.Rdata"))
write_csv(evals_pub, file = here("data", "evals.csv"))

# Beginnings of work for pubpub:
# 
# simple access to pubpub v6 API
# function to get a collection of pubpubs
# function to get details of each pub
# 
# 
# library(httr)
# library(secretbase)
# 
# url <- "https://unjournal.pubpub.org/api/login"
# 
# password_hash <- secretbase::sha3("", bits = 512L)
# payload <- sprintf('{
# "email": "contact@unjournal.org",
# "password": "%s"
# }', password_hash)
# 
# response <- VERB("POST", url, 
#                  body = payload, 
#                  content_type("application/json"), 
#                  accept("application/json"), 
#                  encode = "json")
# 
# content(response, "text")
# 
# 
# url <- "https://www.pubpub.org/api/pubs/cashtransfersmetrics"
# 
# response <- VERB("GET", 
#                  url, 
#                  content_type("application/octet-stream"), 
#                  accept("application/json"))
# 
# content(response, "text")