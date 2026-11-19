import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# Load environment variables from .env file
load_dotenv()

# initialize the embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    )

# load Faiss vector database
vectorstore = FAISS.load_local("vectorstore", embeddings, allow_dangerous_deserialization=True)

# Creat the retriever from the vectorstore
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# initialize the ChatGroq model

llm= ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0,
    api_key=os.environ.get("GROQ_API_KEY")
)
