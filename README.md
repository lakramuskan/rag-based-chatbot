
# 📚 RAG-Based Document Chat System (Ollama + LangChain + Streamlit)

This project is a **Retrieval-Augmented Generation (RAG)** application that allows users to upload documents and ask questions about their content. It uses **Ollama** for local LLM inference, **LangChain** for RAG orchestration, **OllamaEmbeddings** for semantic search, and **Streamlit** for an interactive UI. The entire system runs **offline**, ensuring data privacy and full local control.

---

## 🚀 Features

* Upload and chat with PDF documents
* Accurate, context-aware answers using RAG
* Local LLM inference with Ollama
* Semantic search using Ollama embeddings
* Vector database for fast retrieval
* Simple and clean Streamlit interface
* Fully offline and privacy-friendly

---

## 🧠 How It Works

1. User uploads a document (PDF)
2. Text is extracted and split into chunks
3. Chunks are converted into embeddings using OllamaEmbeddings
4. Embeddings are stored in a vector database
5. User asks a question
6. Relevant document chunks are retrieved
7. Ollama LLM generates an answer based on retrieved context

---

## 🛠️ Tech Stack

* **Python**
* **Ollama** (LLM + Embeddings)
* **LangChain**
* **Streamlit**
* **Vector Database** (Chroma / FAISS)

---

## 📂 Project Structure

```
RAG-BASED-MODEL/
│
├── frontend.py            # Streamlit UI
├── rag_pipeline.py        # RAG logic
├── vector_database.py     # Vector DB handling
├── requirements.txt
├── pdfs/                  # Uploaded documents
├── vectorstore/           # Stored embeddings
├── .env
└── venv/
```

---

## ⚙️ Installation & Setup

### 1️⃣ Install Ollama

Download and install Ollama:

```
https://ollama.com/download
```

Pull required models:

```bash
ollama pull llama3
ollama pull nomic-embed-text
```

---

### 2️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/rag-based-model.git
cd rag-based-model
```

---

### 3️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

---

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 5️⃣ Run the Application

```bash
streamlit run frontend.py
```

---

## 📌 Use Cases

* Research paper analysis
* Academic study assistant
* Legal document Q&A
* Internal knowledge base
* Private AI document assistant

---

## 🔮 Future Enhancements

* Support for DOCX, TXT, CSV files
* Multi-document chat
* Source citations for answers
* Chat history and memory
* Hybrid retrieval (keyword + vector)
* RAG performance optimization

---

## 🔐 Privacy & Security

* Runs completely offline
* No cloud APIs used
* Documents never leave the local machine



Just say the word — you’ve done enough today ❤️
