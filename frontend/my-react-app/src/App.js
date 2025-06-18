import React, { Suspense, useEffect, useState } from 'react';
import axios from 'axios';

export default function App() {
  const [q, setQ] = useState(null)
  useEffect(() => {
    axios.get('http://127.0.0.1:5000/questions')
      .then(r => setQ(r.data))
      .catch(e => console.error(e))
  }, [])

  return (
    <div className="App">
      {question ? (
        <div>
          <h2>Vraag #{question.id}</h2>
          <p>{question.question}</p>
          <small>Categorie: {question.category}</small>
        </div>
      ) : (
        <p>Loading…</p>
      )}
    </div>
  );
}
