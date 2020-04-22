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


@app.route('/states', strict_slashes=False)
def states():
    states = []
    states = storage.all(State)
    return render_template("9-states.html", States=states)


@app.route('/states/<id>', strict_slashes=False)
def states_city(id):
    states = []
    states = storage.all(State)
    state = ''
    if id:
        for value in states.values():
            if value.id == id:
                state = value.name
                break
    cities = storage.all(City)
    print(state)
    return render_template("9-states.html",
                           States=state,
                           id=id,
                           Cities=cities)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
