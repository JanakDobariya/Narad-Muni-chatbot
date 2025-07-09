import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

# Load environment variables (API key, etc.)
load_dotenv()

# Initialize model
model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    # Or set the API key here directly:
    # google_api_key=os.getenv("GOOGLE_API_KEY")
)

# Set up Streamlit page
st.set_page_config(page_title="Narada Muni Chatbot", page_icon="🤖")
st.title("💬 Narada Muni Chatbot")
st.caption("Powered by LangChain + Gemini 2.0")

# Session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User input box
user_input = st.chat_input("Ask me anything...")

# Handle user input
if user_input:
    # Add user message to history
    st.session_state.chat_history.append(user_input)

    # Call Gemini model
    result = model.invoke(st.session_state.chat_history)

    # Append model response
    st.session_state.chat_history.append(result.content)

# Display chat history
for i, message in enumerate(st.session_state.chat_history):
    is_user = i % 2 == 0  # Even index = user, odd = AI
    with st.chat_message("user" if is_user else "assistant"):
        st.markdown(message)