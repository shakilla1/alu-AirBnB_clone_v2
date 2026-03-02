#!/usr/bin/python3
"""
Flask application that displays a list of all State objects.
The list is sorted alphabetically by state name.
Uses storage engine (DBStorage or FileStorage) to fetch data.
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """Remove the current SQLAlchemy session after each request"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Render an HTML page with all State objects sorted by name"""
    all_states = storage.all(State)
    states = sorted(all_states.values(), key=lambda s: s.name if s.name else "")
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
