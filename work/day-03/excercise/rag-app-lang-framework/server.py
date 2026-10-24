from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from rag_pipeline import ask

app = FastAPI(
    title="RAG API",
    version="1.0"
)


class QueryRequest(BaseModel):
    query: str


@app.get("/")
def health():
    return {"status": "running"}


@app.post("/ask")
def ask_endpoint(request: QueryRequest):
    """
    Accepts a JSON request:
    {
        "query": "What are the symptoms of diabetes?"
    }

    Returns whatever the ask() function returns.
    """
    try:
        return ask(request.query)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))