
# Beginnings of work for pubpub:
# 
# simple access to pubpub v6 API
# function to get a collection of pubpubs
# function to get details of each pub
# 
# 


library(httr)
library(secretbase)

# login ====

url <- "https://unjournal.pubpub.org/api/login"
password <- Sys.getenv("PUBPUB_PASSWORD")
password_hash <- secretbase::keccak(password, bits = 512L)
payload <- sprintf('{
"email": "contact@unjournal.org",
"password": "%s"
}', password_hash)

response <- VERB("POST", url,
                 body = payload,
                 content_type("application/json"),
                 accept("application/json"),
                 encode = "json")

pubpub_cookies <- cookies(response)


# get collection ====
# 


url <- "https://www.pubpub.org/api/pubs/cashtransfersmetrics"

response <- VERB("GET",
                 url,
                 content_type("application/octet-stream"),
                 accept("application/json"))

content(response, "text")


