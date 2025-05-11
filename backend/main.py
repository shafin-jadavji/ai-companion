from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routes.chat import router as chat_router

app = FastAPI(title="AI Companion API")

# CORS middleware to allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check
@app.get("/ping")
async def ping():
    return {"message": "pong"}

# Chat route
app.include_router(chat_router, prefix="/chat", tags=["chat"])
