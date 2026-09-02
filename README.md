# Narad Muni Chatbot

A small Streamlit chat application using Groq's chat completions API. Conversation history is kept in the browser session and sent with each request so replies have context.

## Live demo

[Open the Narad Muni Chatbot](https://narad-muni-chatbot.streamlit.app/)

The hosted app may take a few seconds to wake up after a period of inactivity.

## Run locally

```bash
git clone https://github.com/JanakDobariya/Narad-Muni-chatbot.git
cd Narad-Muni-chatbot
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
streamlit run app.py
```

Add your own `GROQ_API_KEY` to `.env`. Never commit that file or put the key directly in the source code.

Open `http://localhost:8501` if Streamlit does not open the browser automatically. On Windows, activate the environment with `.venv\Scripts\activate`.

## Offline use

The Streamlit interface can be started locally, but chatbot responses cannot be generated fully offline. The application must reach Groq's API and therefore requires an internet connection and a valid `GROQ_API_KEY`.

## Deployment

Set `GROQ_API_KEY` in the hosting platform's secret manager. For Streamlit Community Cloud, add it under **App settings → Secrets**.
