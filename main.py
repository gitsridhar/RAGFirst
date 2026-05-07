from pdfreader import read_pdf
from chunker import chunk_pages
from embedder import embed_chunks
from vectorstore import store_in_pinecone
from typing import List

pdf_path = "./resources/ExpFile.pdf"
def main():
    # Step 1: Read PDF
    pages = read_pdf(pdf_path)
    
    # Step 2: Chunk Pages
    chunks = chunk_pages(pages, chunk_size=900, chunk_overlap=550)
    print(f"Total chunks created: {len(chunks)}")
    print("First Chunks:")
    print(chunks[0])
    #for i, chunk in enumerate(chunks):
    #    print(f"Chunk {i+1}:\n{chunk}\n{'-'*40}")
    
    # Step 3: Embed Chunks
    embeddings = embed_chunks(chunks)
    print(f"Total chunks embedded: {len(embeddings)}")
    print(f"First chunk embedding: {embeddings[0]}")
    
    # Step 4: Store in Pinecone
    store_in_pinecone(chunks, embeddings, namespace="")

if __name__ == "__main__":
    main()
