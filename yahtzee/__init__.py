from flask import Flask


def create_app():
    app = Flask(__name__)

    from yahtzee.main.routes import main
    from yahtzee.game.routes import game
    app.register_blueprint(main)
    app.register_blueprint(game)

    return app
    