"""Compatibility entry point for the LangChain RRRGV RAG pipeline."""

from rag_pipeline import ask


if __name__ == "__main__":
    print(ask("What are the symptoms of diabetes?"))
