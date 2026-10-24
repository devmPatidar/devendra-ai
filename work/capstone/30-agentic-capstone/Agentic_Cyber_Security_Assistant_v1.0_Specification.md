# Agentic Cyber Security Assistant v1.0

## Project Specification

## Overview

**Objective:** Build a multi-agent cybersecurity assistant using
LangChain, LangGraph, Pinecone RAG, and the NVD CVE API.

## Technology Stack

-   Python
-   LangChain
-   LangGraph
-   Pinecone
-   OpenAI/Groq
-   NVD CVE API

## Architecture

``` text
User
 │
 ▼
Planner Agent
 │
 ▼
Retrieval Agent (CIS RAG)
 │
 ▼
Threat Intelligence Agent (NVD)
 │
 ▼
Validation Agent
 │
 ▼
Final Response
```

## Agents

### Planner Agent

-   Analyze user intent
-   Create execution plan

### Retrieval Agent

-   Uses `ask_cis()`
-   Retrieves CIS benchmark guidance

### Threat Intelligence Agent

-   Uses `lookup_cve()`
-   Retrieves CVE information

### Validation Agent

-   Merges retrieved evidence
-   Produces final response

## Tools

### ask_cis()

Queries the Pinecone index `cyber-security` using namespace
`cis_documents`.

### lookup_cve()

Queries the NVD CVE API using keyword search.

## Workflow

``` text
START
 ↓
Planner
 ↓
Retrieval
 ↓
Threat
 ↓
Validation
 ↓
END
```

## Shared State

``` python
class CyberState(TypedDict):
    query: str
    plan: str
    rag: str
    cves: str
    final: str
```

## Sample Queries

-   How do I disable SMBv1?
-   What does CIS recommend for Windows Firewall?
-   Show latest SMB vulnerabilities.
-   How do I secure Windows SMB against recent attacks?

## Concepts Covered

-   LangChain create_agent()
-   Custom tools
-   Pinecone RAG
-   External REST APIs
-   LangGraph orchestration
-   Multi-agent collaboration

## Future Enhancements

-   Conditional routing
-   Parallel execution
-   Report agent
-   CISA KEV
-   MITRE ATT&CK
-   EPSS
