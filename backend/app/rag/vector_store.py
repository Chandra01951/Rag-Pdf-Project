import os
from langchain.vectorstores import FAISS
from app.rag.embeddings import get_embedding_model

FAISS_PATH = "app/data/faiss_index"


def create_faiss_index(chunks: list[str]):
    """
    Create and persist FAISS index from text chunks
    """
    embeddings = get_embedding_model()

    vector_store = FAISS.from_texts(
        texts=chunks,
        embedding=embeddings
    )

    os.makedirs(FAISS_PATH, exist_ok=True)
    vector_store.save_local(FAISS_PATH)

    return vector_store


def load_faiss_index():
    """
    Load FAISS index from disk
    """
    embeddings = get_embedding_model()

    if not os.path.exists(FAISS_PATH):
        return None

    vector_store = FAISS.load_local(
        FAISS_PATH,
        embeddings
    )

    return vector_store
