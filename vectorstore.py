from pinecone import Pinecone
import os
from dotenv import load_dotenv
from typing import List

load_dotenv()

#pinecone_client = Pinecone(api_key=os.getenv("PINECONE_API_KEY"), environment=os.getenv("PINECONE_ENVIRONMENT"))
pinecone_client = Pinecone(api_key="XXXXX")
index = pinecone_client.Index("ragfirst-sridhar")

def store_in_pinecone(chunks: List[str], embeddings: List[List[float]], namespace: str = ""):
    vectors_to_upsert = []
    #for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
    #    vector_id = f"{namespace}_{i}"
    #    vectors_to_upsert.append((vector_id, embedding, {"text": chunk}))
    #batch_size = 100
    #for i in range(0, len(vectors_to_upsert), batch_size):
    #    batch = vectors_to_upsert[i:i + batch_size]
   #     index.upsert(vectors=batch, namespace=namespace)
    for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
        vector_data = {
            "id": f"chunk_{i}",
            "values": embedding,
            "metadata": {"text": chunk, "chunk_index": i}
        }
        vectors_to_upsert.append(vector_data)
        
    batch_size = 100
    for i in range(0, len(vectors_to_upsert), batch_size):
        batch = vectors_to_upsert[i:i + batch_size]
        index.upsert(vectors=batch, namespace=namespace)