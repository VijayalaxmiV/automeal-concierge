import { useEffect, useState } from "react";
import axios from "axios";

type HealthResponse = {
  status: string;
  project: string;
  version: string;
};

function App() {
  const [health, setHealth] = useState<HealthResponse | null>(null);

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/health")
      .then((response) => setHealth(response.data))
      .catch((error) => console.error(error));
  }, []);

  return (
    <div
      style={{
        maxWidth: "700px",
        margin: "50px auto",
        fontFamily: "Arial, sans-serif",
      }}
    >
      <h1>🍽️ AutoMeal Concierge</h1>

      <hr />

      {health ? (
        <div>
          <h2>Backend Status</h2>

          <p>
            <strong>Status:</strong> {health.status}
          </p>

          <p>
            <strong>Project:</strong> {health.project}
          </p>

          <p>
            <strong>Version:</strong> {health.version}
          </p>
        </div>
      ) : (
        <p>Connecting to backend...</p>
      )}
    </div>
  );
}

export default App;