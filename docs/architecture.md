# System Architecture: AI Companion MVP

## 🧩 Overview

This document outlines the technical architecture for the AI Companion MVP — a personalized, emotionally supportive AI chatbot with conversational memory and customizable personality traits.

---

## 🛠️ Tech Stack

| Layer       | Technology      | Justification                                  |
|-------------|------------------|-----------------------------------------------|
| Frontend    | CLI or React     | CLI is easiest for rapid prototyping; React for web UI |
| Backend     | FastAPI          | Fast, async, modern framework with OpenAPI support |
| Memory      | SQLite           | Lightweight and local storage for user data and context |
| AI Engine   | OpenAI API       | Reliable LLM interface with strong conversation capabilities |
| Deployment  | Local or Render  | Local for dev, Render/Heroku for early deployment |

---

## 🧱 Components

```
📦 ai-companion/
├── frontend/           # User interface (CLI or web)
│   └── chat_ui.py      # or React components
├── backend/
│   ├── main.py         # FastAPI app entry point
│   ├── routes/
│   │   └── chat.py     # POST /chat endpoint
│   └── services/
│       ├── memory.py   # Handles DB reads/writes
│       └── personality.py
├── data/
│   └── ai_companion.db # SQLite database file
├── models/
│   └── user_state.py   # Pydantic models for requests and responses
└── config.py           # API keys and feature toggles
```

---

## 🔁 Data Flow

1. **User** enters message via CLI or Web UI.
2. **Frontend** sends message to `/chat` endpoint on FastAPI backend.
3. **Backend** loads:
   - User profile, personality, and memory from SQLite
   - Constructs prompt for OpenAI API
4. **AI Engine** responds.
5. Backend:
   - Stores updated conversation history
   - Logs mood or interaction tags (if enabled)
6. **Frontend** displays AI's response.

---

## 🔐 Design Principles

- **Modular Services**: Separate logic for memory, personality, chat.
- **Privacy First**: Memory stored locally by default.
- **Safe Defaults**: Users can opt out of simulated affection or emotional depth.
- **Extensible**: Prepared for voice, avatar, and smart integrations.

---

## 🌐 API Endpoints (Planned)

| Method | Endpoint | Description                  |
|--------|----------|------------------------------|
| POST   | /chat    | Accepts user message and returns AI response |
| GET    | /profile | Retrieves saved personality or memory (future) |

---

*This document will evolve as the system expands beyond the MVP.*