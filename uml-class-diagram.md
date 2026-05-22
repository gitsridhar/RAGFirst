# UML Class Diagram

This project is organized as a small set of module-level services rather than traditional OOP classes. The diagram below models each module as a UML class facade so the relationships in the pipeline are easy to read.

PlantUML source: [uml-class-diagram.puml](uml-class-diagram.puml)
Rendered SVG: [uml-class-diagram.svg](uml-class-diagram.svg)

```mermaid
classDiagram
    class MainPipeline {
        +pdf_path: str
        +main()
    }

    class QueryProcessor {
        +process_user_query(query)
    }

    class PDFReader {
        +read_pdf(file_path)
    }

    class Chunker {
        +chunk_pages(pages, chunk_size, chunk_overlap)
    }

    class Embedder {
        +embed_chunks(chunks)
        +embed_query(query)
    }

    class VectorStore {
        +store_in_pinecone(chunks, embeddings, namespace)
        +search_pinecone(query_embedding, top_k, namespace)
    }

    class LLMService {
        +query_llm_with_context(query, context)
    }

    class OpenAI
    class Pinecone
    class PdfReader

    MainPipeline ..> PDFReader : reads
    MainPipeline ..> Chunker : chunks
    MainPipeline ..> Embedder : embeds
    MainPipeline ..> VectorStore : stores

    QueryProcessor ..> Embedder : embeds query
    QueryProcessor ..> VectorStore : searches
    QueryProcessor ..> LLMService : generates answer

    PDFReader ..> PdfReader : parses PDF
    Embedder ..> OpenAI : embeddings client
    LLMService ..> OpenAI : chat client
    VectorStore ..> Pinecone : vector index client
```
