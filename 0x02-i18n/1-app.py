#!/usr/bin/env python3
""" Flask app """
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """ Config class """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_TIMEZONE = "UTC"
    BABEL_DEFAULT_LOCALE = "en"


babel = Babel(app)
app.config.from_object(Config)


@app.route('/', strict_slashes=False)
def index() -> str:
    """ Returns the index page """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
