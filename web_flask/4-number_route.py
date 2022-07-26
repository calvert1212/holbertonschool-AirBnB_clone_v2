#!/usr/bin/python3
"""
Starts a Flask web application.
"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """
    Displays "Hello HBNB!" on the main page.
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Displays "HBNB"
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """
    Displays "C" followed by <text>. '_'
    replaced with whitespace.
    """
    return "C {}".format(text.replace('_', ' '))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text='is cool'):
    """
    Displays "Python" followed by the text in <text>. If
    no text is provided, default is "is cool". All
    underscores replaced with whitespace.
    """
    return "Python {}".format(text.replace('_', ' '))


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """
    Displays "is a number" after <n> if <n> is an integer.
    """
    return "%d is a number" % n


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
