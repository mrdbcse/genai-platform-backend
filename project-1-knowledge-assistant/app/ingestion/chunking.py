from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.config import settings


def chunk_text(text: str) -> list[str]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=settings.CHUNK_SIZE, chunk_overlap=settings.CHUNK_OVERLAP
    )
    chunk = splitter.split_text(text=text)
    return chunk
