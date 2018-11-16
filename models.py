"""
Dublin Route Planner Prototype
Author: Paul Durack
"""

from app import db
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(80))
    leap_user = db.Column(db.String(15), unique=True)
    leap_pass = db.Column(db.String(15), unique=True)
