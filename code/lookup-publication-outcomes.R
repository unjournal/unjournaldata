
# functions to look for publication outcomes in different databases

library(httr2)
library(glue)
library(purrr)

#' Get statistics about a journal from Scopus
#'
#' @param journal String: a single journal name.
#'
#' @return A list of journal statistics.
lookup_stats_scopus <- function (journal) {
  req <- request("https://api.elsevier.com/content/serial/title") %>% 
    req_url_query(
      apiKey = Sys.getenv("SCOPUS_API_KEY"),
      title = journal,
      content = "journal"
    ) 
  
  resp <- req_perform(req)
  resp <- resp_body_json(resp)
  res <- resp$"serial-metadata-response"
  
  n_results <- length(res$entry)
  if (n_results > 1L) {
    warning(glue("More than one match for journal title '{journal}'"))
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

#' Look up journal names of possible publications
#' 
#' If multiple journals are found these functions will emit a warning
#' and return the first journal name.
#'
#' @param authors Character vector: authors
#' @param title String: publication title
#'
#' @return A single journal name, or `NULL` if no journal was found
lookup_journal <- function (authors, title) {
  journal_scopus <- tryCatch(
    lookup_journal_scopus(authors, title),
    error = \(x) {warning(x); NULL}
  )
  journal_semantic <- tryCatch(
    lookup_journal_semantic(authors, title),
    error = \(x) {warning(x); NULL}
  )
  journal_pubmed <- tryCatch(
    lookup_journal_pubmed(authors, title),
    error = \(x) {warning(x); NULL}
  )
  journal_core <- tryCatch(
    lookup_journal_core(authors, title),
    error = \(x) {warning(x); NULL}
  )
  
  journals <- c(journal_scopus, journal_semantic, journal_pubmed, journal_core)
  journals <- unique(journals)
  
  if (length(journals) > 1L) {
    warning(glue("More than one match across databases for {title}"))
  }
  
  return(journals[1])
}


lookup_journal_scopus <- function (authors, title) {
  
  author_strings <- glue("AUTHOR-NAME({authors})")
  author_string <- paste(author_strings, collapse = " AND ")
  query <- glue("{author_string} AND TITLE({title})")
  
  req <- request("https://api.elsevier.com/content/search/scopus") %>% 
    req_url_query(
      apiKey = Sys.getenv("SCOPUS_API_KEY"),
      query = query
    ) 
  
  resp <- req_perform(req)
  search_results <- resp_body_json(resp)$"search-results"
  n_results <- as.numeric(search_results$"opensearch:totalResults")
  stopifnot(is.numeric(n_results), n_results >= 0L)
  
  if (n_results == 0L) {
    return(NULL)
  } else if (n_results > 0L) {
    if (n_results != 1L) {
      warning(glue("More than one match in scopus for {title}"))
    }
    journal_name <- search_results$entry[[1]]$"prism:publicationName"
    if (is.null(journal_name)) {
      stop("'prism:publicationName' not found in scopus result")
    }
    return(journal_name)
  }
}

lookup_journal_semantic <- function (authors, title) {
  req <- request("https://api.semanticscholar.org/graph/v1/paper/search") %>%
    req_headers(
      "x-api-key" = Sys.getenv("SEMANTIC_SCHOLAR_API_KEY")
    ) %>% 
    req_url_query(
      query = title,
      fields = "title,venue,journal,authors",
      publicationTypes = "journalArticle",
      limit = 10L
    )
  
  resp <- req_perform(req)
  resp <- resp_body_json(resp)
  
  # semantic scholar typically returns many results
  
  author_and_title_matches <- function (x) {
    author_names <- map(x$authors, "name")
    any(authors %in% author_names) &&
    x$title == title
  }
  
  results <- keep(resp$data, author_and_title_matches)
  
  journals <- map(results, "journal")
  journals <- compact(journals)
  journals <- unique(journals)
  
  if (length(journals) > 1L) {
    warning("Found more than one distinct journal in semantic scholar")
  }
  if (length(journals) == 0L) return(NULL)
  return(journals[1])
}


lookup_journal_pubmed <- function(authors, title) {
  author_string <- glue("{authors}[au]")
  author_string <- paste(author_string, collapse = " AND ")
  search_term <- glue("\"{title}\"[Title] AND {author_string}")
  req <- request("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi") %>% 
    req_url_query(
      db = "pubmed",
      term = search_term,
      retmode = "json"
    )

  resp <- req_perform(req)
  res <- resp_body_json(resp)
  
  n_results <- res$esearchresult$count
  if (n_results == 0L) return(NULL)
  
  ids <- unlist(res$esearchresult$idlist)
  
  req2 <- request("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi") %>% 
    req_url_query(
      db = "pubmed",
      id = paste(ids, collapse = ","),
      retmode = "json"
    )
  
  resp2 <- req_perform(req2)
  res2 <- resp_body_json(resp2)
  
  res2 <- res2$result
  pub_details <- res2[names(res2) %in% ids]
  
  journals <- map_chr(pub_details, "fulljournalname")
  journals <- unique(journals)
  journals <- journals[journals != ""]
  
  n_journals <- length(journals)
  if (n_journals > 1L) {
    warning("Found more than one distinct journal in Pubmed")
  }
  
  if (n_journals == 0L) {
    return(NULL)
  } else {
    return(journals[1])
  }
}


lookup_journal_core <- function (authors, title) {
  core_api_key <- Sys.getenv("CORE_API_KEY")
  author_strings <- glue("authors:{authors}")
  author_string <- paste(author_strings, collapse = " ")
  search_query <- glue("{author_string} title:{title}")
  
  req <- request("https://api.core.ac.uk/v3/search/outputs") %>% 
    req_headers(
      Authorization = glue("Bearer {core_api_key}")
    ) %>% 
    req_url_query(
      q = search_query
    )
  
  resp <- req_perform(req)
  
  res <- resp_body_json(resp)
  res <- res$results
  journals <- map(res, "journals") %>% 
    list_flatten() %>% 
    map("title") %>% 
    compact() %>% 
    unlist() %>% 
    unique()
  
  if (length(journals) > 1L) {
    warning("Found more than one distinct journal in core")
  }
  
  if (length(journals) == 0L) {
    return(NULL)
  } else {
    return(journals[1])
  }
}
