# src/api/todo_routes.py

from flask import Blueprint, request, jsonify
from ..database import db
from ..models.todo_models import User, Task

api_bp = Blueprint('api', __name__)

@api_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data.get('username')
    if not username:
        return jsonify({'error': 'Username is required'}), 400
    user = User(username=username)
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User created', 'user': {'id': user.id, 'username': user.username}}), 201

@api_bp.route('/tasks', methods=['GET'])
def get_tasks():
    user_id = request.args.get('user_id')
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    tasks = Task.query.filter_by(user_id=user_id, parent_id=None).all()
    return jsonify({'tasks': [task.to_dict() for task in tasks]}), 200

# Additional CRUD routes would go here
