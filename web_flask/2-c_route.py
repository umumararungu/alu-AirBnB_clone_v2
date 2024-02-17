#!/usr/bin/python3
"""second task"""
from flask import Flask
from markupsafe import escape

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

    return f'C,{escape(text)}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
