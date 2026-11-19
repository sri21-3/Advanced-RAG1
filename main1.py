
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, List
from uuid import uuid4

from langchain_core.messages import HumanMessage, AIMessage
from src.rag_pipeline import rag_chain

import logging
import traceback

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
app = FastAPI(title="Advanced RAG API", version="1.0.0")

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Restrict this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Session storage
store: Dict[str, List] = {}


# Request models
class ChatRequest(BaseModel):
    session_id: str
    question: str


class ChatResponse(BaseModel):
    session_id: str
    question: str
    answer: str


# Session management
def get_session_history(session_id):
    if session_id not in store:
        store[session_id] = []

    return store[session_id]


@app.get("/")
def home():
    return {"message": "Advanced RAG API is running"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/session")
def create_session():
    session_id = str(uuid4())
    store[session_id] = []

    return {"session_id": session_id}


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    if not request.question.strip():
        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty"
        )

    try:
        chat_history = get_session_history(request.session_id)

        # Invoke existing RAG pipeline
        answer = rag_chain.invoke({
            "input": request.question,
            "chat_history": chat_history[-10:]
        })

        # Normalize LangChain message responses
        if hasattr(answer, "content"):
            answer = answer.content

        answer = str(answer)

        # Store conversation
        chat_history.append(
            HumanMessage(content=request.question)
        )

        chat_history.append(
            AIMessage(content=answer)
        )

        return ChatResponse(
            session_id=request.session_id,
            question=request.question,
            answer=answer
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"RAG processing failed: {str(e)}"
        )


@app.delete("/session/{session_id}")
def clear_session(session_id: str):

    if session_id not in store:
        raise HTTPException(
            status_code=404,
            detail="Session not found"
        )

    del store[session_id]

    return {"message": "Session cleared successfully"}
