# loads the PDF, split it, creates embeddings, and stores them in a vector database.

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# step1: load the PDF file  
loader = PyPDFLoader("data/company_policy.pdf")
documents = loader.load()

# step2: split the PDF into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
chunks = text_splitter.split_documents(documents)

# step3: create embeddings for each chunk
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
# step4 : Create FAISS vector database

vectorstore = FAISS.from_documents(chunks, embeddings)

# step5 : Save the vector database
vectorstore.save_local("vectorstore")

print("Vector database created successfully.")

