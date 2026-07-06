# Text chunking
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document


def split_documents(documents: list[Document]) -> list[Document]:
    """
    Split LangChain Document objects into smaller chunks.
    """

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        separators=[
            "\n\n",
            "\n",
            " ",
            ""
        ]
    )

    chunks = text_splitter.split_documents(documents)

    return chunks