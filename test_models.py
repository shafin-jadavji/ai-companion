from models.chat import ChatRequest, ChatResponse
from models.user import UserProfile
from models.memory import ConversationEntry
from datetime import datetime, UTC

# Test ChatRequest
chat_req = ChatRequest(user_id="123", message="Hello!")
print("ChatRequest:", chat_req)

# Test ChatResponse
chat_res = ChatResponse(reply="Hi there!", mood="happy")
print("ChatResponse:", chat_res)

# Test UserProfile
user = UserProfile(user_id="123", name="Alex", personality="supportive")
print("UserProfile:", user)

# Test ConversationEntry
entry = ConversationEntry(
    user_id="123",
    message="Hi",
    response="Hello!",
    timestamp=datetime.now(UTC),
    mood="calm"
)
print("ConversationEntry:", entry)

