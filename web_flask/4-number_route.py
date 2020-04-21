#!/usr/bin/python3
""" Web Flask Aplication """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text='is cool'):
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>')
def number_route(n):
    return '{} is a number'.format(n)

app.run(host="0.0.0.0", port=5000)
