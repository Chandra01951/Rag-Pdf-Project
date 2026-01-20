def build_prompt(context: str, question: str) -> str:
    """
    Create prompt with retrieved context
    """
    prompt = f"""
You are a helpful assistant.
Answer the question using ONLY the context below.
If the answer is not in the context, say "I don't know".

Context:
{context}

Question:
{question}

Answer:
"""
    return prompt