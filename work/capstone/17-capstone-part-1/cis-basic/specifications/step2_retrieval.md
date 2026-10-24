# 🚀 STEP 2 — Retrieval Setup & Testing

## 🎯 Objective
Load vector database and validate retrieval quality.

---

## 📁 Files
- retrieval/retriever.py
- retrieval/test_retrieval.py

---

## 🔧 Retriever Setup

```python
from dotenv import load_dotenv
load_dotenv()

from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

def get_retriever():
    db = FAISS.load_local(
        "vectorstore/",
        OpenAIEmbeddings(),
        allow_dangerous_deserialization=True
    )
    return db.as_retriever(search_kwargs={"k": 4})
```

---

## 🧪 Test Script

```python
from retrieval.retriever import get_retriever

retriever = get_retriever()

query = "password policy requirements"
docs = retriever.invoke(query)

for i, doc in enumerate(docs, 1):
    print(f"\n--- Result {i} ---\n")
    print(doc.page_content)
```

---

## ▶️ Run

```bash
python retrieval/test_retrieval.py
```

---

## ✅ Checklist
- Vectorstore loads
- Retrieval returns relevant CIS content
- No errors
