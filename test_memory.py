from backend.services.memory import save_conversation, get_conversations
from models.memory import ConversationEntry
from datetime import datetime, UTC

# Sample entry
entry = ConversationEntry(
    user_id="123",
    message="Hello, AI!",
    response="Hi there, how can I help?",
    timestamp=datetime.now(UTC),
    mood="curious"
)

# Save to database
save_conversation(entry)
print("✅ Conversation saved.")

# Retrieve last 5 conversations for user
entries = get_conversations(user_id="123", limit=5)
print(f"🧾 Retrieved {len(entries)} conversation(s):")
for e in entries:
    print(f"- {e.timestamp.isoformat()} | {e.message} -> {e.response} ({e.mood})")
