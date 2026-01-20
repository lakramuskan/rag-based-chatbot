import os
import hashlib
from langchain_community.document_loaders import PDFPlumberLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS

PDF_DIR = "pdfs"
DB_DIR = "vectorstore/db_faiss"
EMBEDDING_MODEL = "nomic-embed-text"

os.makedirs(PDF_DIR, exist_ok=True)

def file_hash(file):
    return hashlib.md5(file.getbuffer()).hexdigest()

def save_pdf(file):
    path = os.path.join(PDF_DIR, file.name)
    with open(path, "wb") as f:
        f.write(file.getbuffer())
    return path

def load_pdf(path):
    loader = PDFPlumberLoader(path)
    return loader.load()

def create_chunks(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1500,
        chunk_overlap=100
    )
    return splitter.split_documents(documents)

def get_embeddings():
    return OllamaEmbeddings(model=EMBEDDING_MODEL)

def add_pdf_to_vectorstore(file):
    if file is None:
        return "⚠ No file uploaded"

    file_id = file_hash(file)
    marker = f"{PDF_DIR}/{file_id}.done"

    if os.path.exists(marker):
        return "⚡ PDF already indexed"

    path = save_pdf(file)
    docs = load_pdf(path)
    chunks = create_chunks(docs)
    embeddings = get_embeddings()

    if os.path.exists(DB_DIR):
        db = FAISS.load_local(DB_DIR, embeddings, allow_dangerous_deserialization=True)
        db.add_documents(chunks)
    else:
        db = FAISS.from_documents(chunks, embeddings)

    db.save_local(DB_DIR)
    open(marker, "w").close()

    return "✅ PDF indexed successfully"
    