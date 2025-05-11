import React, { useState, useEffect, useRef } from "react";
import axios from "axios";
import "./ChatApp.css";

const API_URL = "http://localhost:8000/chat/";
const USER_ID = "web_user";

export default function ChatApp() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const [banner, setBanner] = useState({ text: "", type: "" });

  const chatBoxRef = useRef(null);
  const inputRef = useRef(null);

  const showMessage = (text, type = "info", timeout = 4000) => {
    setBanner({ text, type });
    setTimeout(() => {
      setBanner({ text: "", type: "" });
    }, timeout);
  };

  const handleSend = async () => {
    if (!input.trim()) {
      showMessage("⚠️ Please enter a message.", "error");
      return;
    }

    const newMessages = [...messages, { sender: "user", text: input }];
    setMessages(newMessages);
    setInput("");
    setLoading(true);

    try {
      const response = await axios.post(API_URL, {
        user_id: USER_ID,
        message: input,
      });

      const aiReply = response?.data?.reply || "⚠️ I didn't understand that.";
      setMessages([...newMessages, { sender: "ai", text: aiReply }]);
    } catch (err) {
      showMessage("❌ Failed to reach the server.", "error");
    } finally {
      setLoading(false);
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter") {
      handleSend();
    }
  };

  useEffect(() => {
    if (chatBoxRef.current) {
      chatBoxRef.current.scrollTop = chatBoxRef.current.scrollHeight;
    }
  }, [messages]);

  useEffect(() => {
    inputRef.current?.focus();
  }, []);

  return (
    <div className="chat-container">
      <div className="chat-box" ref={chatBoxRef}>
        {messages.map((msg, idx) => (
          <div key={idx} className={`message ${msg.sender}`}>
            <span>{msg.text}</span>
          </div>
        ))}
        {loading && <div className="message ai">⏳ Thinking...</div>}
      </div>
      <div className="input-area">
        <input
          ref={inputRef}
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder="Type your message..."
        />
        <button onClick={handleSend} disabled={!input.trim() || loading}>
          Send
        </button>
      </div>
      {banner.text && <div className={`banner ${banner.type}`}>{banner.text}</div>}
    </div>
  );
}
