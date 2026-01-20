from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import upload, chat

app = FastAPI()

# ✅ CORS CONFIG (THIS FIXES YOUR ERROR)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(upload.router)
app.include_router(chat.router)