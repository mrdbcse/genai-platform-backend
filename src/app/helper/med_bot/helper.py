import os
from typing import List

from dotenv import load_dotenv
from langchain.document_loaders import PyPDFLoader
from langchain.schema import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()


def load_api_keys() -> None:
    os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
    os.environ["PINECONE_API_KEY"] = os.getenv("PINECONE_API_KEY")


def load_pdf(file_path: str) -> List[Document]:
    try:
        print("PDF file loaded")
        return PyPDFLoader(file_path=file_path).load()
    except Exception as e:
        print("Exception: ", e)


def filter_to_minimal_docs(docs: List[Document]) -> List[Document]:
    minimal_docs: List[Document] = []

    try:

        for doc in docs:
            source = doc.metadata.get("source")
            total_pages = doc.metadata.get("total_pages")
            page_label = doc.metadata.get("page_label")
            page = doc.metadata.get("page")

            minimal_docs.append(
                Document(
                    metadata={
                        "source": source,
                        "total_pages": total_pages,
                        "page_label": page_label,
                        "page": page,
                    },
                    page_content=doc.page_content,
                )
            )

        print("Document filter done")

        return minimal_docs
    except Exception as e:
        print("Exception: ", e)


def split_text(minimal_docs: List[Document]) -> List[Document]:
    try:
        print("Split text")
        return RecursiveCharacterTextSplitter(
            chunk_size=500, chunk_overlap=20
        ).split_documents(documents=minimal_docs)
    except Exception as e:
        print("Exception: ", e)
