# AI Companion Project

This project aims to develop an AI-powered emotional support and relationship simulation companion that users can interact with through natural conversations.

## 🚀 Project Overview

The AI Companion offers:
- Emotionally intelligent and context-aware conversations
- Customizable personalities and daily check-ins
- Lightweight memory for personalization
- A modular design ready for future expansion

## 📁 Project Structure

```
ai-companion-project/
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
├── backend/
│   ├── main.py
│   ├── config.py
│   ├── routes/
│   │   └── chat.py
│   └── services/
│       ├── openai_service.py
│       └── memory.py
├── models/
│   ├── user.py
│   ├── chat.py
│   └── memory.py
├── tests/
│   ├── test_models.py
│   ├── test_chat.py
│   └── test_memory.py
├── data/
│   └── ai_companion.db
├── frontend/
│   └── cli.py
└── docs/
    ├── core_functionalities.md
    ├── mvp_specification.md
    ├── architecture.md
    └── COMMIT_CONVENTION.md
```

## 🔧 Setup Instructions

### 1. Clone or Download the Project

```bash
git clone https://github.com/shafin-jadavji/ai-companion.git
cd ai-companion
```

### 2. Create and Activate a Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Windows
venv\Scripts\activate

# On Mac/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the FastAPI App

```bash
uvicorn backend.main:app --reload
```

---

If you’re using VS Code, it will detect the `venv` folder.  
Select the Python interpreter from the command palette if prompted.

## 📄 License

This project is licensed under the [MIT License](LICENSE).  
You are free to use, modify, and distribute this software with proper attribution.
