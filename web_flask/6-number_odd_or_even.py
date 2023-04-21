#!/usr/bin/python3
"""a flask script to display C and arg passed"""
from flask import Flask, render_template


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


@app.route("/number/<int:n>", strict_slashes=False)
def index_number(n):
    """Return Number passed"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def index_temp(n):
    """Return a template"""
    return render_template("5-number.html", num=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def index_odd_even(n):
    """Returns a template"""
    if n % 2 == 0:
        return render_template("6-number_odd_or_even.html", n=n, msg='is even')
    return render_template("6-number_odd_or_even.html", n=n, msg='is odd')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
