import os

import streamlit as st
from dotenv import load_dotenv
from groq import Groq


st.set_page_config(page_title="Narad Muni Chatbot", page_icon="💬")
load_dotenv()

st.title("💬 Narad Muni Chatbot")
st.caption("A simple conversational assistant powered by Groq")

try:
    streamlit_api_key = st.secrets.get("GROQ_API_KEY")
except Exception:
    streamlit_api_key = None
api_key = os.getenv("GROQ_API_KEY") or streamlit_api_key
if not api_key:
    st.error("GROQ_API_KEY is not configured. Add it to a local .env file or the deployment secrets.")
    st.stop()

client = Groq(api_key=api_key)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask me anything..."):
    user_message = {"role": "user", "content": prompt}
    st.session_state.messages.append(user_message)
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        completion = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=st.session_state.messages,
        )
        response = completion.choices[0].message.content or "I could not generate a response."
    except Exception:
        st.error("The chat service is unavailable right now. Please try again shortly.")
    else:
        st.session_state.messages.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"):
            st.markdown(response)
