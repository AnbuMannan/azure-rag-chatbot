# Azure RAG Chatbot (Retrieval-Augmented Generation)

An end-to-end Retrieval-Augmented Generation (RAG) chatbot built using **Azure OpenAI**, **Azure AI Search**, and **Azure Document Intelligence**.

This project demonstrates how to ground Large Language Model (LLM) responses in enterprise data to prevent hallucinations.

---

## 🔹 Architecture

User Query  
→ Embeddings (Azure OpenAI)  
→ Vector Search (Azure AI Search)  
→ Relevant Context  
→ GPT-4o (Azure OpenAI)  
→ Grounded Answer  

---

## 🔹 Technologies Used

- Azure OpenAI (GPT-4o, text-embedding-3-small)
- Azure AI Search (Vector Index, HNSW)
- Azure AI Foundry (Model deployments)
- Azure Document Intelligence (OCR – optional)
- Python

---

## 🔹 Features

- Vector-based semantic search
- Hallucination-free answers
- Manual text ingestion
- Modular & extensible design
- AI-102 (Azure AI Engineer Associate) aligned

---

## 🔹 Project Structure

rag-chatbot/
├── create_index.py
├── ingest_docs.py
├── chat.py
├── ocr_pdf.py
├── requirements.txt
├── .env.example
└── README.md


---

## 🔹 How to Run

1. Clone the repository
2. Create `.env` from `.env.example`
3. Install dependencies:
```bash
pip install -r requirements.txt

4.Create vector index:
python create_index.py

5.Ingest documents:
python ingest_docs.py

6. Start Chat
python chat.py

🔹 Sample Questions

How many casual leaves are allowed?
What are office working hours?
Is work from home allowed?

🔹 Interview Highlights

Uses VectorizedQuery (latest Azure SDK)
Separate embedding and chat deployments
Azure AI Foundry-based deployment workflow
Cost-aware architecture

📌 Author

Anbalagan Mannan
Azure AI Engineer | .NET Developer