#!/usr/bin/python3
"""
Flask application that displays all States and their Cities.
- States are sorted alphabetically by name.
- Cities within each State are also sorted alphabetically.
- Works with DBStorage and FileStorage.
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """Remove the current SQLAlchemy session after each request"""
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """
    Render an HTML page with:
    - All State objects sorted by name
    - Their associated City objects, sorted by name
    """
    all_states = storage.all(State)

    states = sorted(
        all_states.values(),
        key=lambda s: s.name if s.name else ""
    )

    state_cities = {}
    for state in states:
        if hasattr(state, 'cities'):
            cities = state.cities
            if type(cities) != list:
                cities = cities()
        else:
            getter = getattr(state, 'cities', None)
            cities = getter() if callable(getter) else []

        state_cities[state.id] = sorted(
            cities,
            key=lambda c: c.name if c.name else ""
        )

    return render_template(
        "8-cities_by_states.html",
        states=states,
        state_cities=state_cities
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
