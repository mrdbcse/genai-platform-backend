from fastapi import APIRouter
from fastapi.responses import JSONResponse
from src.app.handler.med_bot.prompt import chat_prompt
from src.app.handler.med_bot.retriever import create_index, doc_retriever
from src.app.helper.med_bot.helper import filter_to_minimal_docs, load_pdf, split_text
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from src.app.schema.med_bot import Chat

router = APIRouter(prefix="/api/medical_assistant", tags=["Medical Chatbot"])
index_name = "medical_assistant"
file_path = "data\medical\Current Essentials of Medicine.pdf"

document = load_pdf(file_path=file_path)
minimal_docs = filter_to_minimal_docs(docs=document)
chunks = split_text(minimal_docs=minimal_docs)

create_index(index_name=index_name)


llm = ChatOpenAI(model="gpt-4o")
prompt = chat_prompt()
retriever = doc_retriever(index_name=index_name, chunks=chunks)

document_chain = create_stuff_documents_chain(
    llm=llm, prompt=prompt, output_parser=StrOutputParser()
)
rag_chain = create_retrieval_chain(
    retriever=retriever, combine_docs_chain=document_chain
)


@router.post("/chat")
async def chat(body: Chat):
    print(f"{body=}")
    response = rag_chain.invoke({"input": body.message})
    print(response)
    return JSONResponse(content={"answer": response["answer"]})
