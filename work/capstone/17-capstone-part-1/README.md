### Document Stores

- Select document stores
- Create New
- Choose file loader (PDF)
- Upload file
- Choose the text splitter - Recursive Text Splitter
- Upload and test the chunks
- Click process

### Upsert into Vector DB

- Start upsert
- Choose the embedding (OpenAPI-small)
- Choose vectorstores (Pinecone)
- Visit Pinecone website
- Create an index
    - name
    - configuration (OpenAI-small)
    - Choose the chunk size (1536)
    - AWS zone
    - Create
- Create API key and use in Flowise
- Ref: 17-flowise-rag\01-vectorstore-settings.png
- Test retrieval
  
### Build the Flowise Project

- Refer 17-flowise-rag\01-complete-project.png
- Component list
    - Agent -> Tool Agent
    - Memory -> Buffer Window Memory
    - Chat Models -> Open AI
    - Tools -> Retriever Tool
    - Retrievers -> Pinecone
    - Embeddings -> OpenAI