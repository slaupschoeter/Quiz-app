from flask import Flask, jsonify
from flask_restful import Api
from database import db, init_db, load_question, Question

# Maak de Flask app aan in een aparte functie
def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    api = Api(app)

    # Initialiseer de database
    init_db(app)

    return app

# Maak de app aan
app = create_app()

# Hoofdroutes
@app.route('/')
def home():
    return "Backend is working!"

@app.route('/questions', methods=['GET'])
def get_questions():
    questions = Question.query.all()
    questions_list = []

    for question in questions:
        questions_list.append({
            'id': question.id,
            'question': question.question,
            'answer': question.answer,
            'category': question.category
        })
    return jsonify(questions_list)

if __name__ == '__main__':
    # Maak de database en tabellen aan (indien nodig)
    with app.app_context():
        db.create_all()
    # Laad de vragen uit het CSV-bestand in de database
    load_question(app, 'data/quizvragen.csv')  # Vervang dit door het pad naar je CSV-bestand

    # Start de server
    app.run(debug=True)
