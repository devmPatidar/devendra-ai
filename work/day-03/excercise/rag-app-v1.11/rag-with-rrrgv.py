import chromadb
from chromadb.utils import embedding_functions
from sentence_transformers import CrossEncoder
from groq import Groq
import re



# ---------------- CONFIG ---------------- #
CHROMA_PATH = "./chroma_db"
COLLECTION_NAME = "medical_docs"
MODEL = "llama-3.1-8b-instant"

# ---------------- GROQ CLIENT ---------------- #
groq_path = r"E:\Lenovo Ideapad 330\company-material\digital-workforce-transformation\ai-upskill-11\key-vault\groq\api.key"

with open(groq_path, "r") as f:
    api_key = f.read().strip()

llm_client = Groq(api_key=api_key)

# ---------------- EMBEDDING FUNCTION ---------------- #
embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

# ---------------- LOAD CHROMA ---------------- #
client = chromadb.PersistentClient(path=CHROMA_PATH)

collection = client.get_collection(
    name=COLLECTION_NAME,
    embedding_function=embedding_function
)

# ---------------- QUERY REWRITE ---------------- #
def rewrite_query(query):
    prompt = f"""
    Rewrite: {query}
    Return only the rewritten query without any additional text.
    """

    response = llm_client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
        max_tokens=100
    )

    return response.choices[0].message.content.strip()


# ---------------- RETRIEVAL ---------------- #
def retrieve(query, k=8):
    results = collection.query(
        query_texts=[query],
        n_results=k
    )

    docs = results.get("documents", [[]])[0]

    # Convert to LangChain-like format
    return [{"page_content": d} for d in docs]


# ---------------- RERANK ---------------- #
cross_encoder = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")

def rerank(query, docs):
    pairs = [[query, doc["page_content"]] for doc in docs]
    scores = cross_encoder.predict(pairs)

    ranked = sorted(zip(docs, scores), key=lambda x: x[1], reverse=True)

    return [doc for doc, _ in ranked[:10]]


# ---------------- GENERATE ---------------- #
def generate_answer(query, docs):
    context = "\n".join([d["page_content"] for d in docs])

    prompt = f"""
Use the context to answer the question.

Context:
{context}

Question:
{query}

Answer in bullet points:
"""

    response = llm_client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        max_tokens=200
    )

    return response.choices[0].message.content.strip(), context


# ---------------- VALIDATE ---------------- #
def extract_score(text):
    match = re.search(r"\d*\.?\d+", text)
    return float(match.group()) if match else 0.0


def validate_answer(query, answer, context):
    prompt = f"""
Score the answer from 0 to 1 based on correctness using context.

Return ONLY a number.

Question: {query}
Context: {context}
Answer: {answer}
"""

    response = llm_client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
        max_tokens=10
    )

    return extract_score(response.choices[0].message.content)


# ---------------- MAIN ---------------- #
def ask(query):

    if collection.count() == 0:
        return {"error": "Chroma DB is empty. Run ingest.py first."}

    print("----------------------------------------------------------")
    print("\n\n-- RAG with RRRGV Pipeline ---\n")
    # 1. Rewrite
    rewritten = rewrite_query(query)
    print("🔁 Rewritten:", rewritten)

    # 2. Retrieve
    docs = retrieve(rewritten)
    print(f"Documents retrieved: {len(docs)}")

    # 3. Rerank
    docs = rerank(rewritten, docs)
    print(f"Documents after reranking: {docs}")

    print("\n🔍 Top Docs:")
    for i, d in enumerate(docs, 1):
        print(f"{i}. {d['page_content'][:120]}...")

    # 4. Generate
    answer, context = generate_answer(query, docs)
    print("\n💡 Answer:\n", answer)
    print("\n📚 Used Context:\n", context)

    # 5. Validate
    score = validate_answer(query, answer, context)
    print(f"\n✅ Validation Score: {score:.2f}")

    print("----------------------------------------------------------")

    return {
        "answer": answer,
    }


# ---------------- TEST ---------------- #
if __name__ == "__main__":
    info = ask("What are the symptoms of diabetes?")
    print(info['answer'])