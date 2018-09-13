from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


# creating instances of flask extensions by initializing the flask extenstions
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
# telling the login manager where it should operate from
login_manager.login_view = 'auth.login'


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])
    app.config['SECRET_KEY'] = 'c3be71c065117cd56d5113506fd6fbf3'

    # initializing flask extentions to the app by calling the initapp method on then and passing the app as the arguments to the app
    db.init_app(app)
    login_manager.init_app(app)

    # registering blueprint
    from .main import main as main_bp
    app.register_blueprint(main_bp, url_prefix='/home')
    from .auth import auth as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/authenticate')

    return app
