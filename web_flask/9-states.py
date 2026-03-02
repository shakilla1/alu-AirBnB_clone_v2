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
    """Remove current SQLAlchemy session"""
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def states(state_id=None):
    """Displays states and cities"""
    states = list(storage.all(State).values())
    states.sort(key=lambda s: s.name)

    state = None
    cities = None

    if state_id:
        for s in states:
            if s.id == state_id:
                state = s
                if storage.__class__.__name__ == "DBStorage":
                    cities = sorted(s.cities, key=lambda c: c.name)
                else:
                    cities = sorted(s.cities(), key=lambda c: c.name)
                break

        if state is None:
            state = "Not found!"

    return render_template("9-states.html",
                           states=states,
                           state=state,
                           cities=cities)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
