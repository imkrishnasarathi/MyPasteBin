import { useState } from "react";
import axios from "axios";

function App() {
  const [text, setText] = useState("");
  const [pasteId, setPasteId] = useState("");
  const [pasteText, setPasteText] = useState("");

  const createPaste = async () => {
    const response = await axios.post("http://localhost:8000/paste", {
      text,
    });
    setPasteId(response.data.id);
  };

  const fetchPaste = async () => {
    const response = await axios.get(`http://localhost:8000/paste/${pasteId}`);
    setPasteText(response.data.text);
  };

  return (
    <div>
      <h1>Pastebin</h1>
      <textarea
        rows="4"
        cols="50"
        placeholder="Enter your text..."
        value={text}
        onChange={(e) => setText(e.target.value)}
      />
      <br />
      <button onClick={createPaste}>Create Paste</button>

      {pasteId && (
        <p>
          Paste Created! ID: <strong>{pasteId}</strong>
        </p>
      )}

      <hr />

      <input
        type="text"
        placeholder="Enter Paste ID"
        value={pasteId}
        onChange={(e) => setPasteId(e.target.value)}
      />
      <button onClick={fetchPaste}>Fetch Paste</button>

      {pasteText && (
        <div>
          <h2>Paste Content:</h2>
          <pre>{pasteText}</pre>
        </div>
      )}
    </div>
  );
}

export default App;
