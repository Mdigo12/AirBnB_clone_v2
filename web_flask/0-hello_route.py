#!/usr/bin/python3
"""a flask script to display `Hello HBNB!`"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index_hbnb():
    """returns `hello HBNB!`"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
