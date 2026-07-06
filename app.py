# Main program

from config import DOCUMENTS_DIR
from embeddings import get_embedding_model
from llm import generate_response
from loader import load_pdf
from prompts import RAG_PROMPT
from splitter import split_documents
from utils import get_pdf_files
from vector_store import (
    create_vector_store,
    get_retriever,
    load_vector_store,
    vector_store_exists,
)

def build_vector_store(embedding_model):
    """
    Load an existing vector store if available.
    Otherwise create a new one.
    """

    if vector_store_exists():
        print("\nExisting vector store found.")
        print("Loading ChromaDB...")

        return load_vector_store(embedding_model)

    print("\nNo vector store found.")
    print("Creating a new vector store...\n")

    pdf_files = get_pdf_files(str(DOCUMENTS_DIR))

    print(f"Found {len(pdf_files)} PDF(s).\n")

    all_chunks = []

    for pdf in pdf_files:

        print(f"Processing {pdf.name}...")

        documents = load_pdf(pdf)
        chunks = split_documents(documents)

        all_chunks.extend(chunks)

        print(f"Pages  : {len(documents)}")
        print(f"Chunks : {len(chunks)}")
        print("-" * 60)

    print(f"\nTotal Chunks: {len(all_chunks)}")

    return create_vector_store(
        all_chunks,
        embedding_model,
    )


def ask_question(retriever):
    """
    Ask questions until the user exits.
    """

    while True:

        question = input("\nAsk a question (type 'exit' to quit): ")

        if question.lower() == "exit":
            print("\nGoodbye!")
            break

        documents = retriever.invoke(question)

        context = "\n\n".join(
            doc.page_content
            for doc in documents
        )

        prompt = RAG_PROMPT.format(
            context=context,
            question=question,
        )

        answer = generate_response(prompt)

        print("\n" + "=" * 80)
        print("Answer:\n")
        print(answer)
        print("=" * 80)


def main():

    print("Loading embedding model...")

    embedding_model = get_embedding_model()

    print("Embedding model loaded.")

    vector_store = build_vector_store(
        embedding_model
    )

    print("\nDocuMind AI is ready!")

    retriever = get_retriever(vector_store)

    print("Retriever initialized successfully!")

    ask_question(retriever)


if __name__ == "__main__":
    main()