#!/usr/bin/python3
"""second task"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """first page"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """second page"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def C_fun(text):
    """C page"""
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def Python_fun(text="is cool"):
    """ Python page"""

    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def numbers(n):
    """Number page"""
    return '{} is a number'.format(n)

@app.route("/number_template/<int:n>", strict_slashes=False)
def html(n):
    """Html page"""
    return render_template('templates/5-number_template.html', number=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
