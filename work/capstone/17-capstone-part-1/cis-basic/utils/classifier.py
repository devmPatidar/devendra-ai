def classify_query(query: str) -> str:
    query = query.lower()

    if "summarize" in query or "summary" in query:
        return "summary"
    elif "audit" in query or "check" in query:
        return "audit"
    elif "recommend" in query or "improve" in query:
        return "recommendation"
    else:
        return "general"