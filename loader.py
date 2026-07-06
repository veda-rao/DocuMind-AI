# PDF loading
from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document


def load_pdf(pdf_path: Path) -> list[Document]:
    """
    Load a PDF using LangChain's PyPDFLoader.

    Args:
        pdf_path: Path to the PDF file.

    Returns:
        List of LangChain Document objects.
    """

    if not pdf_path.exists():
        raise FileNotFoundError(
            f"PDF '{pdf_path}' does not exist."
        )

    loader = PyPDFLoader(str(pdf_path))

    return loader.load()