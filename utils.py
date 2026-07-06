from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document


def get_pdf_files(folder_path: str) -> list[Path]:
    """
    Return all PDF files inside the specified folder.
    """

    folder = Path(folder_path)

    if not folder.exists():
        raise FileNotFoundError(
            f"Folder '{folder}' does not exist."
        )

    return sorted(folder.glob("*.pdf"))


def load_pdf(pdf_path: Path) -> list[Document]:
    """
    Load a PDF using LangChain's PyPDFLoader.

    Args:
        pdf_path: Path to the PDF file.

    Returns:
        List of LangChain Document objects (one per page).
    """

    if not pdf_path.exists():
        raise FileNotFoundError(
            f"PDF '{pdf_path}' does not exist."
        )

    loader = PyPDFLoader(str(pdf_path))

    return loader.load()