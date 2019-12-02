from manage import init_env_path
from .apps import create_app

init_env_path(__file__)
app = create_app()
