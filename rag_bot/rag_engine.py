from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
import os

# 1. Initialize Vector Database Path
VECTOR_DB_PATH = "./chroma_db"

# 2. Use FREE Local Embeddings (No API Key needed!)
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

def process_and_store_pdf(file_path, metadata):
    print(f"Processing document: {file_path}")
    loader = PyPDFLoader(file_path)
    pages = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = text_splitter.split_documents(pages)

    for doc in docs:
        doc.metadata.update(metadata)

    Chroma.from_documents(docs, embeddings, persist_directory=VECTOR_DB_PATH)
    print("Document successfully saved to Vector Database!")

def ask_question(user_query):
    db = Chroma(persist_directory=VECTOR_DB_PATH, embedding_function=embeddings)
    results = db.similarity_search(user_query, k=2)
    
    if not results:
        return {"text": "I couldn't find any documents related to that.", "source": None}
    
    best_match = results[0]
    return {
        "text": best_match.page_content,
        "source": best_match.metadata
    }