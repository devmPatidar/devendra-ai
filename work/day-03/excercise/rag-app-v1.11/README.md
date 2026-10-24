
# Medical RAG Assistant using ChromaDB

R -> Re-write
R -> Retrieve
R -> Re-rank
G -> Generate
V -> Validate


## Overview

This project demonstrates a **production-style Retrieval Augmented Generation (RAG) system** using a medical knowledge dataset.

The dataset contains **2000 medical entries** including:

- symptoms
- diagnosis
- treatment
- prevention

Example questions the system can answer:

- What is the course of treatment for type-2 diabetes?
- What are the symptoms of high blood pressure?
- How is asthma diagnosed?
- What lifestyle changes help manage hypertension?

## Architecture

User Question
↓
Embedding Model
↓
ChromaDB Vector Search
↓
Relevant Medical Context
↓
Prompt Construction
↓
LLM Response

## Setup

Install dependencies:

```
pip install -r requirements.txt
```

## Ingest Dataset

```
python ingest_upgraded.py
```

## Run API

```
uvicorn api:app --reload
```

Open:

```
http://localhost:8000/ask?q=What are the symptoms of high blood pressure?
```

## Files

medical_knowledge_dataset.docx → dataset  
ingest.py → loads data into ChromaDB  
retrieval.py → semantic search  
rag_pipeline.py → RAG logic  
api.py → FastAPI server  

# Cross - Encoder Re-Ranker

A cross-encoder reranker is a powerful neural network used in search and Retrieval-Augmented Generation (RAG) systems to precisely evaluate how relevant a document is to a user's query. It dramatically boosts search precision by jointly analyzing the query and candidate documents side-by-side. 


How It Works: Cross-Encoders vs. Bi-Encoders
Most standard vector databases use Bi-Encoders (like Dense Passage Retrievers). A Bi-Encoder processes the query and documents completely independently, allowing you to pre-compute vectors and search through millions of records extremely fast. However, because they never look at the query and document together during the initial search, they can miss subtle context and relationships. 



A Cross-Encoder takes the user query and a retrieved document chunk, and feeds them both together as a single input into a transformer model (e.g., a variant of BERT or RoBERTa). Because the model's self-attention layers can process every word in the query against every word in the document simultaneously, it delivers an incredibly accurate relevance score (usually between 0 and 1). 



The Two-Stage Retrieval Pipeline
Because running a cross-encoder against an entire database is computationally expensive and slow, systems rely on a "two-stage funnel" to balance speed and accuracy: 

Stage 1 (Retrieval): The system uses a fast Bi-Encoder (or keyword search like BM25) to quickly filter millions of documents down to a top-20 or top-50 list.
Stage 2 (Reranking): The Cross-Encoder reranker steps in to deeply analyze only those 20-50 candidates. It rescores them based on their exact semantic relationship to the query and reorders them to elevate the absolute best results to the top. 


Why Use Rerankers in RAG?
Adding a cross-encoder is a proven way to drastically reduce model hallucinations in RAG systems. 

Increased Precision: Typical improvements show a 10% to 25% increase in precision, effectively bringing the most useful documents to rank 1.
Contextual Nuance: Excellent for handling ambiguous, multi-turn, or highly specific queries (e.g., in medical or legal domains).
Better Utilization: Feeds the Large Language Model (LLM) the most accurate information possible to ground its final generated response. 


Popular Frameworks and Models
If you want to implement a reranker in your pipeline, several libraries and hosted APIs offer ready-to-use models:
Hugging Face / Sentence-Transformers: The go-to open-source option for deploying cross-encoders locally. Popular models include cross-encoder/ms-marco-MiniLM-L-6-v2. You can easily run them using the CrossEncoder class.
Cohere: Offers highly optimized hosted reranking models (e.g., rerank-english-v3.0 or rerank-multilingual-v3.0) accessed via their API.
Mixedbread (mxbai): Provides popular state-of-the-art open-source reranker models. 