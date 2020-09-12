import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Get the directory path of our file
basedir = os.path.abspath(os.path.dirname(__file__))

# Create a path to our sqlite file based on the directory path above
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Wrap our Flask-Alchemy instance around our Flask Application
db = SQLAlchemy(app)

from app import routes, db

from app.models import Task

db.drop_all()
db.create_all()

tasks = [
    'Eat some food',
    'Listen to some music',
    'Read a book',
]

for task in tasks:
    new_task = Task(name=task, description='')
    db.session.add(new_task)
db.session.commit()