# 🚀 STEP 4 — Memory, Classification & Persistence

## 🎯 Objective
Enhance agent with memory, query classification, and saving outputs.

---

## 📁 Files
- utils/memory.py
- utils/classifier.py
- utils/saver.py

---

## 🧠 Memory

```python
from collections import deque

class Memory:
    def __init__(self):
        self.history = deque(maxlen=5)

    def add(self, q, r):
        self.history.append((q, r))

    def get(self):
        return "\n".join([f"Q: {q}\nA: {r}" for q, r in self.history])
```

---

## 🔍 Classifier

```python
def classify_query(q):
    q = q.lower()
    if "audit" in q:
        return "audit"
    elif "recommend" in q:
        return "recommendation"
    elif "summarize" in q:
        return "summary"
    return "general"
```

---

## 💾 Save Output

```python
def save_response(q, r):
    with open("outputs.txt", "a") as f:
        f.write(f"\nQ: {q}\nA: {r}\n")
```

---

## ▶️ Run

```bash
python main.py
```

---

## ✅ Checklist
- Memory works
- Query type adapts response
- Outputs saved
