from embedder import embed_query
from vectorstore import search_pinecone
from llm import query_llm_with_context

def process_user_query(query):
    # Placeholder for query processing logic
    print(f"Processing query: {query}")
    # Here you would add the actual logic to handle the query
    
    # embed user's query to create vector representation
    query_vector = embed_query(query)
    
    # search the vector database to get top matching chunks related to the query
    matched_chunks = search_pinecone(query_vector)
    
    # send the user query and the search results (query + context) to LLM to generate a response
    response = query_llm_with_context(query, matched_chunks)
    print(f"LLM Response: {response}")

if __name__ == "__main__":
    user_query = "What is this?"
    process_user_query(user_query)