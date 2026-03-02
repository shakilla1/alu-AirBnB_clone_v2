#!/usr/bin/python3
"""
Starts a Flask web application
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def states(state_id=None):

    if state_id is None:
        states = sorted(storage.all(State).values(),
                        key=lambda s: s.name)
        return render_template("9-states.html",
                               states=states,
                               state=None,
                               cities=None)

    state = storage.all(State).get("State." + state_id)

    if state is None:
        return render_template("9-states.html",
                               states=None,
                               state="Not found!",
                               cities=None)

    if storage.__class__.__name__ == "DBStorage":
        cities = sorted(state.cities, key=lambda c: c.name)
    else:
        cities = sorted(state.cities(), key=lambda c: c.name)

    return render_template("9-states.html",
                           states=None,
                           state=state,
                           cities=cities)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
