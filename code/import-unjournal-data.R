
# standalone script to create data frame of unjournal reviews
# currently uses airtable. In future could use pubpub API.

# Currently creates 4 R variables:
# - evals_pub: data frame of our evaluations
# - all_papers_p: data frame of all papers considered: shareable data
# - all_pub_records: all papers considered, raw data. *Use with care!*
# - labels: column labels and original descriptions for evals_pub

# Environment variable AIRTABLE_API_KEY should be set to your 
# Personal Access Token; these function the same way as the old API keys.
# Your PAT needs only read access to tables and table structure.

# Beginnings of work for pubpub are now in the import-from-pubpub branch
# (but it only tries v6 for now)

library(tidyr)
library(dplyr)
library(airtabler)   
library(snakecase)
library(stringr)
library(here)
library(readr)

base_id <- "applDG6ifmUmeEJ7j" # new ID to cover "UJ - research & core members" base

pub_records <- air_select(base = base_id, table = "crucial_rsx")
all_pub_records <- pub_records
offset <- get_offset(pub_records)

# the offset is only returned while there are more records
while(! is.null(offset)) {
  pub_records <- air_select(base = base_id, table = "crucial_rsx", 
                            offset = offset)
  all_pub_records <- bind_rows(all_pub_records, pub_records)
  offset <- get_offset(pub_records)
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
           crucial_research_2,
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
  "crucial_rsx_id" = "crucial_research_2",
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
    output_eval,
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


#' Saves data created by the script to the data/ subfolder
#'
#' @return NULL
save_data <- function () {
  saveRDS(all_papers_p, file = here("data", "all_papers_p.Rdata"))
  write_csv(all_papers_p, file = here("data", "all_papers_p.csv"))
  
  saveRDS(evals_pub, file = here("data", "evals.Rdata"))
  write_csv(evals_pub, file = here("data", "evals.csv"))
  
  invisible(NULL)
}

