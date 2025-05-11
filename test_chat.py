import httpx

def test_chat():
    url = "http://127.0.0.1:8000/chat/"
    payload = {
        "user_id": "123",
        "message": "How are you feeling today?"
    }

    try:
        response = httpx.post(url, json=payload)
        response.raise_for_status()
        data = response.json()
        print("✅ AI Response:", data.get("reply"))
    except httpx.RequestError as e:
        print("❌ Request failed:", e)
    except httpx.HTTPStatusError as e:
        print("❌ Server error:", e.response.status_code, e.response.text)

if __name__ == "__main__":
    test_chat()
