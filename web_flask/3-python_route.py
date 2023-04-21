#!/usr/bin/python3
"""a flask script to display C and arg passed”"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hbnb():
    """Return Hello HBNB"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def index_hbnb():
    """Return HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def index_text(text):
    """Return HBNB"""
    return "C " + text.replace('_', ' ')


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def index_python(text='is cool'):
    """Return HBNB"""
    return "Python " + text.replace('_', ' ')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
