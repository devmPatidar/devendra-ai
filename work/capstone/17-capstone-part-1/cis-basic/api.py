from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from assistants.policy_agent_enhanced import build_assistant

# Initialize FastAPI
app = FastAPI(
    title="CIS Policy Intelligence API",
    version="1.0.0"
)

# Build the assistant only once at startup
assistant = build_assistant()


class QueryRequest(BaseModel):
    query: str


class QueryResponse(BaseModel):
    answer: str


@app.post("/ask", response_model=QueryResponse)
async def ask_assistant(request: QueryRequest):
    try:
        result = assistant(request.query)

        return QueryResponse(
            answer=result["answer"]
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
    

'''
uvicorn api:app 

'''