from flask import Flask
from config import config_options


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])
    app.config['SECRET_KEY'] = 'c3be71c065117cd56d5113506fd6fbf3'

    # registering blueprint
    from .main import main as main_bp
    app.register_blueprint(main_bp, url_prefix='/home')
    from .auth import auth as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/authenticate')

    return app
