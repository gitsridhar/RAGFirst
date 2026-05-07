from typing import List, Tuple

def chunk_pages(pages: List[str], chunk_size: int = 900, chunk_overlap: int = 150) -> List[str]:
    """
    Chunks the pages into smaller pieces based on the specified chunk size.

    Args:
        pages (List[str]): A list of page texts.
        chunk_size (int): The maximum number of characters in each chunk.
        chunk_overlap (int): The number of characters to overlap between chunks.

    Returns:
        List[Tuple[str, int]]: A list of tuples containing the chunk text and its corresponding page number.
    
    chunks = []
    for page_number, page in enumerate(pages):
        start = 0
        while start < len(page):
            end = min(start + chunk_size, len(page))
            chunk_text = page[start:end]
            chunks.append((chunk_text, page_number))
            start += chunk_size
    return chunks

    chunks: List[Tuple[str, int]] = []
    for text in pages:
        start = 0
        n = len(text)
        while start < n:
            end = min(start + chunk_size, n)
            chunk_text = text[start:end]
            last_period = chunk_text.rfind(". ")
            if last_period != -1 and end < n and (last_period > chunk_size * 0.5):
                end = start + last_period + 2
                chunk_text = text[start:end]
            chunks.append(chunk_text.strip())
            start = max(end - chunk_overlap, end)
    return chunks
    """
    chunks: List[str] = []
    full_text = " ".join(pages)
    text_length = len(full_text)
    
    if text_length == 0:
        return chunks
    
    start = 0
    while start < text_length:
        end = min(start + chunk_size, text_length)
        chunk = full_text[start:end].strip()
        
        if chunk:
            chunks.append(chunk)
        print("SRIDHAR", chunk)
        
        if end >= text_length:
            break
        start = end - chunk_overlap  # Move start forward with overlap
        print("Starting new chunk from index:", start)
    return chunks