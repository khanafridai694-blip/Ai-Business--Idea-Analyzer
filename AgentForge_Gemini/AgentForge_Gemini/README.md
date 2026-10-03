# 🚀 AgentForge

AgentForge is a CrewAI multi-agent startup/product idea analyzer powered by the Google Gemini Developer API.

## AI Team

- 🧠 Manager Agent
- 🔎 Market Agent
- 💰 Business Agent
- 💻 Technical Agent
- ⚔️ Challenger Agent

## Workflow

User Idea → Market + Business + Technical Analysis → Challenger Debate → Manager → Final Improved Plan

## LLM

The project uses:

`gemini/gemini-2.5-flash`

through CrewAI/LiteLLM and the Gemini Developer API.

## API Key

Set:

`GEMINI_API_KEY`

For Streamlit Community Cloud, add the key under:

App Settings → Secrets

Example:

```toml
GEMINI_API_KEY = "your-key-here"
```

Never commit the real key to GitHub.

## Important

This project does not use:

- Groq
- GROQ_API_KEY
- Serper
- Flask
- FastAPI
- a separate backend
