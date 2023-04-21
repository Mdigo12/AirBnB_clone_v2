from flask import Flask, render_template

app = Flask(__name__)
@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays Hello HBNB!"""
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays HBNB!"""
    return "HBNB!"

@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    """Displays C and the value of {text}"""
    return 'C' + text.replace("_", " ")

@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_is_cool(text='is cool'):
    """Displays Python and the value of {text}, by default text=<is cool>"""
    return 'Python ' + text.replace("_", " ")

@app.route("/number/<int:n>", strict_slashes=False)
def is_a_number(n):
    """Displays only integers, testing how to pass datatypes"""
    return '{n} is a number'

@app.route("/number_template/<int:n>", strict_slashes=False)
def index_is_num(n):
    return render_template("5-number.html", n=n)

@app.route("/number_odd_or_even/<int:n>>", strict_slashes=False)
def index_odd_even(n):
    if n % 2 == 0:
        return render_template("6-number_odd_or_even.html", n=n, text="is even")
    return render_template("6-number_odd_or_even.html", n=n, text="is odd")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
