#!/usr/bin/python3
""" List of states """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
app = Flask(__name__)


@app.teardown_appcontext
def teardown_app_context(self):
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def states_list():
    states = []
    states = storage.all(State)
    cities = storage.all(City)
    return render_template("8-cities_by_states.html",
                           States=states, Cities=cities)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
