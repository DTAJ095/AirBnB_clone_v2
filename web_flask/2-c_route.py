#!/usr/bin/python3
""" Starting a Flask web application
The app must be listening on 0.0.0.0:5000
Routes:
    /:display "Hello HBNB!"
    /hbnb: display “HBNB”
    /c/<text>: display “C ”
    followed by the value of the text variable
       (replace underscore _ symbols with a space )
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ Displays Hello HBNB! """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Displays HBNB """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_c(text):
    """ display “C ” followed by the value of the text variable """
    text = text.replace("_", " ")
    return ("C {}".format(text))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
