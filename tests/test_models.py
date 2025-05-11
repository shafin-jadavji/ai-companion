from models.chat import ChatRequest, ChatResponse
from models.memory import ConversationEntry
from models.user import UserProfile
from datetime import datetime, UTC

def test_chat_request_valid():
    request = ChatRequest(user_id="123", message="Hi!")
    assert request.user_id == "123"
    assert request.message == "Hi!"

def test_chat_response_valid():
    response = ChatResponse(reply="Hello!", mood="friendly")
    assert response.reply.startswith("Hello")
    assert response.mood == "friendly"

def test_user_profile_valid():
    profile = UserProfile(user_id="user_1", name="Ava", personality="supportive")
    assert profile.user_id == "user_1"
    assert profile.name == "Ava"

def test_conversation_entry_valid():
    timestamp = datetime.now(UTC)
    entry = ConversationEntry(
        user_id="123",
        message="Hello",
        response="Hi there!",
        timestamp=timestamp,
        mood="curious"
    )
    assert entry.user_id == "123"
    assert entry.timestamp == timestamp
