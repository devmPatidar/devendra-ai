
# Medical RAG Assistant — LangChain

This project uses LangChain for document chunking, Hugging Face embeddings, Chroma retrieval, and Groq chat-model prompt chains. A Sentence Transformers cross-encoder reranks retrieved chunks.

## Setup (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
Copy-Item .env.example .env
```

Set `GROQ_API_KEY` in `.env`. Optionally set `GROQ_MODEL`; the default is `llama-3.1-8b-instant`.

## Ingest the dataset

Keep `medical_knowledge_dataset.docx` in this folder, then run:

```powershell
python .\ingest_upgraded.py
```

The vector store is persisted in `chroma_db`. Ingestion skips an already-populated collection; remove that folder to rebuild it.

## Run the application

Start the API:

```powershell
uvicorn server:app --reload
```

In another terminal, start the Streamlit UI:

```powershell
streamlit run .\ui.py
```

The API accepts `POST /ask` with JSON such as `{"query":"What are the symptoms of diabetes?"}`. Run `python .\test-case.py` to test it.

## Main files

- `ingest_upgraded.py` — LangChain chunking, embeddings, and Chroma ingestion.
- `retrieval.py` — LangChain Chroma retriever.
- `rag_pipeline.py` — LangChain Groq prompt chains, reranking, and answer validation.
- `server.py` / `ui.py` — FastAPI endpoint and Streamlit UI.