import { useState } from "react";
import { askQuestion } from "../services/api";
import MessageBubble from "./MessageBubble";

export default function ChatWindow({ uploadedFile }) {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
    if (!input.trim() || !uploadedFile) return;

    setMessages((prev) => [...prev, { text: input, sender: "user" }]);
    setInput("");
    setLoading(true);

    try {
      const response = await askQuestion(input);
      setMessages((prev) => [
        ...prev,
        { text: response.answer, sender: "bot" },
      ]);
    } catch {
      setMessages((prev) => [
        ...prev,
        { text: "Error: Could not get response", sender: "bot" },
      ]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="chat-window">
      <div className="messages">
        {!uploadedFile && (
          <MessageBubble
            text="📄 Please upload a PDF to start chatting."
            sender="bot"
          />
        )}

        {messages.map((msg, i) => (
          <MessageBubble key={i} text={msg.text} sender={msg.sender} />
        ))}

        {loading && <MessageBubble text="Thinking..." sender="bot" />}
      </div>

      <div className="input-box">
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder={
            uploadedFile
              ? "Ask a question about your PDF..."
              : "Upload a PDF to enable chat"
          }
          disabled={!uploadedFile || loading}
        />
        <button
          onClick={sendMessage}
          disabled={!uploadedFile || loading || !input.trim()}
        >
          Send
        </button>
      </div>
    </div>
  );
}
