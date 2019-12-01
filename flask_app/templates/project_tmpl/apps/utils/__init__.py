import os
import argparse
from logging.config import dictConfig


def config_log():
    dictConfig({
        'version': 1,
        'formatters': {
            'default': {
                'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
            }
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'level': 'DEBUG',
                'formatter': 'default'
            },
            'file': {
                'class': 'logging.FileHandler',
                'filename': os.path.join(os.path.dirname(__file__), '../logs/stdout.log'),
                'level': 'INFO',
                'formatter': 'default'
            },
        },
        'root': {
            'level': 'INFO',
            'handlers': ['console', 'file']
        }
    })


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("cmd", help="run app command!")
    parser.add_argument("-p", "--port", help="bind port!", type=int)
    return parser.parse_args()


def get_abs_dir(_file_):
    return os.path.abspath(os.path.dirname(_file_))
