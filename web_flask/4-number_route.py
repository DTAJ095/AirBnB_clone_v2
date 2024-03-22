#!/usr/bin/python3
""" Starting a Flask web application
The app must be listening on 0.0.0.0:5000
Routes:
    /:display "Hello HBNB!"
    /hbnb: display “HBNB”
    /c/<text>: display “C ” followed by the value of the text variable
       (replace underscore _ symbols with a space )
    /python/<text>: display “Python ”, followed by the value of the text variable
    /number/<n>: display “n is a number” only if n is an integer
"""
from flask import Flask
from flask import abort

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

@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def display_py(text="is cool"):
    """ display “Python ”, followed by the value of
    the text variable
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)

@app.route("/number/<int:n>", strict_slashes=False)
def display_num(n):
    """ display 'n is a number' only if n is an integer """
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")