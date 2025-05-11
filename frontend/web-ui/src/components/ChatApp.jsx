import React, { useState, useEffect, useRef } from "react";
import axios from "axios";
import "./ChatApp.css";

const API_URL = "http://localhost:8000/chat/";
const USER_ID = "web_user";

export default function ChatApp() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const chatBoxRef = useRef(null);

  const handleSend = async () => {
    if (!input.trim()) {
      setError("⚠️ Please enter a message.");
      return;
    }

    const newMessages = [...messages, { sender: "user", text: input }];
    setMessages(newMessages);
    setInput("");
    setLoading(true);
    setError("");

    try {
      const response = await axios.post(API_URL, {
        user_id: USER_ID,
        message: input,
      });

      const aiReply = response?.data?.reply || "⚠️ I didn't understand that.";
      setMessages([...newMessages, { sender: "ai", text: aiReply }]);
    } catch (err) {
      setError("❌ Failed to reach the server.");
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
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder="Type your message..."
        />
        <button onClick={handleSend}>Send</button>
      </div>
      {error && <div className="error">{error}</div>}
    </div>
  );
}
