import React, { useEffect, useState } from 'react'
import axios from 'axios';
import './App.css'

interface Question {
  id: number
  question: string
  answer: string
  category: string
}

const App: React.FC = () => {
  const [question, setQuestion] = useState<Question | null>(null)
  const [error, setError] = useState<string | null>(null)
  const [showAnswer, setShowAnswer] = useState<Boolean | null>(false)

  useEffect(() => {
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
    {error && <p>{error}</p>}

    {!error && (
      question ? (
        <div>
          <h2>Vraag #{question.id}</h2>
          <p>{question.question}</p>
          <small>Categorie: {question.category}</small>

          {/* knop om antwoord te tonen */}
          {!showAnswer ? (
            <button onClick={() => setShowAnswer(true)}>
              Toon Antwoord
            </button>
          ) : (
            <p><strong>Antwoord:</strong> {question.answer}</p>
          )}
        </div>
      ) : (
        <p>Loading…</p>
      )
    )}
  </div>
)
}

export default App