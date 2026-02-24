# Integration Outline: AI Engine + Middleware
The project operates as a seamless data flow between three layers: **User (Browser) ↔️ Middleware (.NET) ↔️ AI Engine (Python).**

### 1. Intelligence Layer (Python + RAG)
This layer handles the "heavy lifting": parsing the PDF, converting text into vector embeddings, and orchestrating the RAG pipeline using Llama 3.3 (via Groq).

- **Directory:** `ai-engine-python/`
- **Spin-up Command:** 
```bash
uv run uvicorn main:app --reload --port 8000
```
- **How it works:** The server listens on port 8000. It processes incoming semantic queries at http://127.0.0.1:8000/ask?question=... and returns context-aware responses. 

### 2. Orchestration Layer (C# / .NET Middleware)

This layer acts as the system's "gatekeeper" and orchestrator. It manages business logic and secures the communication between the frontend and the AI engine.

- **Directory:** `middleware-dotnet/BlipGateway/`
- **Spin-up Command:** 
```bash
dotnet run
```
- **How it works:** Once you run the command above, check the terminal output for a message like: `Now listening on: http://localhost:5xxx`

(Usually it defaults to 5000, 5001, or 5216).

This service uses a pre-configured `HttpClient` to forward user queries to the Python engine.

### 3. Request Lifecycle (The "Happy Path")

To get the system up and running, follow this checklist:

1. **Sync Terminals:** Keep two terminal tabs open, one for the Python engine and one for the .NET middleware.

2. **The Handshake:** When you hit the .NET endpoint `(/ask-ai),` it sends an internal request to the Python server, waits for the RAG processing to finish, and serves the JSON response.

### Troubleshooting
If a port is stuck, you can quickly clear it using:
- `lsof -ti:8000 | xargs kill -9 (Python)`
- `lsof -ti:5216 | xargs kill -9 (.NET)`