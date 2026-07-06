# Main program
from loader import load_pdf
from splitter import split_documents
from utils import get_pdf_files

PDF_FOLDER = "documents/research_papers"

pdf_files = get_pdf_files(PDF_FOLDER)

for pdf in pdf_files:

    documents = load_pdf(pdf)

    chunks = split_documents(documents)

    print(f"\n{pdf.name}")

    print(f"Pages  : {len(documents)}")

    print(f"Chunks : {len(chunks)}")

    print("\nFirst Chunk:\n")

    print(chunks[0].page_content)

    print("\nMetadata:")

    print(chunks[0].metadata)

    print("-" * 70)