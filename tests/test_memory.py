import os
import sqlite3
import pytest
import gc
from importlib import reload
from datetime import datetime, UTC
from backend.services.memory import save_conversation, get_conversations
from models.memory import ConversationEntry

# Setup test database
TEST_DB_PATH = "data/test_ai_companion.db"

@pytest.fixture(scope="function", autouse=True)
def setup_test_db(monkeypatch):
    # Patch the DB path for testing
    monkeypatch.setattr("backend.services.memory.DB_PATH", TEST_DB_PATH)

    # Ensure clean test db before test
    if os.path.exists(TEST_DB_PATH):
        os.remove(TEST_DB_PATH)

    # Reload the module to ensure fresh state
    import backend.services.memory as memory_service
    reload(memory_service)
    memory_service.initialize_database()

    yield

    # Force-close any open connections
    gc.collect()

    # Clean up after test
    if os.path.exists(TEST_DB_PATH):
        os.remove(TEST_DB_PATH)

def test_save_and_get_conversation():
    timestamp = datetime.now(UTC)
    entry = ConversationEntry(
        user_id="test_user",
        message="What's up?",
        response="Not much, you?",
        timestamp=timestamp,
        mood="neutral"
    )

    save_conversation(entry)
    results = get_conversations(user_id="test_user")

    assert len(results) == 1
    retrieved = results[0]
    assert retrieved.user_id == "test_user"
    assert retrieved.message == "What's up?"
    assert retrieved.response == "Not much, you?"
    assert retrieved.timestamp == timestamp
    assert retrieved.mood == "neutral"
