from app.rag.vector_store import load_faiss_index

def retrieve_context(query: str, k: int = 4) -> str:
    """
    Retrieve relevant chunks from FAISS
    """
    vector_store = load_faiss_index()

    if vector_store is None:
        return ""

    docs = vector_store.similarity_search(query, k=k)

    context = "\n\n".join([doc.page_content for doc in docs])
    return context