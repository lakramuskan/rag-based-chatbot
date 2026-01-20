from langchain_groq import ChatGroq
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

# ================= CONFIG =================
DB_DIR = "vectorstore/db_faiss"
EMBEDDING_MODEL = "nomic-embed-text"

llm_model = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

# ================= LOAD VECTOR DB =================
def load_faiss_db():
    embeddings = OllamaEmbeddings(model=EMBEDDING_MODEL)
    db = FAISS.load_local(
        DB_DIR,
        embeddings,
        allow_dangerous_deserialization=True
    )
    return db

# ================= RETRIEVE DOCS =================
def retrieve_docs(query):
    db = load_faiss_db()
    return db.similarity_search(query, k=4)

def get_context(documents):
    return "\n\n".join(doc.page_content for doc in documents)

# ================= PROMPT =================
custom_prompt_template = """
Use the pieces of information provided in the context to answer the user's question.
If you don't know the answer, just say that you don't know.
Do not make up answers.
Only use the given context.

Question: {question}
Context: {context}
Answer:
"""

# ================= ANSWER =================
def answer_query(query):
    documents = retrieve_docs(query)
    context = get_context(documents)

    prompt = ChatPromptTemplate.from_template(custom_prompt_template)
    chain = prompt | llm_model

    response = chain.invoke({
        "question": query,
        "context": context
    })

    return response.content
