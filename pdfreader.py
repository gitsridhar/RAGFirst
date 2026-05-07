import os
from pypdf import PdfReader

def read_pdf(file_path):
    if not os.path.isfile(file_path):
        print(f"File {file_path} does not exist.")
        # return None
        raise FileNotFoundError(f"File {file_path} does not exist.")

    #try:
    #    reader = PdfReader(file_path)
    #    text = ""
    #    for page in reader.pages:
    #        text += page.extract_text() + "\n"
    #    return text
    #except Exception as e:
    #    print(f"An error occurred while reading the PDF: {e}")
    #    return None
    
    reader = PdfReader(file_path)
    pages = [page.extract_text() for page in reader.pages]
    return pages
