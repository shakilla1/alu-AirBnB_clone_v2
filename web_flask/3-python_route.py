#!/usr/bin/python3
"""
Flask application with multiple dynamic routes.

Routes:
- / → displays "Hello HBNB!"
- /hbnb → displays "HBNB"
- /c/<text> → displays "C <text>" (underscores replaced with spaces)
- /python/<text> → displays "Python <text>"
  If no text is provided, default text is "is cool"
"""

from flask import Flask

# Create the Flask application
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
    """Display 'C' followed by the provided text."""
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route('/python/', defaults={'text': 'is cool'},
           strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """Display 'Python' followed by the provided text."""
    text = text.replace('_', ' ')
    return "Python {}".format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
