from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .routes import *
from .models import db

def create_app():
    app = Flask(__name__, static_folder='static')
    app.config.from_object(Config)

    # Initialize database
    db.init_app(app)
    migrate = Migrate(app, db)

    # Register routes
    register_routes(app)
    
    from app import routes, models
    
    return app
