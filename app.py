# Main program

from vector_store import create_vector_store
from embeddings import get_embedding_model
from splitter import split_documents
from loader import load_pdf
from utils import get_pdf_files

from config import DOCUMENTS_DIR

pdf_files = get_pdf_files(str(DOCUMENTS_DIR))

print("Loading embedding model...")
embedding_model = get_embedding_model()
print("Embedding model loaded.\n")

all_chunks = []

print(f"Found {len(pdf_files)} PDF(s).\n")

for pdf in pdf_files:

    print(f"Processing {pdf.name}...")

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

print("\nVector store created successfully.")
print("Embeddings generated and stored in ChromaDB.")