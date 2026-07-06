from utils import get_pdf_files, load_pdf

PDF_FOLDER = "documents/research_papers"

pdf_files = get_pdf_files(PDF_FOLDER)

print("\nAvailable PDFs\n")

for pdf in pdf_files:
    print(f"📄 {pdf.name}")

print("\nLoading PDFs...\n")

for pdf in pdf_files:

    documents = load_pdf(pdf)

    print(f"Loaded: {pdf.name}")
    print(f"Pages: {len(documents)}")

    print("\nFirst Page Preview:\n")

    print(documents[0].page_content[:500])

    print("\nMetadata:")

    print(documents[0].metadata)

    print("-" * 60)