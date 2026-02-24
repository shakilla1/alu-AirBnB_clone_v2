#!/usr/bin/python3
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
    states = storage.all(State)
    states_list = list(states.values())
    states_list.sort(key=lambda s: s.name)
    selected_state = None
    if state_id:
        for state in states_list:
            if state.id == state_id:
                selected_state = state
                break
    return render_template('9-states.html', states=states_list, selected_state=selected_state)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
