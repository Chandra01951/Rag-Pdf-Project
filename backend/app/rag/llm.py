from langchain.llms import Ollama


def get_llm():
    """
    Load LLaMA/Mistral via Ollama
    """
    llm = Ollama(
        model="mistral",
        temperature=0.2
    )
    return llm