from flask_sqlalchemy import SQLAlchemy
import pandas as pd

db = SQLAlchemy()

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(255), nullable=False)
    answer = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<Question {self.question}>'

def init_db(app):
    db.init_app(app)

def load_question(app, file):
    with app.app_context():
        #db.session.query(Question).delete()
        #db.session.commit()
        df = pd.read_csv(file)
        for index, row in df.iterrows():
            existing_question = Question.query.filter_by(question=row['Vraag']).first()
            if not existing_question:
                question = Question(
                    question=row['Vraag'],
                    answer=row['Antwoord'],
                    category=row['Categorie']
                )
                db.session.add(question)
        db.session.commit()