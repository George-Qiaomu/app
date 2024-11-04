# src/models/todo_models.py

from ..database import db
from sqlalchemy.orm import relationship

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    tasks = relationship('Task', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('task.id'), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    children = relationship('Task')

    def __repr__(self):
        return f'<Task {self.title}>'
