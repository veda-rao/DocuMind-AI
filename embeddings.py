# Provides embedding model to Generate embeddings (sematic vectors)

from langchain_huggingface import HuggingFaceEmbeddings


def get_embedding_model():
    """
    Initialize and return the Hugging Face embedding model.
    """

    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    return embedding_model