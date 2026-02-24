#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.teardown_appcontext
def teardown_db(exception):
    storage.close()

@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    all_states = storage.all(State).values()
    states = sorted(all_states, key=lambda state: state.name)
    return render_template('8-cities_by_states.html', states=states)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
