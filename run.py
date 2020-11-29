import os

from app import create_app

config_name = 'production' if os.getenv('FLASK_CONFIG') is None else os.getenv('FLASK_CONFIG')
app = create_app(config_name)


if __name__ == '__main__':
    app.run()