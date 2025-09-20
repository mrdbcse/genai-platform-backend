from langchain.prompts import ChatPromptTemplate


system_prompt = "\n".join(
    [
        "You are an medical assistant for question answering task",
        "Use the following pieces of retrieved context to answer the question",
        "If you don't know the answer, just say that you don't know",
        "Use three sentences maximum and keep the answer concise.",
        "\n\n",
        "{context}",
    ]
)


def chat_prompt() -> ChatPromptTemplate:
    return ChatPromptTemplate.from_messages(
        messages=[("system", system_prompt), ("human", "{input}")]
    )
