#!/usr/bin/python3
"""
Simple Flask application.

This app starts a small web server with two routes:
- The root route (/) displays "Hello HBNB!"
- The /hbnb route displays "HBNB"
"""

from flask import Flask

# Create a Flask application instance
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Return a friendly welcome message."""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Return the text 'HBNB'."""
    return "HBNB"


# Run the server on 0.0.0.0:5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
