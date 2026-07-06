# Helper functions
from pathlib import Path


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