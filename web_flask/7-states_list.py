#!/usr/bin/python3
""" Starting flask application """
from flask import Flask, render_template
from models import *
from models import storage

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def list_state():
    """ Displays an html page with all states ilsted """
    states = sorted(list(storage.all('State').values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(exception):
    """ Remove the current sqlalchemy session """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
