from langchain_groq import ChatGroq

from retrieval.retriever import get_retriever
from utils.memory import Memory
from utils.classifier import classify_query

memory = Memory()

GROQ_KEY_PATH = r"C:\Users\user\Desktop\devendra-ai\work\key-vault\groq\groq-api.key"


def build_assistant():
    with open(GROQ_KEY_PATH) as key_file:
        api_key = key_file.read().strip()

    llm = ChatGroq(
        model="openai/gpt-oss-20b",
        temperature=0,
        api_key=api_key,
    )
    retriever = get_retriever()

    def run(query):
        query_type = classify_query(query)

        docs = retriever.invoke(query)
        context = "\n\n".join([doc.page_content for doc in docs])

        memory_context = memory.get_context()

        prompt = f"""
You are a CIS Policy Intelligence Agent.

Query Type: {query_type}

Conversation History:
{memory_context}

Context:
{context}

User Query:
{query}

Instructions:
- Adapt response based on query type:
    * summary → concise explanation
    * audit → verification steps
    * recommendation → actionable steps
    * general → structured answer

Respond in format:

1. Answer
2. Relevant CIS Controls
3. Summary
4. Recommendations

Rules:
- Use only context
- If not found, say "Not found in CIS document"
"""

        response = llm.invoke(prompt)

        memory.add(query, response.content)

        return {
            "query": query,
            "answer": response.content,
            "source_docs": docs,
            "type": query_type
        }

    return run