from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///test.db'

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    age = Column(Integer)

with app.app_context():
    db.drop_all()

with app.app_context():
    db.create_all()

    user_john = User(id=1, name='John', age=30)
    user_jihny = User(id=2, name='Jihny', age=40)
    users = [user_john, user_jihny]

    with db.session.begin():
        db.session.add_all(users)
        db.session.commit()

app.run()