# Narad Muni Chatbot

A small Streamlit chat application using Groq's chat completions API. Conversation history is kept in the browser session and sent with each request so replies have context.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
streamlit run app.py
```

Add your own `GROQ_API_KEY` to `.env`. Never commit that file or put the key directly in the source code.

## Deployment

Set `GROQ_API_KEY` in the hosting platform's secret manager. For Streamlit Community Cloud, add it under **App settings → Secrets**.
