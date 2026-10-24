
from functools import lru_cache
from pathlib import Path

import chromadb
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

BASE_DIR = Path(__file__).resolve().parent
CHROMA_PATH = BASE_DIR / "chroma_db"
COLLECTION_NAME = "medical_docs"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"


@lru_cache(maxsize=1)
def get_vector_store():
    client = chromadb.PersistentClient(path=str(CHROMA_PATH))
    # Fail clearly if ingestion has not created the collection yet.
    client.get_collection(name=COLLECTION_NAME)
    return Chroma(
        client=client,
        collection_name=COLLECTION_NAME,
        embedding_function=HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL),
    )


def search(query: str, k: int = 5):
    """Retrieve relevant LangChain Documents from the persistent Chroma store."""
    if not query or not query.strip():
        return []
    retriever = get_vector_store().as_retriever(search_kwargs={"k": k})
    return retriever.invoke(query.strip())


if __name__ == "__main__":
    for index, document in enumerate(search("What are the symptoms of diabetes?"), 1):
        print(f"{index}. {document.page_content[:200]}...\n")