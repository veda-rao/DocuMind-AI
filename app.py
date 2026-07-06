# Main program

from vector_store import (
    create_vector_store,
    load_vector_store,
    vector_store_exists,
    get_retriever,
)
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

if vector_store_exists():

    print("\nExisting vector store found.")
    print("Loading ChromaDB...")

    vector_store = load_vector_store(
        embedding_model
    )

else:

    print("\nNo vector store found.")
    print("Creating a new vector store...")

    vector_store = create_vector_store(
        all_chunks,
        embedding_model
    )

print("\nDocuMind AI is ready!")

retriever = get_retriever(vector_store)
print("Retriever initialized successfully!")

# Testing:
question = "What is Multi-Head Attention?"
print(f"\nQuestion: {question}\n")

results = retriever.invoke(question)
print(f"Retrieved {len(results)} chunk(s):\n")

for index, document in enumerate(results, start=1):
    print(f"Chunk {index}")
    print("-" * 60)
    print(document.page_content[:500])
    print(f"\nMetadata: {document.metadata}")
    print("=" * 60)