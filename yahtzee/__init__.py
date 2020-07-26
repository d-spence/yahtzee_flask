import logging
from flask import Flask

logging.basicConfig(level=logging.DEBUG)

SECRET_KEY = 'CE12EA4CF0EA5D3A6C7891F4'

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = SECRET_KEY

    from yahtzee.main.routes import main
    from yahtzee.game.routes import game
    app.register_blueprint(main)
    app.register_blueprint(game)

    return app
    