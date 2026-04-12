"use client";

import { useState } from "react";

export default function Home() {
  const [result, setResult] = useState<any>(null);

  const sendFirmware = async () => {
    const res = await fetch("http://localhost:8000/firmware", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        request_id: "fw-1",
        drone_type: "quad",
        firmware: {
          commit_hash: "abc123"
        }
      })
    });

    const data = await res.json();
    setResult(data);
  };

  const sendOperator = async () => {
    const res = await fetch("http://localhost:8000/operator", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        message_id: "op-1",
        operator_id: "pilot_007"
      })
    });

    const data = await res.json();
    setResult(data);
  };

  const sendInsurer = async () => {
    const res = await fetch("http://localhost:8000/insurer", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        message_id: "ins-1",
        insurer_id: "ins_company"
      })
    });

    const data = await res.json();
    setResult(data);
  };

  return (
    <main style={{ padding: 20 }}>
      <h1>🚁 Regulator Control Panel</h1>

      <button onClick={sendFirmware}>Test Firmware</button>
      <br /><br />

      <button onClick={sendOperator}>Certify Operator</button>
      <br /><br />

      <button onClick={sendInsurer}>Insurance Check</button>

      <pre>{JSON.stringify(result, null, 2)}</pre>
    </main>
  );
}