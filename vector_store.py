from pathlib import Path

from langchain_chroma import Chroma

from config import CHROMA_DB_DIR


def vector_store_exists() -> bool:
    """
    Check if a persisted Chroma database already exists.
    """

    db_path = Path(CHROMA_DB_DIR)

    return (
        db_path.exists()
        and (db_path / "chroma.sqlite3").exists()
    )


def create_vector_store(chunks, embedding_model):
    """
    Create and persist a Chroma vector database.
    """

    return Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=str(CHROMA_DB_DIR)
    )


def load_vector_store(embedding_model):
    """
    Load an existing Chroma vector database.
    """

    return Chroma(
        persist_directory=str(CHROMA_DB_DIR),
        embedding_function=embedding_model
    )

def get_retriever(vector_store, k: int = 4):
    """
    Create a retriever from the vector store.

    Args:
        vector_store: Chroma vector database
        k: Number of document chunks to retrieve.

    Returns:
        LangChain retriever.
    """

    return vector_store.as_retriever(
        search_kwargs={"k": k}
    )