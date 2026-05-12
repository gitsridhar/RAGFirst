This repo contains the following:
1. Code to read a pdf file, chunk it, create vectors using embedding model and store them in pinecone vector db.
2. Code to query the above mentioned injected data, going through embedding model to create vectors for the query without chunking it and search in pinecone for similar data and send both to LLM and get results.
