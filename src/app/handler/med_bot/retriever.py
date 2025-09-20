from typing import List

from src.app.helper.med_bot.helper import load_api_keys
from langchain.schema import Document
from langchain_core.vectorstores.base import VectorStoreRetriever
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone, ServerlessSpec

pc = Pinecone()

load_api_keys()


def create_index(index_name: str) -> None:
    try:
        if not pc.has_index(index_name):
            pc.create_index(
                name=index_name,
                dimension=1536,
                metric="cosine",
                spec=ServerlessSpec(cloud="aws", region="us-east-1"),
            )
            print("Index created successfully")
            index = pc.Index(name=index_name)
            print("Index Name: ", index)
        print("Index exists")
    except Exception as e:
        print("Exception: ", e)


def doc_retriever(
    chunks: List[Document], index_name: str = None
) -> VectorStoreRetriever:
    try:
        return PineconeVectorStore.from_documents(
            documents=chunks, embedding=OpenAIEmbeddings(), index_name=index_name
        ).as_retriever(search_type="similarity", search_kwargs={"k": 3})
    except Exception as e:
        print("Exception: ", e)
