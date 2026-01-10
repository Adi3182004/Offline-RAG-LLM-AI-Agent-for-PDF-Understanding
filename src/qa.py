import numpy as np
from src.embeddings import embed_chunks
from src.vector_store import search
from src.llm import generate


def answer_question(question, chunks, index, difficulty="medium"):
    if not question.strip():
        return "Please enter a question."

    q_emb = embed_chunks([question])
    ids = search(index, np.array(q_emb), k=12)

    retrieved = [chunks[i] for i in ids[0] if i < len(chunks)]
    context = "\n".join(retrieved).strip()

    if not context:
        return "No relevant content found in the selected PDF."

    prompt = f"""
You are answering questions from official study notes or meeting minutes.

Context:
{context}

Question:
{question}

Instructions:
- The answer may be implied, not explicitly stated
- Infer intent or purpose logically if needed
- Do NOT add information not present in the notes
- Answer clearly in 1–2 sentences
- Difficulty level: {difficulty}
"""

    return generate(prompt)


def generate_mcqs(chunks, difficulty="medium"):
    if not chunks:
        return "No content available to generate MCQs."

    context = "\n".join(chunks[:20])

    prompt = f"""
Generate 5 multiple-choice questions from the following notes.
Difficulty: {difficulty}

Rules:
- Questions must be strictly based on the notes
- Each question must include marks
- Include correct answer
- Do NOT add external information

Format STRICTLY:
Q1 (2 Marks). Question?
A) option
B) option
C) option
D) option
Answer: B

Notes:
{context}
"""

    return generate(prompt)
