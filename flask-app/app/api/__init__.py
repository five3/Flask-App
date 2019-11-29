from .index import index
from .datasource import datasource

bps = [index, datasource]


def init_blue_print(app):
    for bp in bps:
        app.register_blueprint(bp)
