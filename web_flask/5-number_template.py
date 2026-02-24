#!/usr/bin/python3
"""5-number_template.py: Flask app to display integers via templates"""

from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display 'Hello HBNB!' on the root route"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display 'HBNB' on the /hbnb route"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Display 'C <text>' where underscores in <text> are replaced by spaces
    Example: /c/hello_world => 'C hello world'
    """
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """
    Display 'Python <text>' where underscores in <text> are replaced by spaces.
    Default text is 'is cool' if not provided
    Example: /python/awesome => 'Python awesome'
    """
    text = text.replace('_', ' ')
    return f"Python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    Display '<n> is a number' only if n is an integer.
    Routes like /number/3.5 or /number/abc will give 404
    """
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Render an HTML template displaying 'Number: n' in an H1 tag.
    Only accepts integers, invalid inputs give 404.
    """
    return render_template('5-number.html', n=n)


# Run the Flask app on 0.0.0.0:5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
