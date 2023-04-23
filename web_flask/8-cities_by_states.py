#!/usr/bin/python3
"""
Flask script that starts the web application
Should display a list of all states in the storage
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def list_states():
    """A function that gets all the states object from db"""
    states_list = storage.all(State)
    return render_template('8-cities_by_states.html',
                           states=states_list)

@app.teardown_appcontext
def teardown_session(exception):
    """removes session after each request"""
    storage.close()


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
