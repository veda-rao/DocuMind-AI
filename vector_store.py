from langchain_chroma import Chroma

from config import CHROMA_DB_DIR

def create_vector_store(chunks, embedding_model):
    """
    Create and persist a Chroma vector database.
    """

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=CHROMA_DB_DIR
    )

    return vector_store


def load_vector_store(embedding_model):
    """
    Load an existing Chroma vector database.
    """

    return Chroma(
        persist_directory=CHROMA_DB_DIR,
        embedding_function=embedding_model
    )