import os
import re
from functools import lru_cache
from pathlib import Path

from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from sentence_transformers import CrossEncoder

from retrieval import search

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")
MODEL = os.getenv("GROQ_MODEL", "llama-3.1-8b-instant")
RERANKER_MODEL = "cross-encoder/ms-marco-MiniLM-L-6-v2"

REWRITE_PROMPT = ChatPromptTemplate.from_messages([
    ("system", "Rewrite the user's question as a concise search query. Return only the query."),
    ("human", "{question}"),
])
ANSWER_PROMPT = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a medical information assistant. Answer using the provided context. "
        "If the context does not support an answer, say you don't know. Be concise and use bullets. "
        "Do not present this as a substitute for professional medical advice.",
    ),
    ("human", "Context:\n{context}\n\nQuestion: {question}"),
])
VALIDATE_PROMPT = ChatPromptTemplate.from_messages([
    ("system", "Score how well the answer is supported by the context from 0 to 1. Return only a number."),
    ("human", "Question: {question}\nContext: {context}\nAnswer: {answer}"),
])


@lru_cache(maxsize=1)
def get_llm():
    if not os.getenv("GROQ_API_KEY"):
        raise RuntimeError("GROQ_API_KEY is not set. Add it to the environment or the project's .env file.")
    return ChatGroq(model=MODEL, temperature=0.2, max_tokens=300)


@lru_cache(maxsize=1)
def get_reranker():
    return CrossEncoder(RERANKER_MODEL)


def rewrite_query(question: str) -> str:
    chain = REWRITE_PROMPT | get_llm() | StrOutputParser()
    return chain.invoke({"question": question}).strip() or question


def rerank(query, documents, limit=5):
    if len(documents) < 2:
        return documents[:limit]
    scores = get_reranker().predict([[query, doc.page_content] for doc in documents])
    return [doc for doc, _ in sorted(zip(documents, scores), key=lambda item: item[1], reverse=True)[:limit]]


def generate_answer(question, documents):
    context = "\n\n".join(doc.page_content for doc in documents)
    chain = ANSWER_PROMPT | get_llm() | StrOutputParser()
    return chain.invoke({"question": question, "context": context}), context


def validate_answer(question, answer, context):
    chain = VALIDATE_PROMPT | get_llm() | StrOutputParser()
    result = chain.invoke({"question": question, "answer": answer, "context": context})
    match = re.search(r"(?:0(?:\.\d+)?|1(?:\.0+)?)", result)
    return min(1.0, max(0.0, float(match.group()))) if match else 0.0


def ask(question: str):
    if not question or not question.strip():
        return {"error": "Question cannot be empty."}

    try:
        docs = search(question, k=8)
        if not docs:
            return {"answer": "I don't know", "validation_score": 0.0}

        rewritten = rewrite_query(question)
        docs = search(rewritten, k=8) or docs
        docs = rerank(rewritten, docs)
        answer, context = generate_answer(question, docs)
        score = validate_answer(question, answer, context)
        return {"answer": answer, "validation_score": score}
    except Exception as exc:
        return {"error": str(exc)}


if __name__ == "__main__":
    print(ask("What are the symptoms of diabetes?"))