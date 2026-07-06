# Main program

from embeddings import get_embedding_model
from splitter import split_documents
from loader import load_pdf
from utils import get_pdf_files

PDF_FOLDER = "documents/research_papers"

pdf_files = get_pdf_files(PDF_FOLDER)

embedding_model = get_embedding_model()

print("Embedding Model Loaded Successfully!\n")

for pdf in pdf_files:

    documents = load_pdf(pdf)

    chunks = split_documents(documents)

    print(f"{pdf.name}")
    print(f"Pages  : {len(documents)}")
    print(f"Chunks : {len(chunks)}")

    print("-" * 60)