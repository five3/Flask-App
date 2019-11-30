from apps.utils import parse_args, init_env_path

init_env_path(__file__)

from flask_app.apps import create_app

__all__ = ['main']


def main():
    app = create_app()
    args = parse_args()
    port = args.port if args.port else 8080
    app.run('0.0.0.0', port)
    app.logger.info(f'run server at port {port}')


if __name__ == '__main__':
    main()
