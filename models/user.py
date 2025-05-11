from pydantic import BaseModel

class UserProfile(BaseModel):
    user_id: str
    name: str
    personality: str
    prefers_affection: bool = True
