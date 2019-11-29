import os
from flask import Flask
from .api import init_blue_print
from atmp.config import config


def create_app():
    app = Flask(__name__)
    env = os.environ.get('FLASK_ENV', 'default')
    app.config.from_object(config.get(env))
    init_blue_print(app)

    return app
