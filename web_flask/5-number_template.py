#!/usr/bin/python3
"""
Flask web application for HBNB project routes:
0-hello_route up to 5-number_template
Displays text, numbers, and templates with proper routes.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display 'Hello HBNB!' on the root route"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display 'HBNB' on /hbnb route"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Display 'C <text>' on /c/<text> route
    Replaces underscores '_' in <text> with spaces.
    """
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """
    Display 'Python <text>' on /python/<text> route
    Replaces underscores '_' in <text> with spaces.
    Default text is 'is cool'.
    """
    text = text.replace('_', ' ')
    return f"Python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Display '<n> is a number' only if n is an integer"""
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Render template '5-number.html' displaying 'Number: n'
    Only accepts integers, non-integers return 404 automatically
    """
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    """Run the Flask web application"""
    app.run(host='0.0.0.0', port=5000)
