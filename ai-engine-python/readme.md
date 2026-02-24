# AI Engine (Python + RAG)
This service is the core "brain" of the assistant. It processes technical documentation and provides context-aware answers using a **Retrieval-Augmented Generation (RAG) architecture.**

### 🛠️ Tech Stack
- **FastAPI:** High-performance web framework for the API layer.
- **LangChain:** Framework for orchestrating the LLM and RAG pipeline.
- **ChromaDB:** Vector database used for document storage and semantic search.
- **Groq Cloud:** Inference engine for running Llama 3.3-70b with ultra-low latency.

### API Key Setup (Groq Cloud) 
To run this engine, you need an API Key from Groq Cloud.

- Why Groq? We use Groq because it provides an incredibly fast inference engine (LPUs), allowing the **Llama 3.3** model to respond almost instantly. It also has a generous free tier for developers.
- How to get one: 
1. Create a free account at `console.groq.com.`
2. Generate an API Key in the "API Keys" section.
3. Create a `.env` file in this folder and add your key: `GROQ_API_KEY=your_key_here.`

### How to Run
1. **Environment Setup:** Ensure you have `uv` installed.
2. **Navigate to the folder:**

```Bash
cd ai-engine-python
```

3. **Spin up the engine:**

```Bash
uv run uvicorn main:app --reload --port 8000
```
The engine will be available at http://127.0.0.1:8000.

### Understanding the Endpoints (How to interact)
Since this is a "headless" API (it doesn't have a visual interface yet), we use specific web addresses to talk to it:

- ``GET /test`` **(The Health Check):**

    - **What it is:** A simple "Are you alive?" test.
    - **How to use:** Open http://127.0.0.1:8000/test in your browser. If it returns "Hello World", the server is working perfectly.

- ``GET /ask?question=...`` **(The Brain):**

    - **What it is:** This is where the magic happens. You send a question, and the AI processes the PDF to answer.
    - **How to use:** http://127.0.0.1:8000/ask?question=WhatIsBlip

- ``/docs`` **(Automatic Documentation):**

    - **What it is:** FastAPI (our framework) automatically creates a test page for us.
    - **How to use:** Go to http://127.0.0.1:8000/docs to see and test all available commands visually.

### RAG Pipeline Logic
1. **Document Loading:** Parses the Blip technical PDF files.
2. **Chunking & Embeddings:** Splits the text into optimized segments and converts them into vector representations.
3. **Vector Storage:** Stores embeddings in ChromaDB for fast retrieval.
4. **Retrieval & Synthesis:** When a query arrives, the engine finds the most relevant document chunks and sends them to Llama 3.3 to generate an accurate, grounded answer.

