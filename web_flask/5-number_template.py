#!/usr/bin/python3
"""
Flask application with dynamic routes and templates.

Routes:
- / → "Hello HBNB!"
- /hbnb → "HBNB"
- /c/<text> → "C <text>"
- /python/<text> → "Python <text>" (default: "is cool")
- /number/<n> → "<n> is a number"
- /number_template/<n> → Render HTML page if n is an integer
"""

from flask import Flask, render_template

# Create Flask application instance
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Return welcome message."""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Return 'HBNB'."""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Display 'C' followed by text."""
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route('/python/', defaults={'text': 'is cool'},
           strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """Display 'Python' followed by text."""
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Display number only if n is integer."""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Render HTML template displaying the number."""
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
