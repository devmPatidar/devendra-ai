# 🚀 Semantic Chunking Upgrade Spec  
**CIS Policy Intelligence Agent — RAG Enhancement**

---

## 🎯 Objective

Upgrade the ingestion pipeline from **character-based chunking** to **semantic chunking**, ensuring:

- Each CIS control is preserved as a complete unit  
- Improved retrieval accuracy  
- Reduced hallucination in LLM responses  

---

## 🧠 Problem with Default Chunking

### ❌ Character-Based Chunking Issues

| Problem | Impact |
|--------|--------|
| Splits mid-sentence | Broken meaning |
| Splits control sections | Loss of context |
| Poor retrieval relevance | Weak answers |
| High hallucination risk | Unreliable output |

---

## ✅ Solution: Semantic Chunking

Instead of splitting by characters, we:

👉 Detect **CIS control boundaries**  
👉 Extract **full control sections**  
👉 Store each control as a **single chunk**

---

## 📄 CIS Document Structure

```
1.1.5 Ensure 'Password must meet complexity requirements'

Description:
...

Rationale:
...

Audit:
...

Remediation:
...
```

---

## ⚙️ Implementation Overview

### Step 1: Combine Full Text

```python
full_text = "\n".join([doc.page_content for doc in documents])
```

---

### Step 2: Detect Control Boundaries

```python
pattern = r'(\d+\.\d+\.\d+.*?)((?=\n\d+\.\d+\.\d+)|$)'
matches = re.findall(pattern, text, re.DOTALL)
```

---

### Step 3: Extract Semantic Chunks

```python
chunks = [match[0].strip() for match in matches if len(match[0]) > 200]
```

---

### Step 4: Convert to Documents

```python
Document(
    page_content=chunk,
    metadata={
        "chunk_id": i,
        "control_id": control_id
    }
)
```

---

## 📁 File Structure Changes

```
utils/
 └── semantic_chunker.py

ingestion/
 └── ingest.py  (updated)
```

---

## 🧩 semantic_chunker.py

```python
import re
from langchain.schema import Document

def split_cis_controls(text):
    pattern = r'(\d+\.\d+\.\d+.*?)((?=\n\d+\.\d+\.\d+)|$)'
    matches = re.findall(pattern, text, re.DOTALL)

    return [m[0].strip() for m in matches if len(m[0]) > 200]


def create_documents(chunks):
    docs = []
    for i, chunk in enumerate(chunks):
        control_match = re.match(r'(\d+\.\d+\.\d+)', chunk)
        control_id = control_match.group(1) if control_match else "unknown"

        docs.append(
            Document(
                page_content=chunk,
                metadata={
                    "chunk_id": i,
                    "control_id": control_id
                }
            )
        )
    return docs
```

---

## 🔄 Updated Ingestion Flow

### ❌ Remove

```python
RecursiveCharacterTextSplitter
```

---

### ✅ Replace With

```python
chunks = split_cis_controls(full_text)
docs = create_documents(chunks)
```

---

## 📊 Expected Improvements

| Metric | Before | After |
|------|--------|------|
| Retrieval relevance | Medium | High |
| Context completeness | Low | High |
| LLM accuracy | Medium | High |
| Hallucination | Moderate | Low |

---

## 🧪 Validation Strategy

### Test Queries

- Password complexity requirements  
- Audit steps for logging  
- Firewall configuration CIS  

---

### Expected Behavior

- Returns **complete CIS control**
- Includes:
  - Description
  - Audit
  - Remediation

---

## ⚠️ Edge Cases

### 1. PDF Formatting Issues
- Broken lines  
- Split words  

---

### 2. Regex Misses Controls

If chunk count is too low:

```python
pattern = r'(\d+\.\d+\.\d+\s+Ensure.*?)((?=\n\d+\.\d+\.\d+)|$)'
```

---

### 3. Very Large Chunks

- Rare, but can be split further if needed

---

## 🔥 Advanced Enhancements

- Hybrid chunking (semantic + size fallback)  
- Section tagging (audit/remediation)  
- Hybrid search (BM25 + vector)  

---

## 🧠 Key Insight

> RAG quality depends heavily on chunking quality.

---

## 🏁 Final Outcome

After this upgrade:

- Structure-aware retrieval  
- Better context  
- Improved answer accuracy  
- Capstone-level implementation  

---

## 🚀 Next Steps

- Display control IDs in output  
- Add evaluation (RAGAS)  
- Improve retrieval further  
