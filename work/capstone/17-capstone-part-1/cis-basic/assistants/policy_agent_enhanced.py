from langchain_openai import ChatOpenAI
from retrieval.retriever import get_retriever
from utils.memory import Memory
from utils.classifier import classify_query

memory = Memory()

keypath = r"C:\Users\user\Desktop\devendra-ai\work\key-vault\openai\open-ai-api.key"
with open(keypath) as f:
    api_key = f.read().strip()

def build_assistant():
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, api_key=api_key)
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