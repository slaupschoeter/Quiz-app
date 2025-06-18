import React, { useEffect, useState } from 'react'
import axios from 'axios';

interface Question {
  id: number
  question: string
  answer: string
  category: string
}

const App: React.FC = () => {
  // 2. Gebruik een generieke useState met Question of null
  const [question, setQuestion] = useState<Question | null>(null)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    // 3. Geef de verwachte response-type mee aan axios.get
    axios
      .get<Question>('http://127.0.0.1:5000/questions')
      .then(response => {
        setQuestion(response.data)
      })
      .catch(err => {
        console.error(err)
        setError('Kan vraag niet laden')
      })
  }, [])

  if (error) {
    return <p>{error}</p>
  }

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
  )
}

export default App