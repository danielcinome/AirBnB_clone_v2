#!/usr/bin/python3
""" List of states """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
app = Flask(__name__)


@app.teardown_appcontext
def teardown_app_context(self):
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    states = []
    states = storage.all(State)
    cities = storage.all(City)
    amenities = storage.all(Amenity)
    places = storage.all(Place)
    return render_template("100-hbnb.html",
                           States=states,
                           Cities=cities,
                           Amenity=amenities,
                           Place=places)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
