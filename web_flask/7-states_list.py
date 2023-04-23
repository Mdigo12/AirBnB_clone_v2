#!/usr/bin/python3
"""
Flask script that starts the web application
Should display a list of all states in the storage
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def list_states():
    """A function that renders a sorted list of states in db"""
    states_list = storage.all(State)
    states_list_sort = sorted(states_list.values(),
                              key=lambda state: state.name)
    return render_template('7-states_list.html', states=states_list_sort)


@app.teardown_appcontext
def teardown_session(exception):
    """removes session after each request"""
    storage.close()


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
