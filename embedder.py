from openai import OpenAI
from dotenv import load_dotenv
import os
from typing import List

load_dotenv()

client = OpenAI(base_url='http://localhost:11434/v1', api_key='ollama')
#EMBEDDING_MODEL = 'text-embedding-3-small'
# ollama pull nomic-embed-text
EMBEDDING_MODEL = 'nomic-embed-text'

def embed_chunks(chunks: List[str]) -> List[List[float]]:
    #response = client.embeddings.create(
    #    model=EMBEDDING_MODEL,
    #    input=chunks
    #)
    #return [embedding['embedding'] for embedding in response.data] 
    embeddings = []
    for chunk in chunks:
        response = client.embeddings.create(
            model=EMBEDDING_MODEL,
            input=chunk
        )
        embeddings.append(response.data[0].embedding)
    print(f"Embedded 2:", embeddings[0][:1])
    return embeddings