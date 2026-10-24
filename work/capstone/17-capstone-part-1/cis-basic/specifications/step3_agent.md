# 🚀 STEP 3 — Build CIS Policy Agent

## 🎯 Objective
Combine retrieval + LLM to generate structured responses.

---

## 📁 Files
- agents/policy_agent.py
- utils/formatter.py
- main.py

---

## 🤖 Agent Code

```python
from langchain_openai import ChatOpenAI
from retrieval.retriever import get_retriever

def build_agent():
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    retriever = get_retriever()

    def run(query):
        docs = retriever.invoke(query)
        context = "\n\n".join([d.page_content for d in docs])

        prompt = f"""
Context:
{context}

Query:
{query}

Provide:
1. Answer
2. Relevant CIS Controls
3. Summary
4. Recommendations
"""

        response = llm.invoke(prompt)

        return {"query": query, "answer": response.content}

    return run
```

---

## ▶️ Run

```bash
python main.py
```

---

## ✅ Checklist
- Structured output
- Uses retrieved context
- No hallucination
