#!/usr/bin/python3
"""
Simple Flask application with multiple routes.

Routes:
- / → displays "Hello HBNB!"
- /hbnb → displays "HBNB"
- /c/<text> → displays "C <text>" (underscores replaced with spaces)
"""

from flask import Flask

# Create the Flask application instance
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Return a welcome message."""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Return the text 'HBNB'."""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Display 'C' followed by the provided text.

    Any underscore in the text is replaced with a space.
    """
    text = text.replace('_', ' ')
    return f"C {text}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
