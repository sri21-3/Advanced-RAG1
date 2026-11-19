# Advanced RAG – Company Policy AI Assistant

An AI-powered conversational assistant built using **Retrieval-Augmented Generation (RAG)** to answer questions based on company policy documents.

The application uses **Groq API with the `openai/oss-20b` model** as the LLM, **FAISS** for vector storage and similarity search, **FastAPI** for backend API development, and **Streamlit** for the interactive frontend.

Users can ask questions about company policies and receive context-aware answers grounded in the provided PDF document.

## 🚀 Project Overview

This project implements an end-to-end RAG pipeline that allows users to interact with company policy documents through a conversational interface.

The system uses `company_policy.pdf` as its knowledge source. The PDF content is processed, converted into embeddings, and stored in a FAISS vector database.

When a user submits a question:

1. The system identifies the user's intent.
2. Relevant document chunks are retrieved from FAISS when required.
3. Retrieved context is passed to the Groq LLM.
4. The LLM generates a response grounded in the retrieved document content.
5. Conversation history is maintained to support contextual follow-up questions.

The application supports document-based queries, conversation history, greetings, and simple general interactions.

## 🏗️ System Architecture

```text
              USER
                |
                v
        STREAMLIT FRONTEND
                |
                v
          FASTAPI BACKEND
             main1.py
                |
                v
        INTENT CLASSIFICATION
                |
       +--------+---------+
       |        |         |
       v        v         v
    DOCUMENT  HISTORY   GENERAL
       |        |         |
       v        v         v
    FAISS    Chat       General
   Retrieval History   Response
       |
       v
  RETRIEVED CONTEXT
       |
       v
    GROQ LLM
  openai/oss-20b
       |
       v
   AI RESPONSE
       |
       v
 STREAMLIT FRONTEND
```

## 🛠️ Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| LLM Provider | Groq API |
| LLM Model | `openai/oss-20b` |
| RAG Framework | LangChain |
| Embeddings | LangChain Embeddings |
| Vector Database | FAISS |
| Backend Framework | FastAPI |
| Frontend Framework | Streamlit |
| Document Source | PDF |
| API Communication | HTTP / REST API |

## 📂 Project Structure

```text
Advanced-RAG1/
│
├── data/
│   └── company_policy.pdf
│
├── frontend/
│   └── Streamlit application files
│
├── src/
│   ├── __init__.py
│   ├── chains.py
│   ├── config.py
│   ├── prompts.py
│   └── rag_pipeline.py
│
├── vectorstore/
│   ├── index.faiss
│   └── index.pkl
│
├── .vscode/
│
├── ingest.py
├── main.py
├── main1.py
│
├── requirements.txt
└── README.md
```

### File Description

| File / Directory | Description |
|---|---|
| `data/` | Contains the source PDF document. |
| `frontend/` | Contains the Streamlit frontend application. |
| `src/` | Contains the modular RAG implementation. |
| `chains.py` | Handles LangChain chain configurations. |
| `config.py` | Contains project configurations. |
| `prompts.py` | Defines system prompts for intent classification, contextualization, document answering, history, and general conversation. |
| `rag_pipeline.py` | Implements the core RAG pipeline. |
| `vectorstore/` | Stores the FAISS index and associated metadata. |
| `ingest.py` | Processes PDF documents and creates embeddings for vector storage. |
| `main.py` | Runs the RAG application locally through the terminal. |
| `main1.py` | Runs the FastAPI backend and exposes endpoints for frontend communication. |
| `requirements.txt` | Contains Python project dependencies. |

## ⚙️ RAG Workflow

### 1. Document Ingestion

The source document `company_policy.pdf` is processed to extract its textual content.

The extracted text is divided into smaller chunks to improve retrieval accuracy.

### 2. Embedding Generation

Document chunks are converted into vector embeddings using the configured embedding model.

### 3. FAISS Vector Storage

The generated embeddings are stored in a FAISS vector database.

The vectorstore contains:

- `index.faiss` – Stores the vector index.
- `index.pkl` – Stores associated document information and metadata.

### 4. User Query Processing

When a user submits a question, the intent classification component identifies the query category:

- **DOCUMENT:** Questions requiring information from company policy documents.
- **HISTORY:** Questions about previous user queries and AI responses.
- **GENERAL:** Greetings, small talk, and simple conversational interactions.

### 5. Context Retrieval and Answer Generation

For document-related questions, the system retrieves relevant chunks from FAISS and passes them to the Groq LLM.

The LLM generates an answer using the retrieved document context.

### 6. Conversational Memory

Conversation history is used to understand follow-up questions and maintain conversational context.

## 🔌 Backend – FastAPI

The backend is implemented using FastAPI.

The application is defined in `main1.py` and exposes an API endpoint that allows the Streamlit frontend to communicate with the RAG pipeline.

Responsibilities:

- Accept user queries through HTTP requests.
- Process queries using the RAG pipeline.
- Manage intent-based routing.
- Generate responses using the Groq API.
- Return AI-generated responses to the frontend.

## 🖥️ Frontend – Streamlit

The frontend is developed using Streamlit.

It provides a conversational interface where users can:

- Submit questions about company policies.
- Receive AI-generated answers.
- Ask contextual follow-up questions.
- Interact with the assistant through a chat interface.

The Streamlit application communicates with the FastAPI backend through HTTP API requests.

## 🔧 Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/sri21-3/Advanced-RAG1
cd Advanced-RAG1
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Groq API Key

Create a `.env` file in the project root and configure your Groq API key.

```env
GROQ_API_KEY=your_groq_api_key
```

Never commit API keys or other sensitive credentials to GitHub.

### 5. Run Document Ingestion

To process the PDF and generate the FAISS vectorstore:

```bash
python ingest.py
```

Ensure the source PDF is available in the configured data directory.

### 6. Run the Application Locally

To execute the RAG application directly through the terminal:

```bash
python main.py
```

### 7. Start the FastAPI Backend

Run the FastAPI application using Uvicorn:

```bash
uvicorn main1:app --reload
```

The backend will be available at:

```text
http://127.0.0.1:8000
```

FastAPI interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

### 8. Start the Streamlit Frontend

Open another terminal and run the Streamlit application:

```bash
streamlit run frontend/app.py
```

Replace `frontend/app.py` with the actual Streamlit entry-point filename if different.

Ensure the frontend API URL points to the running FastAPI backend.

## 🔐 Environment Variables

| Variable | Description |
|---|---|
| `GROQ_API_KEY` | API key used to access the Groq LLM service. |

Keep environment variables and credentials outside version control.

## 🎯 Key Features

- **Retrieval-Augmented Generation:** Combines semantic document retrieval with LLM-based answer generation.
- **FAISS Vector Search:** Efficient similarity search over document embeddings.
- **Groq LLM Integration:** Uses the `openai/oss-20b` model through the Groq API.
- **Intent Classification:** Routes user queries based on their intent.
- **Contextual Question Handling:** Understands follow-up questions using conversation history.
- **Document-Grounded Responses:** Generates answers using retrieved company policy information.
- **FastAPI Backend:** Exposes the RAG pipeline through REST API endpoints.
- **Streamlit Frontend:** Provides an interactive conversational interface.

## 🔮 Future Enhancements

- Support for multiple PDF documents.
- Document upload through the frontend.
- Improved retrieval and reranking strategies.
- Source citations and page-level references.
- Enhanced conversational memory.
- Authentication and user-specific chat history.
- Evaluation of retrieval accuracy and answer quality.

## 👨‍💻 Author

**Srivatsava**

Advanced RAG implementation using LangChain, Groq, FAISS, FastAPI, and Streamlit.

---

⭐ If you find this project useful, feel free to explore and contribute.
