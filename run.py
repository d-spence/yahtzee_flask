# Python/Flask Yahtzee App -- Play Yahtzee through a flask web application.

from yahtzee import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
    