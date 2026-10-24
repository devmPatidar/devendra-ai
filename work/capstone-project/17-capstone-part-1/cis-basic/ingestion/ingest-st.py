import os
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

# Load environment variables
load_dotenv()

def ingest():
    print("\n📄 Loading CIS document...")

    loader = PyPDFLoader(
        r"C:\Users\user\Desktop\devendra-ai\work\capstone-project\17-capstone-part-1\cis-basic\data\cis_docs\CIS_Microsoft_Windows_11_Enterprise_Benchmark_v5.0.1.pdf"
    )

    documents = loader.load()

    print(f"✅ Loaded {len(documents)} pages")

    # Split into chunks
    print("\n✂️ Splitting into chunks...")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(documents)

    print(f"✅ Created {len(chunks)} chunks")

    # Create embeddings
    print("\n🧠 Generating embeddings...")

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2" # Embedding model from Hugging Face
    )

    # Create vector store
    print("\n📦 Storing in FAISS vector DB...")

    db = FAISS.from_documents(chunks, embeddings)

    # Save locally
    db.save_local("vectorstore")

    print("\n🎉 Ingestion complete! Vector store saved.")

if __name__ == "__main__":
    ingest()