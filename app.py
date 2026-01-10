import streamlit as st
import os
import numpy as np
from src.ocr import pdf_to_text
from src.chunker import chunk_text
from src.embeddings import embed_chunks
from src.vector_store import save_index, load_index
from src.qa import answer_question, generate_mcqs
from src.voice import record_and_transcribe
from src.export_pdf import export_mcqs_pdf

os.makedirs("data/uploaded_pdfs", exist_ok=True)
os.makedirs("data/extracted_text", exist_ok=True)
os.makedirs("data/faiss_indexes", exist_ok=True)

st.set_page_config(page_title="Offline AI Study Assistant", layout="wide")
st.title("Offline AI Study Assistant")

if "pdf_data" not in st.session_state:
    st.session_state.pdf_data = {}

if "chat_history" not in st.session_state:
    st.session_state.chat_history = {}

if "mcqs" not in st.session_state:
    st.session_state.mcqs = []

uploaded_files = st.file_uploader(
    "Upload up to 5 PDFs",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:
    for file in uploaded_files[:5]:
        base = os.path.splitext(file.name)[0]
        pdf_path = f"data/uploaded_pdfs/{file.name}"
        txt_path = f"data/extracted_text/{base}.txt"
        idx_path = f"data/faiss_indexes/{base}.index"

        with open(pdf_path, "wb") as f:
            f.write(file.getbuffer())

        if base not in st.session_state.pdf_data:
            pdf_to_text(pdf_path, txt_path)
            text = open(txt_path, encoding="utf-8").read()
            chunks = chunk_text(text)
            embeddings = embed_chunks(chunks)
            save_index(np.array(embeddings), idx_path)

            st.session_state.pdf_data[base] = {
                "chunks": chunks,
                "index": idx_path
            }
            st.session_state.chat_history[base] = []

    st.success("PDFs processed")

if st.session_state.pdf_data:
    mode = st.radio("Mode", ["Single PDF", "All PDFs"])
    difficulty = st.selectbox("Difficulty", ["easy", "medium", "hard"])

    if mode == "Single PDF":
        selected = st.selectbox(
            "Select PDF",
            list(st.session_state.pdf_data.keys())
        )
        chunks = st.session_state.pdf_data[selected]["chunks"]
        index = load_index(st.session_state.pdf_data[selected]["index"])
    else:
        chunks = []
        for p in st.session_state.pdf_data.values():
            chunks.extend(p["chunks"])
        embeddings = embed_chunks(chunks)
        temp_index = "data/faiss_indexes/all.index"
        save_index(np.array(embeddings), temp_index)
        index = load_index(temp_index)

    col1, col2 = st.columns(2)

    with col1:
        question = st.text_input("Ask a question")

    with col2:
        if st.button("🎤 Voice Input"):
            question = record_and_transcribe()
            st.success("Voice captured")

    if st.button("Get Answer"):
        if question.strip():
            answer = answer_question(question, chunks, index, difficulty)
            st.write(answer)
            if mode == "Single PDF":
                st.session_state.chat_history[selected].append((question, answer))
        else:
            st.warning("Enter a question first")

    if st.button("Generate MCQs"):
        st.session_state.mcqs = generate_mcqs(chunks, difficulty)
        st.subheader("MCQs")
        st.write(st.session_state.mcqs)

    if st.button("📄 Export MCQs as PDF"):
        if st.session_state.mcqs:
            export_mcqs_pdf(st.session_state.mcqs)
            st.success("MCQs exported as mcqs.pdf")
        else:
            st.warning("Generate MCQs first")

    # ---------- SIDEBAR (HAMBURGER MENU CONTENT) ----------
    with st.sidebar:
        st.title("☰ Menu")

        if mode == "Single PDF":
            with st.expander("💬 Chat History", expanded=False):
                if st.session_state.chat_history[selected]:
                    for q, a in st.session_state.chat_history[selected]:
                        st.markdown(f"**Q:** {q}")
                        st.markdown(f"**A:** {a}")
                        st.markdown("---")
                else:
                    st.info("No chat history yet.")
