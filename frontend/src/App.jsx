import { useState } from "react";
import "./App.css";

function App() {
  const [file, setFile] = useState(null);
  const [uploadResult, setUploadResult] = useState(null);

  const handleUpload = async () => {
    if (!file) {
      alert("Choose a log file first, sweetheart.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await fetch("http://127.0.0.1:8000/logs/upload", {
        method: "POST",
        body: formData,
      });

      if (!response.ok) throw new Error("Upload failed");

      const data = await response.json();
      setUploadResult(data);
    } catch (error) {
      alert("Backend down. I’ll fix it, you rest.");
      console.error(error);
    }
  };

  const handleExport = () => {
    if (!uploadResult?.parsed_logs) return;
    const blob = new Blob([uploadResult.parsed_logs.join("\n")], { type: "text/plain" });
    const url = URL.createObjectURL(blob);
    const link = document.createElement("a");
    link.href = url;
    link.download = "suspicious_logs.txt";
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  return (
    <div className="matrix-bg">
      <div className="hacker-glass">
        <h1 className="glow-title">ATHENA<span>_</span></h1>
        <h2 className="tagline">Threat Log Uploader</h2>

        <input
          type="file"
          onChange={(e) => setFile(e.target.files[0])}
          className="hacker-input"
        />

        <div className="button-group">
          <button onClick={handleUpload} className="hacker-btn">Upload 🔥</button>
          {uploadResult && (
            <button onClick={handleExport} className="hacker-btn export">Export 📁</button>
          )}
        </div>

        {uploadResult && (
          <div className="results-box">
            <h3 className="result-heading">{uploadResult.message}</h3>
            <ul className="log-lines">
              {uploadResult.parsed_logs?.map((line, index) => (
                <li key={index}>
                  <span className="timestamp">[{new Date().toLocaleTimeString()}]</span> {line}
                </li>
              ))}
            </ul>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
