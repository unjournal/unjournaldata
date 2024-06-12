
# functions to look for publication outcomes in different databases

library(httr2)
library(glue)
library(purrr)

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
  
  journals <- c(journal_scopus, journal_semantic, journal_pubmed)
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
