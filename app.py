from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from langchain_tavily import TavilySearch 
import os
from langgraph.prebuilt import create_react_agent 
from langchain_groq import ChatGroq
import uvicorn

# --- Setup: Ensure Keys are available ---
# Replace the placeholder key with your actual key if needed, or rely on the environment variable
groq_api_key = os.getenv("GROQ_API_KEY", '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') 
os.environ["TAVILY_API_KEY"] = os.getenv("TAVILY_API_KEY", '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')

# Corrected model list to include the latest, supported Mixtral model (mixtral-8x7b-32k)
MODEL_NAMES = [
    "llama-3.1-8b-instant",    # Corrected name
    "llama-3.3-70b-versatile",   # Corrected name
    "qwen/qwen3-32b"      # This name is correct
]


# Configure Tavily tool
tool_tavily = TavilySearch(max_results=1) 
tools = [tool_tavily]

app = FastAPI(title='LangGraph AI Agent')

# Pydantic model for the incoming request data
class RequestState(BaseModel):
    system_prompt: str
    model_name: str
    messages: List[str]

# --- FastAPI Endpoint ---
@app.post("/chat")
def chat_endpoint(request: RequestState):
    """
    API endpoint to interact with the chatbot using LangGraph and tools.
    """
    # 1. Model Validation 
    if request.model_name not in MODEL_NAMES:
        return {"error": "Invalid model name. Please select a valid model."}

    # 2. Initialize LLM
    try:
        # Initialize the LLM with the API key and the model name from the request
        llm = ChatGroq(groq_api_key=groq_api_key, model_name=request.model_name)
    except Exception as e:
        # Catch key/auth errors before agent creation
        print(f"LLM Initialization Error: {e}")
        return {"error": f"LLM Initialization Error: {e}"}

    # 3. Agent setup
    # Note: create_react_agent is a robust pre-built agent
    agent = create_react_agent(llm, tools=tools) 
    
    # 4. Prepare Message State
    # LangGraph expects messages in the format: [('role', 'content')]
    messages_list = [("system", request.system_prompt)]
    
    # Add the user messages (we only expect one message from the Streamlit payload)
    for msg in request.messages:
        messages_list.append(("user", msg))

    # Create the initial state dictionary
    state = {"messages": messages_list}

    # 5. Process the state using the agent
    try:
        # Invoke the agent to run the chat logic
        result = agent.invoke(state)
        # result is a dictionary containing the final state, including messages
        return result
    except Exception as e:
        # This catch block is crucial for turning internal errors into a readable 500 error response
        error_message = f"Agent processing failed. Error: {e.args[0] if e.args else str(e)}"
        print(f"Agent Invocation Failed: {error_message}")
        return {"error": error_message}

# --- Execution ---
if __name__ == '__main__':
    # Runs the server on port 8001 as required by the Streamlit frontend
    uvicorn.run(app, host='127.0.0.1', port=8001)