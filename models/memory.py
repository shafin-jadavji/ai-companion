from pydantic import BaseModel
from datetime import datetime, UTC

class ConversationEntry(BaseModel):
    user_id: str
    message: str
    response: str
    timestamp: datetime
    mood: str | None = None
