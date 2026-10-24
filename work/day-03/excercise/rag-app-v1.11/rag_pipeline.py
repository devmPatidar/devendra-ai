from retrieval import search
from groq import Groq

# ---------------- LOAD GROQ ---------------- #
groq_path = r"C:\Users\user\Desktop\devendra-ai\work\key-vault\groq\groq-api.key"

with open(groq_path, "r") as f:
    api_key = f.read().strip()

client = Groq(api_key=api_key)
MODEL = "llama-3.1-8b-instant"

# ---------------- PROMPT ---------------- #
SYSTEM_PROMPT = """
You are a medical assistant.

Use the provided context to answer the question.

If the context contains relevant information (even partial), use it to form the answer.

Only say "I don't know" if the context is completely unrelated.

Give concise bullet points.
"""

def build_prompt(context, question):
    return f"""
Context:
{context}

Question:
{question}

Answer:
"""

# ---------------- ASK ---------------- #
def ask(question):
    docs = search(question)

    if not docs:
        return {"answer": "I don't know"}

    # 🔥 Deduplicate
    docs = list(dict.fromkeys(docs))

    # Use more diverse context
    context = "\n".join(docs[:5])

    # compressed_docs = context_compression(context)

    prompt = build_prompt(context, question)

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=200
        )

        answer = response.choices[0].message.content.strip()

        return {"answer": answer}

    except Exception as e:
        return {"error": str(e)}


# ---------------- MAIN ---------------- #
if __name__ == "__main__":
    q = "What is diabetes?"
    print(ask(q))