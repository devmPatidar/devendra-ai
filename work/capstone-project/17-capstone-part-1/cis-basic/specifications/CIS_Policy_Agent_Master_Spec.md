# 🧠 CIS Policy Intelligence Assistant
## 📘 Master Project Specification Document (Assessment Submission)

---

## 🎯 1. Project Overview

### 📌 Title  
**CIS Policy Intelligence Assistant using RAG (Retrieval-Augmented Generation)**

### 🧾 Description  
This project implements an intelligent command-line agent that interacts with CIS benchmark documents (e.g., Windows 11 Enterprise Benchmark) to:

- Answer security-related queries  
- Extract relevant CIS controls  
- Summarize policies  
- Provide actionable security recommendations  

The system uses a **RAG pipeline** enhanced with **semantic chunking**, **memory**, and **query classification**.

---

## 🎯 2. Objectives

- Build a working RAG-based AI system  
- Enable intelligent querying of CIS policy documents  
- Improve retrieval quality using semantic chunking  
- Provide structured, reliable responses  
- Demonstrate agentic capabilities (memory + reasoning)  

---

## 🏗️ 3. System Architecture

```
User Query
   ↓
Query Classifier
   ↓
Retriever (FAISS Vector DB)
   ↓
Context Injection
   ↓
LLM (Reasoning Engine)
   ↓
Response Formatter (Rich CLI)
   ↓
Memory + Logging
```

---

## 🧩 4. Core Components

### 4.1 Document Ingestion
- Loads CIS PDF  
- Applies semantic chunking  
- Generates embeddings  
- Stores in vector database  

---

### 4.2 Semantic Chunking
- Splits document based on CIS control IDs  
- Preserves complete control sections  
- Improves retrieval accuracy  

---

### 4.3 Retrieval System
- Uses FAISS  
- Performs similarity search  
- Returns top-k relevant chunks  

---

### 4.4 Agent Layer
- Combines retrieved context + user query  
- Uses LLM for reasoning  
- Produces structured output  

---

### 4.5 Memory Module
- Stores recent interactions  
- Enables conversational continuity  

---

### 4.6 Query Classification
- Summary  
- Audit  
- Recommendation  
- General  

---

### 4.7 Output Formatting
- Rich CLI formatting  
- Structured readable output  

---

## 📁 5. Directory Structure

```
cis_policy_agent/
│
├── data/
├── ingestion/
├── retrieval/
├── agents/
├── utils/
├── vectorstore/
├── main.py
└── .env
```

---

## ⚙️ 6. Technology Stack

- Python  
- LangChain  
- OpenAI API  
- FAISS  
- Rich  

---

## 🔄 7. Workflow

1. Ingestion → Chunk + Embed + Store  
2. Retrieval → Fetch relevant chunks  
3. Agent → Generate structured response  
4. Enhancement → Memory + Save outputs  

---

## 🧪 8. Testing Strategy

- Password policy queries  
- Audit queries  
- Summary queries  
- Recommendation queries  

Evaluation:
- Accuracy  
- Completeness  
- Relevance  
- Structure  

---

## 📊 9. Key Features

- RAG pipeline  
- Semantic chunking  
- Structured responses  
- Memory  
- Logging  
- CLI interface  

---

## ⚠️ 10. Challenges & Solutions

- Broken chunks → semantic chunking  
- Hallucination → strict prompt  
- Retrieval noise → better chunking  

---

## 🚀 11. Future Enhancements

- Hybrid search  
- LangGraph agents  
- RAG evaluation  
- UI layer  

---

## 🧠 12. Key Insight

RAG quality depends heavily on chunking quality.

---

## 🏁 13. Conclusion

This project demonstrates a practical AI system capable of:
- Understanding CIS policies  
- Retrieving relevant controls  
- Generating intelligent responses  

---

## 📎 14. References

- CIS Benchmarks  
- LangChain Docs  
- FAISS  
- OpenAI API  

---

## 🎓 Submission Note

Demonstrates:
- RAG system design  
- Agentic workflows  
- Applied AI engineering  
