# packages imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

# local imports
from config import app_config


# initialization
db = SQLAlchemy()
login_manager = LoginManager()


def create_app(config_name):
    # flask app & configs
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    # database 
    db.init_app(app)

    # login
    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_view = "auth.login"

    # models
    from app import models

    # migration
    migrate = Migrate(app, db)

    # blueprints
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    # return app object
    return app

