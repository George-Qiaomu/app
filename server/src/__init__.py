# src/__init__.py

from flask import Flask
from flask_cors import CORS
from .database import db
from .api.todo_routes import api_bp
from flask_sqlalchemy import SQLAlchemy
from .config import Config


def create_app():
    app = Flask(__name__)
    
    # Load configurations
    app.config.from_object(Config)
    
    # Initialize extensions
    CORS(app)
    db.init_app(app)
    
    # Register Blueprints
    app.register_blueprint(api_bp, url_prefix='/api')
    
    return app
