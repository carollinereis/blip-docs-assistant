# Blip Docs Assistant 🤖

AI assistant designed to streamline technical documentation analysis, specifically developed with a focus on **Blip's ecosystem**. 

## 🚀 Project Status

| Task | Status |
| :--- | :--- |
| Project Structure | ✅ Done |
| Python Environment | ✅ Done |
| AI Engine (API Base) | ✅ Done |
| AI Engine (RAG Logic) | ✅ Done |
| Middleware (.NET Orchestrator) | ⏳ To Do |
| Frontend (React + TypeScript) | ⏳ To Do |


> [!TIP]
> This project is part of my technical preparation for the Software Engineering MBA at ESALQ USP (starting May 2026). You can track the full progress in the [Kanban Board](https://github.com/users/carollinereis/projects/4).

## Overview
The **Blip Docs Assistant** is a full-stack application that leverages Large Language Models (LLMs) to answer questions based on technical documentation. It uses a **RAG (Retrieval-Augmented Generation)** architecture to ensure accurate and context-aware responses.

## Architecture

Designed with industry-standard patterns in mind, the project is organized into modular services to simulate a real-world production environment:

* [AI Engine (Python):](./ai-engine-python/readme.md) Powered by FastAPI and LangChain. Handles PDF processing and RAG logic.

* [Middleware (C# / .NET)](./middleware-csharp/readme.md): An ASP.NET Core API acting as a secure gateway.

* Frontend (React + TypeScript): A modern, responsive chat interface (Coming soon).

## 🛠️ Tech Stack
* **Languages:** Python 3.11+, C# (ASP.NET Core), TypeScript.
* **Frameworks:** FastAPI, LangChain
* **LLM:** Llama 3.3-70b (via Groq Cloud for ultra-low latency)
* **Web:** React.js, Vite, TailwindCSS.
* **DevOps:** GitHub Projects (Agile/Kanban), Git.

---
*Developed by Carolline Rezende - 2026*
