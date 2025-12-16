# Multimodle_ai_assistant

# 🤖 LangGraph Chatbot Agent 

## 💡 Overview

This project presents a web-based interface for building and interacting with flexible, role-based **AI Agents** powered by the **LangGraph framework**. It allows users to define a specific agent personality (system prompt) and select a large language model (LLM) for the agent's core reasoning.

 
## ✨ Key Features

  * **Custom Agent Definition:** Easily define the agent's role and behavior (e.g., "health assistance," "career counselor") via a system prompt input field.
  * **Model Selection:** Choose from different locally served or accessible LLMs (e.g., `llama-3.1-8b-instant`).
   
  * **Interactive UI:** Simple, dark-themed user interface built for fast prototyping and interaction.

## 🛠️ Technology Stack

| Component | Role |
| :--- | :--- |
| **Backend Framework** | Python / FastAPI (ASGI Server) |
| **Server** | Uvicorn |
| **Core Logic** | LangGraph, LangChain |
| **LLM Access** | Integrated via Ollama or similar local API endpoints (assumed) |
| **Frontend** | streamlit |

## 🚀 Getting Started

Follow these steps to set up and run the LangGraph Chatbot Agent locally.

### Prerequisites

1.  **Python 3.9+** installed.
2.  Access to a model API (e.g., running **Ollama** locally to serve models like `llama-3.1-8b-instant`).
3.  Ensure your required model is available on your local endpoint.

### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/LangGraph-Chatbot-Agent.git
    cd LangGraph-Chatbot-Agent
    ```

2.  **Create and activate a virtual environment:**

    ```bash
    python -m venv v
    .\venv\Scripts\activate  # Windows
    source venv/bin/activate # macOS/Linux
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

    *(Note: Ensure your `requirements.txt` includes `fastapi`, `uvicorn`, `langgraph`, `langchain`,`streamlit` etc.)*

### Running the Application

1.  **Start the Uvicorn server:**

    ```bash
    uvicorn app:app --reload --port 8001
    ```

    *(Note: If your client is configured for port 8001, use `uvicorn app:app --reload --port 8001`)*

2.  **Access the Interface:**
    Open your web browser and navigate to:

    ```
    http://127.0.0.1:8000
    ```

    *(Replace 8000 with your chosen port if different).*

## 📖 Usage

1.  **Define Agent:** In the "Define you AI Agent" field, enter the system prompt (e.g., "You are a professional Python developer who only responds with code examples.").
2.  **Select Model:** Choose the desired LLM from the "Select Model" dropdown.
3.  **Enter Message:** Type your query into the "Enter your message(s)" box (e.g., "I am feeling cold").
4.  **Submit:** Click "Submit" to run the LangGraph agent and view the detailed response in the "Agent Response" section.

 
 
 

## 🖥️ User interface 
<img width="1919" height="1079" alt="Screenshot 2025-12-16 090936" src="https://github.com/user-attachments/assets/1a04cd45-0fc5-4246-9347-164b38d89341" />

## demonstration
<img width="1920" height="1020" alt="Screenshot 2025-12-16 091324" src="https://github.com/user-attachments/assets/ba0870ee-405e-4cb6-a6f1-f56796861c3b" />
<img width="1913" height="1064" alt="Screenshot 2025-12-16 091419" src="https://github.com/user-attachments/assets/7b0d09a8-ff59-445e-8e42-838812ed79c8" />



