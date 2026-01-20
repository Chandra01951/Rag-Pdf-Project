import os
from fastapi import UploadFile

PDF_DIR = "app/data/pdfs"

def save_pdf(file: UploadFile) -> str:
    """
    Save uploaded PDF file to disk
    """
    os.makedirs(PDF_DIR, exist_ok=True)

    file_path = os.path.join(PDF_DIR, file.filename)

    with open(file_path, "wb") as f:
        f.write(file.file.read())

    return file_path