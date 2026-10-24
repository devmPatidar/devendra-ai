
# from sentence_transformers import SentenceTransformer
# import chromadb
# from chromadb.config import Settings

# model = SentenceTransformer("all-MiniLM-L6-v2")

# client = chromadb.Client(Settings(persist_directory="./chroma_db"))
# collection = client.get_or_create_collection("medical_docs")

# def search(query, k=5):
#     emb = model.encode([query]).tolist()
#     results = collection.query(query_embeddings=emb, n_results=k)
#     print("Retrieved documents:\n", results["documents"][0])
#     return results["documents"][0]

# if __name__ == "__main__":
#     query = "What are the symptoms of diabetes?"
#     search(query)


import chromadb
from chromadb.utils import embedding_functions

# ---------------- CONFIG ---------------- #
CHROMA_PATH = "./chroma_db"
COLLECTION_NAME = "medical_docs"

# ---------------- EMBEDDING FUNCTION ---------------- #
embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

# ---------------- LOAD CLIENT ---------------- #
client = chromadb.PersistentClient(path=CHROMA_PATH)

collection = client.get_collection(
    name=COLLECTION_NAME,
    embedding_function=embedding_function
)

# ---------------- SEARCH FUNCTION ---------------- #
def search(query, k=5):
    results = collection.query(
        query_texts=[query],
        n_results=k
    )

    docs = results.get("documents", [[]])[0]

    if not docs:
        print("⚠️ No documents retrieved. Check ingestion.")
        return []

    print("\n🔍 Retrieved documents:\n")
    for i, doc in enumerate(docs, 1):
        print(f"{i}. {doc[:200]}...\n")

    return docs


# ---------------- MAIN ---------------- #
if __name__ == "__main__":
    query = "What are the symptoms of diabetes?"
    search(query)