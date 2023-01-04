from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
import json

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

@app.route("/users/first")
def get_first_user():
    user = User.query.first()
    return json.dumps({
        "id": user.id,
        "name": user.name,
        "age": user.age
    })

@app.route("/users/count")
def get_count():
    user_count = User.query.count()
    return json.dumps(user_count)

@app.route("/users")
def get_users():
    users = User.query.all()
    users_list = []
    for user in users:
        users_list.append({
        "id": user.id,
        "name": user.name,
        "age": user.age
    })
    return json.dumps(users_list)

@app.route("/users/<int:sid>")
def get_user_by_id(sid):
    user = User.query.get(sid)
    if user is None:
        return f"User with id {sid} is not found"
    else:
        user ={
            "id": user.id,
            "name": user.name,
            "age": user.age
        }
        return json.dumps(user)

app.run()