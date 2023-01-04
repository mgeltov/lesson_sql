from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///:memory:'

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'))
    group = relationship("Group")

class Group(db.Model):
    __tablename__ = 'group'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    # users = relationship("User")

with app.app_context():
    db.drop_all()

with app.app_context():
    db.create_all()

    group_1 = Group(id=1, name='Group-1')
    group_2 = Group(id=2, name='Group-2')

    user_1 = User(id=1, name='John', age=30, group = group_1)
    user_2 = User(id=2, name='Jihny', age=40, group = group_1)
    user_3 = User(id=3, name='Jim', age=50, group = group_1)
    user_4 = User(id=4, name='Ron', age=60, group = group_2)
    user_5 = User(id=5, name='Bob', age=20, group = group_2)
    user_6 = User(id=6, name='Bill', age=10, group = group_2)

    for_db = [user_1, user_2, user_3, user_4, user_5, user_6]

    with db.session.begin():
        db.session.add_all(for_db)

    query = db.session.query(User).filter(User.name == 'Bill')
    print(query.one().name, '=', query.one().age, 'years')


# app.run()