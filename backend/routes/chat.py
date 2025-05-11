from fastapi import APIRouter, HTTPException
from openai import OpenAI
from models.chat import ChatRequest, ChatResponse
from backend.services.memory import get_conversations, save_conversation
from models.memory import ConversationEntry
from datetime import datetime, UTC
from backend.config import settings

router = APIRouter()

# Initialize OpenAI client
client = OpenAI(api_key=settings.openai_api_key)

@router.post("/", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        # Retrieve recent messages
        recent = get_conversations(user_id=request.user_id, limit=5)

        # Build OpenAI messages format
        messages = [
            {"role": "system", "content": "You are a supportive AI companion. Keep responses kind, brief, and emotionally aware."}
        ]
        for entry in reversed(recent):
            messages.append({"role": "user", "content": entry.message})
            messages.append({"role": "assistant", "content": entry.response})

        # Add current user message
        messages.append({"role": "user", "content": request.message})

        # Send to OpenAI
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.7,
        )

        reply = response.choices[0].message.content.strip()

        # Create response object
        response_obj = ChatResponse(reply=reply)

        # Save to memory
        entry = ConversationEntry(
            user_id=request.user_id,
            message=request.message,
            response=reply,
            timestamp=datetime.now(UTC),
            mood=None  # Can be set later with emotion analysis
        )
        save_conversation(entry)

        return response_obj

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
