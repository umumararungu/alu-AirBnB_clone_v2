#!/usr/bin/python3
""""new thing"""
from flask import Flask, render_template
from models import storage
from models.state import State
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the database again at the end of the request."""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Displays a list of states"""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda x: x.name)

    return render_template('7-states_list.html', states=sorted_states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
