from fastapi import APIRouter, HTTPException
from openai import OpenAI
from models.chat import ChatRequest, ChatResponse
from backend.services.memory import get_conversations, save_conversation
from models.memory import ConversationEntry
from datetime import datetime, UTC
from backend.config import settings
import logging

logger = logging.getLogger(__name__)

router = APIRouter()

client = OpenAI(api_key=settings.openai_api_key)

@router.post("/", response_model=ChatResponse)
async def chat(request: ChatRequest):
    logger.info("POST /chat called")
    logger.info(f"User message: {request.message}")

    try:
        logger.info(f"Retrieving recent conversations for user: {request.user_id}")
        recent = get_conversations(user_id=request.user_id, limit=5)

        messages = [
            {"role": "system", "content": "You are a supportive AI companion. Keep responses kind, brief, and emotionally aware."}
        ]
        for entry in reversed(recent):
            messages.append({"role": "user", "content": entry.message})
            messages.append({"role": "assistant", "content": entry.response})

        messages.append({"role": "user", "content": request.message})

        logger.info("Calling OpenAI API")
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.7,
        )

        reply = response.choices[0].message.content.strip()
        logger.info(f"OpenAI reply: {reply}")

        response_obj = ChatResponse(reply=reply)

        entry = ConversationEntry(
            user_id=request.user_id,
            message=request.message,
            response=reply,
            timestamp=datetime.now(UTC),
            mood=None
        )
        logger.info("Saving conversation entry to memory")
        save_conversation(entry)

        return response_obj

    except Exception as e:
        logger.exception("Error in /chat endpoint")
        raise HTTPException(status_code=500, detail=str(e))
