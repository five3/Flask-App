from .index import index
from .api import api

bps = [index, api]


def init_blue_print(app):
    for bp in bps:
        app.register_blueprint(bp)
