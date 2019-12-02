import os
import logging
from flask import Flask
from .{% app_name %} import init_blue_print
from .utils import config_log
from {% project_name %}.config import config, G


def create_app():
    config_log()
    app = Flask(__name__)
    env = os.environ.get('FLASK_ENV', 'default')
    app.config.from_object(config.get(env))

    logger = logging.getLogger('flask.app.module')
    G.logger = logger

    init_blue_print(app)

    return app
