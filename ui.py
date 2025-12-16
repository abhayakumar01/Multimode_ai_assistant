
import streamlit as st
import requests

# Streamlit App Configuration
st.set_page_config(page_title="LangGraph Agent UI", layout="centered")

# Define API endpoint
API_URL = "http://127.0.0.1:8001/chat"

st.title("LangGraph Chatbot Agent")
st.write("Interact with the LangGraph-based agent using this interface.")

# Input box for system prompt
given_system_prompt = st.text_area("Define you AI Agent:", height=70, placeholder="Type your system prompt here...")
# Predefined models
# Predefined models
models = ["llama-3.1-8b-instant", "llama-3.3-70b-versatile", "qwen/qwen3-32b"]
# Dropdown for selecting the model
selected_model = st.selectbox("Select Model:", models) # <-- Should be 'models'


# Input box for user messages
user_input = st.text_area("Enter your message(s):", height=150, placeholder="Type your message here...")

# Button to send the query
if st.button("Submit"):
    if user_input.strip():
        try:
            # Send the input to the FastAPI backend
            payload = {"messages": [user_input], "model_name": selected_model, 'system_prompt': given_system_prompt}
            response = requests.post(API_URL, json=payload)

            # Display the response
            if response.status_code == 200:
                response_data = response.json()
                if "error" in response_data:
                    st.error(response_data["error"])
                else:
                    # LangGraph returns messages as a list of tuples/dicts, we extract the AI content
                    ai_responses = [
                        message.get("content", "")
                        for message in response_data.get("messages", [])
                        if message.get("type") == "ai"
                    ]

                    if ai_responses:
                        st.subheader("Agent Response:")
                        # We show the last and final response from the agent
                        st.markdown(f"**Final Response:** {ai_responses[-1]}")
                    else:
                        st.warning("No AI response found in the agent output. Check the backend logs for tool execution errors.")
            else:
                st.error(f"Request failed with status code {response.status_code}. Check the backend terminal for detailed error traceback.")
        except requests.exceptions.ConnectionError:
             st.error("Connection Error: Could not connect to the FastAPI backend. Ensure the uvicorn server is running on http://127.0.0.1:8001.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a message before clicking 'Submit'.")