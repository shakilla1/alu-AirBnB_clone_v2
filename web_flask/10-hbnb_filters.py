#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)

@app.teardown_appcontext
def teardown(exception):
    """Close the storage session after each request"""
    storage.close()

@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Render HBNB filters page"""
    states = list(storage.all(State).values())
    amenities = list(storage.all(Amenity).values())
    states.sort(key=lambda s: s.name)
    amenities.sort(key=lambda a: a.name)
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
