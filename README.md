# RAG PDF Chatbot

A full-stack Retrieval-Augmented Generation (RAG) chatbot that allows users to upload PDF documents and ask questions about their content using LLaMA/Mistral LLM.

## Tech Stack

### Backend
- **Framework**: FastAPI
- **LLM**: LLaMA/Mistral (via Ollama)
- **Vector Database**: FAISS
- **Embeddings**: HuggingFace sentence-transformers
- **PDF Processing**: PyPDF

### Frontend
- **Framework**: React + Vite
- **Styling**: Custom CSS
- **API Integration**: Fetch API

## Features

✅ PDF upload and processing  
✅ Text extraction and intelligent chunking  
✅ Semantic search using FAISS vector database  
✅ Context-aware responses using LLaMA  
✅ Professional chat interface  
✅ Real-time message display  

## Setup Instructions

### Prerequisites

1. **Python 3.9+**
2. **Node.js 18+**
3. **Ollama** - [Install from ollama.com](https://ollama.com)

### Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create necessary __init__.py files
touch app/__init__.py
touch app/api/__init__.py
touch app/rag/__init__.py
touch app/schemas/__init__.py
touch app/utils/__init__.py
touch app/core/__init__.py

# Create data directories
mkdir -p app/data/pdfs
mkdir -p app/data/faiss_index
```

### Install and Run Ollama

```bash
# Install Ollama (follow instructions at ollama.com)

# Pull Mistral model
ollama pull mistral

# Keep Ollama running (in a separate terminal)
ollama run mistral
```

### Run Backend

```bash
# From backend directory
uvicorn app.main:app --reload

# Backend will run on http://localhost:8000
# Swagger docs available at http://localhost:8000/docs
```

### Frontend Setup

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Run development server
npm run dev

# Frontend will run on http://localhost:5173
```

## Usage

1. **Start Ollama**: Run `ollama run mistral` in a terminal
2. **Start Backend**: Run `uvicorn app.main:app --reload` in backend directory
3. **Start Frontend**: Run `npm run dev` in frontend directory
4. **Open Browser**: Navigate to `http://localhost:5173`
5. **Upload PDF**: Click "Upload PDF" and select a PDF file
6. **Ask Questions**: Type questions about your PDF in the chat interface

## RAG Pipeline Flow

```
1. PDF Upload
   ↓
2. Text Extraction (PyPDF)
   ↓
3. Text Chunking (with overlap)
   ↓
4. Generate Embeddings (HuggingFace)
   ↓
5. Store in FAISS Vector DB
   ↓
6. User Query
   ↓
7. Query Embedding
   ↓
8. Similarity Search (FAISS)
   ↓
9. Retrieve Context
   ↓
10. Generate Prompt
    ↓
11. LLM Generation (LLaMA/Mistral)
    ↓
12. Return Answer
```

## API Endpoints

### Health Check
- **GET** `/` - Check if backend is running

### Upload PDF
- **POST** `/api/upload`
- Body: `multipart/form-data` with PDF file
- Response: Confirmation with number of chunks created

### Chat
- **POST** `/api/chat`
- Body: `{"question": "your question here"}`
- Response: `{"answer": "generated answer"}`

## Project Structure

```
rag-pdf-chatbot/
├── backend/
│   ├── app/
│   │   ├── api/          # API routes
│   │   ├── rag/          # RAG pipeline logic
│   │   ├── schemas/      # Pydantic models
│   │   ├── utils/        # Helper functions
│   │   ├── data/         # PDF storage & FAISS index
│   │   └── main.py       # FastAPI app
│   └── requirements.txt
│
└── frontend/
    ├── src/
    │   ├── components/   # React components
    │   ├── pages/        # Page components
    │   ├── services/     # API calls
    │   └── styles/       # CSS files
    └── package.json
```

## Interview Talking Points

1. **RAG Architecture**: "I implemented a RAG system that combines retrieval from a vector database with generative AI to provide accurate, context-grounded answers."

2. **Vector Search**: "I used FAISS for efficient similarity search and HuggingFace embeddings for semantic understanding."

3. **Chunking Strategy**: "I implemented recursive chunking with overlap to preserve context across chunk boundaries."

4. **LLM Integration**: "I integrated an open-source LLaMA model via Ollama to keep the solution free and locally deployable."

5. **Full-Stack**: "I built a complete full-stack application with FastAPI backend and React frontend, ensuring clean separation of concerns."

6. **Production Practices**: "The code follows production best practices with proper error handling, schema validation, and CORS configuration."

## Troubleshooting

### Backend Issues
- **ImportError**: Ensure all `__init__.py` files are created in directories
- **Module not found**: Check virtual environment is activated
- **FAISS errors**: Try reinstalling with `pip install faiss-cpu --force-reinstall`

### Frontend Issues
- **CORS errors**: Ensure backend CORS middleware is configured
- **API connection failed**: Verify backend is running on port 8000
- **Build errors**: Delete `node_modules` and run `npm install` again

### Ollama Issues
- **Model not found**: Run `ollama pull mistral`
- **Connection refused**: Ensure Ollama is running with `ollama run mistral`
- **Slow responses**: First query may be slow due to model loading

## Future Enhancements

- [ ] Multi-PDF support
- [ ] Chat history persistence
- [ ] User authentication
- [ ] Document source citations
- [ ] Export chat conversations
- [ ] Deployment to cloud platforms

## License

MIT License