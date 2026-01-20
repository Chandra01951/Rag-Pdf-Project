from fastapi import APIRouter
from app.schemas.chat import ChatRequest, ChatResponse
from app.rag.retriever import retrieve_context
from app.rag.prompt import build_prompt
from app.rag.llm import get_llm

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    question = request.question

    # Retrieve context from FAISS
    context = retrieve_context(question)

    if not context:
        return ChatResponse(answer="No relevant context found. Please upload a PDF first.")

    # Build prompt
    prompt = build_prompt(context, question)

    # Generate answer using LLaMA
    llm = get_llm()
    answer = llm(prompt)

    return ChatResponse(answer=answer)