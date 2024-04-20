from flask_sqlalchemy import SQLAlchemy
from flask import Flask
db = SQLAlchemy()
# Create our database model

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    dob = db.Column(db.Date)
    created_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())
