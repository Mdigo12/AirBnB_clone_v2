#!/usr/bin/python3
"""
Flask script that starts the web application
Should display a list of all states in the storage
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def list_cities_by_states():
    """A function that gets all the states object from db"""
    states_list = storage.all(State)
    amenity_list = storage.all(Amenity)
    return render_template('10-hbnb_filters.html',
                           states=states_list, amenities=amenity_list)



@app.teardown_appcontext
def teardown_session(exception):
    """removes session after each request"""
    storage.close()


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
