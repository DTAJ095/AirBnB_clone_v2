#!/usr/bin/python3
""" Starting flask application
The app must be listening on 0.0.0.0, port 5000
Routes:
    /states_list: display a HTML page with the list of states
"""
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def list_state():
    """ Displays an HTML page with the list of states """
    states = storage.all('State')
    return render_template('7-states_list.html', states=states)


@app.teardwon_appcontext
def teardown(exc):
    """ Removes the current sqlalchemy session """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
