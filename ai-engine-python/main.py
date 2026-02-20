import os
import uvicorn
from fastapi import FastAPI, HTTPException
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_chroma import Chroma
from langchain_classic.chains  import RetrievalQA  # Use a versão estável
from dotenv import load_dotenv

# --- INITIAL CONFIGURATION ---
# Load environment variables from the .env file
load_dotenv()
CHAVE_GROQ = os.getenv("GROQ_API_KEY")
PDF_PATH = "/Users/carollinereis/PROJ/blip-docs-assistant/docs/blip-docs-API-reference.pdf"

# Validate API Key existence before starting the server
if not CHAVE_GROQ:
    raise ValueError("ERRO: GROQ_API_KEY não encontrada no arquivo .env!")

# Initialize FastAPI app
app = FastAPI(docs_url="/test", 
              title="Blip Docs Assistant",
              description="AI-powered assistant to query Blip API documentation using RAG."
)

# --- RAG ENGINE SETUP (PRE-LOADING) ---
# We process the PDF and create the vector database once at startup to optimize performance.
print("⚙️ Loading intelligence from PDF... Please hold.")

loader = PyPDFLoader(PDF_PATH)
documents = loader.load()

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = Chroma.from_documents(documents, embeddings)
print("System ready for queries!")

# --- API ROUTES ---

@app.get("/")
def home():
    return {"status": "Online", "engine": "Groq + Llama 3.3"}

@app.get("/ask", tags=["Query"])
def ask_ai(question: str):
    try:
        # Initialize the LLM via Groq
        llm = ChatGroq(
            model_name="llama-3.3-70b-versatile", 
            temperature=0,
            groq_api_key=CHAVE_GROQ
        )

        # Set up the RetrievalQA chain
        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=vectorstore.as_retriever()
        )

        # Execute the query
        response = qa_chain.invoke(question)
        return {"question": question, "answer": response["result"]}
    
    except Exception as e:
        # Return a professional 500 Internal Server Error if something goes wrong
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)