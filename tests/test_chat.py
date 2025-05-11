from fastapi.testclient import TestClient
from backend.main import app

def test_chat_endpoint(monkeypatch):
    # Mock OpenAI response
    class MockResponse:
        def __init__(self, content):
            self.choices = [type("Choice", (), {"message": type("Message", (), {"content": content})})()]

    class MockClient:
        def __init__(self, **kwargs):
            pass

        class chat:
            class completions:
                @staticmethod
                def create(model, messages, temperature):
                    return MockResponse("This is a test reply.")

    # Patch OpenAI client in the route
    monkeypatch.setattr("backend.routes.chat.client", MockClient())

    # Use synchronous FastAPI test client
    client = TestClient(app)
    response = client.post("/chat/", json={"user_id": "test_user", "message": "Hello"})

    assert response.status_code == 200
    data = response.json()
    assert "reply" in data
    assert data["reply"] == "This is a test reply."
