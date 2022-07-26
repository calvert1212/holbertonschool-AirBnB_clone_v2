#!/usr/bin/python3
"""
Starts a Flask web application.
"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """
    Displays "Hello HBNB!" on main page.
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Displays HBNB message
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """
    Displays "C" followed by <text>. Underscores delimited as white space.
    """
    return "C {}".format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
