from fastapi import APIRouter, UploadFile, File, HTTPException
from app.utils.file_utils import save_pdf
from app.schemas.upload import UploadResponse
from app.rag.loader import extract_text_from_pdf
from app.rag.chunker import chunk_text
from app.rag.vector_store import create_faiss_index

router = APIRouter()

@router.post("/upload", response_model=UploadResponse)
async def upload_pdf(file: UploadFile = File(...)):
    # Validate file type
    if not file.filename.endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed"
        )

    # Save PDF
    file_path = save_pdf(file)

    # Extract text
    extracted_text = extract_text_from_pdf(file_path)

    if not extracted_text.strip():
        raise HTTPException(
            status_code=400,
            detail="No text extracted from PDF"
        )

    # Chunk text
    chunks = chunk_text(extracted_text)

    if not chunks:
        raise HTTPException(
            status_code=400,
            detail="Chunking failed"
        )

    # Create FAISS index
    create_faiss_index(chunks)

    return UploadResponse(
        filename=file.filename,
        message=f"PDF processed and indexed successfully ({len(chunks)} chunks)"
    )