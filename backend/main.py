from fastapi import FastAPI
from backend.routes.chat import router as chat_router

app = FastAPI(title="AI Companion API")

# Health check
@app.get("/ping")
async def ping():
    return {"message": "pong"}

# Include routes
app.include_router(chat_router, prefix="/chat", tags=["chat"])
