
# Functions to look for publication outcomes in different online databases.

library(dplyr)
library(glue)
library(httr2)
library(purrr)
library(tidyr)

# The contact email passed to openalex in their header. This gives us access to 
# a faster API.
openalex_email <- "contact@unjournal.org"


#' Look up journal names of possible publications
#' 
#' If multiple journals are found these functions will emit a warning
#' and return the first journal name.
#' 
#' @param title String: publication title
#' @param authors Character vector: authors
#'
#' @return A [tibble()] with columns:
#' 
#' * name of `journal` 
#' * publication `title`
#' * lookup `source`
#' 
#' @examples
#' lookup_journal("Honesty", authors = "David Hugh-Jones")
#' 
lookup_journal <- function (title, authors = character(0L)) {
  lookup_funs <- list(
    Scopus   = lookup_journal_scopus, 
    # Disabled until we get an api key:
    # `Semantic Scholar` = lookup_journal_semantic, 
    PubMed   = lookup_journal_pubmed, 
    CORE     = lookup_journal_core,
    Openalex = lookup_journal_openalex
  )
  
  journals <- map(lookup_funs, function (lookup_fun) {
    tryCatch(
      lookup_fun(title, authors),
      error = \(x) {warning(x); empty_results_tibble()}
    )
  })
  
  journals <- list_rbind(journals)
  journals <- journals %>% arrange(title, journal, source)
  
  return(journals)
}


lookup_journal_scopus <- function (title, authors = character(0L)) {
  
  if (grepl("\\(", title)) {
    warning("Removing parentheses from title in scopus lookup")
    title <- gsub("\\(.*?\\)", "", title)
  }
  # we always have AND at the end, since the last AND comes before TITLE(...).
  author_strings <- glue("AUTHOR-NAME({authors}) AND ") 
  author_string <- paste(author_strings, collapse = "")
  query <- glue("{author_string}TITLE({title})")
  
  req <- request("https://api.elsevier.com/content/search/scopus") %>% 
    req_url_query(
      apiKey = Sys.getenv("SCOPUS_API_KEY"),
      query = query
    ) %>% 
    req_retry(max_tries = 3)
  
  resp <- req_perform(req)
  search_results <- resp_body_json(resp)$"search-results"
  n_results <- as.numeric(search_results$"opensearch:totalResults")
  stopifnot(is.numeric(n_results), n_results >= 0L)
  
  results <- map(search_results$entry, \(x) {
    tibble(
      journal = x$"prism:publicationName", 
      title   = x$"dc:title",
      source  = "Scopus"
    )
  })
  
  results <- list_rbind(results)
  
  return(results)
}


lookup_journal_semantic <- function (title, authors = character(0L)) {
  req <- request("https://api.semanticscholar.org/graph/v1/paper/search") %>%
    req_headers(
      "x-api-key" = Sys.getenv("SEMANTIC_SCHOLAR_API_KEY")
    ) %>% 
    req_url_query(
      query = title,
      fields = "title,venue,journal,authors",
      publicationTypes = "journalArticle",
      limit = 10L
    ) %>% 
    req_retry(max_tries = 3)
  
  resp <- req_perform(req)
  results <- resp_body_json(resp)
  
  # semantic scholar typically returns many results
  author_and_title_matches <- function (x) {
    title_matches <- x$title == title
    if (length(authors) == 0L) return(title_matches)
    author_names <- map(x$authors, "name")
    author_matches <- any(authors %in% author_names) 
    author_matches && title_matches
  }
  
  results <- keep(results$data, author_and_title_matches)
  
  results <- tibble(
    journal = map_chr(results, "journal"),
    title = map_chr(results, "title"),
    source = "Semantic Scholar"
  )
  
  return(results)
}


lookup_journal_pubmed <- function(title, authors = character(0L)) {
  author_string <- glue("{authors}[au]")
  author_string <- paste(author_string, collapse = " AND ")
  search_term <- glue("\"{title}\"[Title] AND {author_string}")
  req <- request("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi") %>% 
    req_url_query(
      db = "pubmed",
      term = search_term,
      retmode = "json"
    ) %>% 
    req_retry(max_tries = 3)

  resp <- req_perform(req)
  res <- resp_body_json(resp)
  
  n_results <- res$esearchresult$count
  if (n_results == 0L) return(empty_results_tibble())
  
  ids <- unlist(res$esearchresult$idlist)
  
  req2 <- request("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi") %>% 
    req_url_query(
      db = "pubmed",
      id = paste(ids, collapse = ","),
      retmode = "json"
    ) %>% 
    req_retry(max_tries = 3)
  
  resp2 <- req_perform(req2)
  res2 <- resp_body_json(resp2)
  
  res2 <- res2$result
  pub_details <- res2[names(res2) %in% ids]
  
  results <- tibble(
    journal = map_chr(pub_details, "fulljournalname"),
    title   = map_chr(pub_details, "title"),
    source  = "PubMed"
  )
  
  return(results)
}


lookup_journal_core <- function (title, authors = character(0L)) {
  author_strings <- glue("authors:{authors}")
  author_string <- paste(author_strings, collapse = " ")
  search_query <- glue("{author_string} title:{title}")
  
  req <- request_core("https://api.core.ac.uk/v3/search/outputs") %>% 
    req_url_query(
      q = search_query
    ) 
  
  resp <- req_perform(req)
  
  res <- resp_body_json(resp)
  res <- res$results
  
  find_journal_name <- function (x) {
    if (is.null(x$journals)) return(NA_character_)
    map_chr(x$journals, \(jnl) {
      if (! is.null(jnl$title)) return(jnl$title)
      identifiers <- unlist(jnl$identifiers)
      issns <- grep("^issn:", identifiers, value = TRUE)
      titles <- map_chr(issns, lookup_journal_by_issn_core)
      titles <- titles[! is.na(titles)]
      if (length(titles)) return(titles[1]) else return(NA_character_)
    })
  }
  
  journal_names <- map_chr(res, find_journal_name)

  results <- tibble(
    journal = journal_names,
    title = map_chr(res, "title"),
    source = "CORE"
  )

  return(results)
}


#' Find journal title by issn using CORE
#' 
#' Often returns no result even for well-known journals
#'
#' @param issn An issn string like "issn:1832-4274" 
#'
#' @return A journal title or `NA_character_`.
#' 
#' @examples
#' lookup_journal_by_issn_core("issn:1179-1497")
lookup_journal_by_issn_core <- function (issn) {
  req <- request_core("https://api.core.ac.uk/v3/journals/") %>% 
    req_url_path_append(issn)
  resp <- tryCatch(
    req_perform(req),
    httr2_http_404 = function (err) NULL
  )
  if (is.null(resp)) return(NA_character_)
  
  res <- resp_body_json(resp)
  if (is.null(res$title)) {
    warning("No `title` field found")
    return(NA_character_)
  }
  
  return(res$title)
}


#' Return a request object suitable for talking to the core.ac.uk server
#'
#' @param url A URL
#'
#' @return A [httr2::request()] object with headers and retry strategy set.
request_core <- function(url) {
  # This function returns TRUE if the `resp`onse from the core server is 
  # telling us to slow down.
  core_is_transient <- function (resp) {
    status <- resp_status(resp)
    rate_limit_header <- resp_header(resp, "x-ratelimit-remaining")
    status == 429 && rate_limit_header == "0"
  }
  
  # This function tells us how many seconds to wait.
  core_delay <- function (resp) {
    retry_time <- resp_header(resp, "X-ratelimit-retry-after")
    retry_time <- as.POSIXct(retry_time, format="%Y-%m-%dT%H:%M:%S", tz = "UTC")
    now <- as.POSIXct(Sys.time(), tz = "UTC")
    delay <- difftime(retry_time, now, units = "secs")
    delay <- as.double(delay)
    ceiling(delay)
  }
  
  core_api_key <- Sys.getenv("CORE_API_KEY")
  
  req <- request(url) %>% 
    req_headers(
      Authorization = glue("Bearer {core_api_key}")
    ) %>% 
    req_retry(max_tries = 3L, is_transient = core_is_transient, 
              after = core_delay) 

  return(req)
}


lookup_journal_openalex <- function (title, authors = character(0L)) {
  # This is a hack because the title search doesn't like commas
  title <- gsub(",", "", title, fixed = TRUE)
  query_filter <- glue("title.search:{title}")
  
  if (length(authors) > 0L) {
    author_ids <- lookup_authors_openalex(authors)
    if (length(author_ids) > 0L) {
      authors_string <- paste(author_ids, collapse = "|")
      query_filter <- glue("{query_filter},authorships.author.id:{authors_string}")
    }
  }
  
  req <- request("https://api.openalex.org/works") %>% 
    req_headers(
      mailto = openalex_email
    ) %>% 
    req_url_query(
      filter = query_filter,
      select = "display_name,primary_location"
    ) %>% 
    req_throttle(
      rate = 5 # openalex specifies 10 per second
    )
  
  resp <- req_perform(req)
  
  res <- resp_body_json(resp)
  res <- res$results
  
  # We discard results which aren't in journals
  source_types <- map(res, c("primary_location", "source", "type"))
  null_sources <- map_lgl(source_types, is.null)
  res <- res[! null_sources]
  source_types <- source_types[! null_sources]
  res <- res[source_types == "journal"]
  
  results <- tibble(
    journal = map_chr(res, c("primary_location", "source", "display_name")),
    title   = map_chr(res, "display_name"),
    source  = "Openalex"
  )

  return(results)
}


#' Look up authors' openalex IDs by name
#'
#' @param authors Character vector
#'
#' @return A named list of openalex ids e.g. 
#' `"https://openalex.org/A5035113852"`. The names are the `display_name`s
#' as given by openalex. There may be more than one matching name per author.
#'   
lookup_authors_openalex <- function (authors) {
  author_string <- paste(authors, collapse = "|")
  
  req <- request("https://api.openalex.org/authors") %>% 
    req_headers(
      mailto = openalex_email
    ) %>% 
    req_url_query(
      filter = glue("display_name.search:{author_string}"),
      select = "id,display_name"
    ) %>% 
    req_throttle(
      rate = 5 # openalex specifies max 10 per second
    )
  
  resp <- req_perform(req)
  
  res <- resp_body_json(resp)
  
  openalex_ids <- map_chr(res$results, "id")
  display_names <- map_chr(res$results, "display_name")
  names(openalex_ids) <- display_names
  
  return(openalex_ids)
}


#' Get statistics about a journal from Scopus
#'
#' @param journal String: a single journal name.
#'
#' @return A list of journal statistics. List elements are `NA` if the journal
#'   was not found. See 
#'   <https://dev.elsevier.com/documentation/SerialTitleAPI.wadl>
lookup_stats_scopus <- function (journal) {
  req <- request("https://api.elsevier.com/content/serial/title") %>% 
    req_url_query(
      apiKey = Sys.getenv("SCOPUS_API_KEY"),
      title = journal,
      content = "journal"
    ) %>% 
    req_retry(max_tries = 3)
  
  resp <- req_perform(req)
  resp <- resp_body_json(resp)
  res <- resp$"serial-metadata-response"
  
  n_results <- length(res$entry)
  if (n_results > 1L) {
    warning(glue("More than one Scopus match for journal title '{journal}'.
                  Returning the first match."))
  }
  if (n_results < 1L) {
    return(list(snip = NA_real_, cite_score = NA_real_, sjr = NA_real_))
  }
  
  res <- res$entry[[1]]
  
  # source normalized impact per paper
  snip <- res$SNIPList$SNIP[[1]]$"$"
  snip <- as.numeric(snip)
  
  cite_score <- res$citeScoreYearInfoList$citeScoreCurrentMetric
  cite_score <- as.numeric(cite_score)
  
  sjr <- res$SJRList$SJR[[1]]$"$"
  sjr <- as.numeric(sjr)
            
  list(snip = snip, cite_score = cite_score, sjr = sjr)
}


#' Get statistics about a journal from Openalex
#'
#' @param journal String: a single journal name.
#'
#' @return A list of lists of journal statistics. The names of the list
#'   are display names according to Openalex. 
#'   <https://docs.openalex.org/api-entities/sources/source-object#summary_stats>
lookup_stats_openalex <- function (journal) {
  journal <- gsub(",", "", journal, fixed = TRUE)
  
  req <- request("https://api.openalex.org/sources") %>% 
    req_headers(
      mailto = openalex_email
    ) %>% 
    req_url_query(
      filter = glue("display_name.search:{journal}"),
      select = "display_name,summary_stats"
    ) %>% 
    req_throttle(
      rate = 5
    )
  
  resp <- req_perform(req)
  res <- resp_body_json(resp)
   
  n_results <- res$meta$count
  
  results <- res$results
  if (n_results > 1L) {
    warning(glue("More than one Openalex match for journal title '{journal}'."))
    # Trim results, if we can, to those with an exact match
    results_trimmed <- purrr::keep(results, \(x) x$display_name == journal)
    if (length(results_trimmed) > 0L) results <- results_trimmed
  }
  
  stats <- purrr::map(results, "summary_stats")
  names(stats) <- purrr::map(results, "display_name")
  return(stats)
}


#' Helper function for lookups
#'
#' @return A zero-row tibble with the correct columns
empty_results_tibble <- function () {
  tibble(
    journal = character(0L),
    title   = character(0L),
    source  = character(0L)
  )
}