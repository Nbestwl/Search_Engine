# EECS-767
Information Retrieval (Spring 2018)


## Todo lists
#### 1.Document processing and indexing
- [x] Pre-process the documents by removing all HTML tags and convert everything into lower case.
- [x] Implement a stop list and a stemmer to pre-process the documents
- [x] Build an inverted index (including dictionary and posting lists) for the documents(Please make sure to keep all the frequency information)

#### 2.Vector Space model
- [x] 1.calculate the length of the corresponding doc vector for each doc
- [x] 2.pre-process the query and calc the length of query vector
- [x] 3.compute the tf-idf similarity scores


#### 3.Niche crawler
- [ ] a multi-threaded spider that fetches and parses webpages
- [ ] the URL frontier which stores to-be-crawled URLs
- [ ] the URL repository that stores crawled URLs

#### 4.Implement a simple UI
###### Please feed the collected documents to the search engine that you implemented in step 2. Please implement a Web-based interface to take user queries and return answers (document names, snapshot with search term(s) highlighted, and URL) to the user. You only need to provide a reasonable (not so fancy) interface, you can use WYSIWYG editors to generate HTML. Keep this version of your search engine, since it will be compared with two future versions.


#### 5.Add term proximity into your scoring mechanism
###### Define your own score that reflects the proximity of search terms in each document. Define your own algorithm to integrate term proximity score with the tf-idf score from step 2.

#### 6.Add one of the following to your search engine:
###### 6.1. Search personalization: use cookies to track users. Record each search and each click-through. For a new query, add a small component of the "search history" as query expansion.
###### 6.2. Relevance feedback. For each query, allow the user to identify a set of "positive" and "negative" results. Use user feedback to update the query and return new (refined) results to the user.

#### 7.Please evaluate and compare the performance of the original search engine (step 4), and the new versions (step 5 and 6).
