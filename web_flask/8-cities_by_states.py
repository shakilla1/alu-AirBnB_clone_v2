#!/usr/bin/python3
"""
Flask app to display all States and their Cities.
Works with both DBStorage and FileStorage.
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """Remove current SQLAlchemy session"""
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """Render HTML page with states and their cities"""
    all_states = storage.all(State)
    states = sorted(all_states.values(), key=lambda s: s.name if s.name else "")

    # Map state_id -> sorted list of cities
    state_cities = {}
    for state in states:
        if hasattr(state, "cities") and not callable(state.cities):
            # DBStorage
            cities = state.cities
        elif hasattr(state, "cities") and callable(state.cities):
            # FileStorage
            cities = state.cities()
        else:
            cities = []

        # sort cities alphabetically by name
        state_cities[state.id] = sorted(cities, key=lambda c: c.name if c.name else "")

    return render_template(
        "8-cities_by_states.html",
        states=states,
        state_cities=state_cities
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
