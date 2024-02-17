#!/usr/bin/python3
""""new thing"""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    """
    first page
    """
    return "Hello HBNB!"

@app.route("/hbnb")
def hello_world():
    """
    first page
    """
    return "HBNB"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    