# Main program

from embeddings import get_embedding_model
from loader import load_pdf
from rag import create_vector_store
from splitter import split_documents
from utils import get_pdf_files

PDF_FOLDER = "documents/research_papers"

pdf_files = get_pdf_files(PDF_FOLDER)

embedding_model = get_embedding_model()

all_chunks = []

for pdf in pdf_files:

    documents = load_pdf(pdf)

    chunks = split_documents(documents)

    all_chunks.extend(chunks)

    print(f"{pdf.name}")
    print(f"Pages  : {len(documents)}")
    print(f"Chunks : {len(chunks)}")
    print("-" * 60)

print(f"\nTotal Chunks: {len(all_chunks)}")

vector_store = create_vector_store(
    all_chunks,
    embedding_model
)

print("\nVector Store Created Successfully!")