# 🚀 STEP 1 — Project Setup (CIS Policy Intelligence Agent)

## 🎯 Objective
Set up the project environment and prepare for document ingestion.

---

## 📁 Project Structure

```
cis_policy_agent/
│
├── data/
│   └── cis_docs/
│       └── cis_policy.pdf
│
├── ingestion/
├── retrieval/
├── agents/
├── utils/
├── vectorstore/
│
├── main.py
├── requirements.txt
└── .env
```

---

## 🧰 1. Create Project Directory

```bash
mkdir cis_policy_agent
cd cis_policy_agent

mkdir data ingestion retrieval agents utils vectorstore
mkdir data/cis_docs
```

---

## 🐍 2. Create Virtual Environment

### Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac:
```bash
python -m venv venv
source venv/bin/activate
```

---

## 📦 3. Install Dependencies

```bash
pip install --upgrade pip
pip install langchain langchain-openai faiss-cpu rich pypdf python-dotenv
```

(Optional)
```bash
pip freeze > requirements.txt
```

---

## 🔑 4. Configure API Key

Create `.env` file in root:

```
OPENAI_API_KEY=your_openai_api_key_here
```

---

## 📄 5. Add CIS Benchmark Document

Place your file here:

```
data/cis_docs/cis_policy.pdf
```

Recommended:
- CIS Microsoft Windows 11 Enterprise Benchmark v5.0.1

---

## ⚙️ 6. Verify Setup

Run Python:

```bash
python
```

Test:

```python
import os
from dotenv import load_dotenv

load_dotenv()
print(os.getenv("OPENAI_API_KEY"))
```

Expected:
- Your API key prints correctly

---

## ✅ Step 1 Checklist

- [ ] Project folders created
- [ ] Virtual environment activated
- [ ] Dependencies installed
- [ ] `.env` file configured
- [ ] CIS PDF placed correctly
- [ ] API key accessible in Python

---

## ⏭️ Next Step

Proceed to **Step 2: Retrieval Setup and Testing**
