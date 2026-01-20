import streamlit as st
from vector_database import add_pdf_to_vectorstore
from rag_pipeline import answer_query

st.title("📄 RAG PDF Chatbot")

uploaded_file = st.file_uploader(
    "Upload a PDF file",
    type=["pdf"],
    accept_multiple_files=False
)

if uploaded_file is not None:
    with st.spinner("Indexing PDF..."):
        st.toast(add_pdf_to_vectorstore(uploaded_file))

user_query = st.text_area(
    "Ask a question",
    height=150,
    placeholder="Type your question here..."
)

if st.button("Ask Question"):
    if uploaded_file is None:
        st.warning("Please upload a PDF first.")
    elif not user_query.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking..."):
            answer = answer_query(user_query)
            st.chat_message("assistant").write(answer)
