import docx
from PyPDF2 import PdfReader


def extract_text_from_pdf(file_path: str) -> str:
    reader = PdfReader(file_path)
    return "\n".join([page.extract_text() or "" for page in reader.pages])


def extract_text_from_docx(file_path: str) -> str:
    doc = docx.Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])


def extract_text(file_path: str) -> str:
    if file_path.endswith(".pdf"):
        return extract_text_from_pdf(file_path=file_path)
    elif file_path.endswith(".docx"):
        return extract_text_from_docx(file_path=file_path)
    else:
        raise ValueError("Unsupported file format for text extraction.")
