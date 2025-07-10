import streamlit as st
from dotenv import load_dotenv
from groq import Groq
import os

# Load environment variables (like GROQ_API_KEY)
load_dotenv()

# Initialize Groq client with API key from environment
groq_api_key = os.getenv("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")
if not groq_api_key:
    st.error("GROQ_API_KEY not set. Please add it to your .env file.")
    st.stop()
groq_client = Groq(api_key=groq_api_key)

def groq_invoke(messages, model="llama3-70b-8192"):
    # Prepare messages for Groq (alternating user/assistant)
    formatted_messages = []
    for i, m in enumerate(messages):
        role = "user" if i % 2 == 0 else "assistant"
        formatted_messages.append({"role": role, "content": m})
    # Call Groq API
    completion = groq_client.chat.completions.create(
        model=model,
        messages=formatted_messages
    )
    return completion.choices[0].message.content

# --- Streamlit UI setup ---
st.set_page_config(page_title="Narad Muni Chatbot", page_icon="🤖")
st.title("💬 Narad Muni Chatbot")
st.caption("Made by Janak Dobariya")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.chat_input("Ask me anything...")

if user_input:
    st.session_state.chat_history.append(user_input)
    response = groq_invoke(st.session_state.chat_history)
    st.session_state.chat_history.append(response)

# Display chat history
for i, message in enumerate(st.session_state.chat_history):
    is_user = i % 2 == 0  # Even index = user, odd = AI
    with st.chat_message("user" if is_user else "assistant"):
        st.markdown(message)
