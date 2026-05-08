from openai import OpenAI
from dotenv import load_dotenv
import os
from typing import List

load_dotenv()

client = OpenAI(base_url='http://localhost:11434/v1', api_key='ollama')

def query_llm_with_context(query: str, context: List[str]) -> str:
    # Combine the query and context into a single prompt
    prompt = f"Context:\n{'\n'.join(context)}\n\nQuestion: {query}\nAnswer:"
    
    # Call the LLM to generate a response
    response = client.chat.completions.create(
        model="gpt-oss",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that answers questions based on the provided context."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=200,
        temperature=0.7
    )
    
    return response.choices[0].message.content.strip()