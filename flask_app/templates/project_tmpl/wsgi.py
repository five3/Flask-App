from .manage import init_python_path
from .apps import create_app

init_python_path(__file__)
app = create_app()
