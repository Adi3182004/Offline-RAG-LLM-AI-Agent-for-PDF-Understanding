import faiss
import numpy as np
import os

def save_index(embeddings, path):
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings))
    faiss.write_index(index, path)

def load_index(path):
    return faiss.read_index(path)

def search(index, query_embedding, k=5):
    D, I = index.search(query_embedding, k)
    return I
