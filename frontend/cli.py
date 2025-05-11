import httpx

API_URL = "http://127.0.0.1:8000"

def check_server():
    try:
        response = httpx.get(f"{API_URL}/ping")
        if response.status_code == 200:
            print("✅ Connected to AI Companion API.")
        else:
            print("⚠️ Unable to verify backend is running.")
            return False
    except httpx.RequestError:
        print("❌ Backend not reachable. Is the FastAPI server running?")
        return False
    return True

def chat_loop(user_id="local_user"):
    print("\n👋 Welcome to your AI Companion. Type 'exit' to quit.")
    while True:
        message = input("You: ").strip()
        if message.lower() in {"exit", "quit"}:
            print("👋 Goodbye!")
            break

        try:
            response = httpx.post(f"{API_URL}/chat/", json={"user_id": user_id, "message": message})
            response.raise_for_status()
            reply = response.json().get("reply", "[No reply received]")
            print("AI:", reply)
        except httpx.RequestError as e:
            print("❌ Request failed:", e)
        except httpx.HTTPStatusError as e:
            print(f"❌ Server error: {e.response.status_code} - {e.response.text}")

if __name__ == "__main__":
    if check_server():
        chat_loop()
