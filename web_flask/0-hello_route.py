#!/usr/bin/python3
#new one
from flask import Flask
""""
new thing
"""
app = Flask(__name__)

@app.route("/")
def hello_world():
    """
    first page
    """
    return "<p>Hello HBNB!</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)