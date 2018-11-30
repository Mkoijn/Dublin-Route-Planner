"""
Dublin Route Planner Prototype
Author: Paul Durack
"""

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_heroku import Heroku

app = Flask(__name__)

app.config.from_pyfile('config.py')

Bootstrap(app)
heroku = Heroku(app)
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

from views import *
from errors.handlers import errors
app.register_blueprint(errors)

if __name__ == '__main__':
    app.run()
