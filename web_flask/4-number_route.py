#!/usr/bin/python3
"""0-hello_route module"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display HBNB!"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """c_text"""
    return ('C {}'.format(text.replace('_', ' ')))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is_cool'):
    """python_text"""
    return ('Python {}'.format(text.replace('_', ' ')))


@app.route('/number', strict_slashes=False)
@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    """number_n"""
    return ('{:d} is number'.format(n))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
