from flask import Flask, jsonify, abort
from flask_cors import CORS
from flask_restful import Api
from sqlalchemy.sql.expression import func
from database import db, init_db, load_question, Question

# Maak de Flask app aan in een aparte functie
def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    api = Api(app)
    CORS(app)
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
    question = Question.query.order_by(func.random()).first()

    if not question:
        abort(404, description="No questions found")
    return jsonify({
        'id': question.id,
        'question': question.question,
        'answer': question.answer,
        'category': question.category
    })

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    load_question(app, 'data/quizvragen.csv')  

    app.run(debug=True)
