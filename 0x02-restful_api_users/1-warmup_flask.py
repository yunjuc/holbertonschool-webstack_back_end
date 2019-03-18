#!/usr/bin/python3
'''start a flask app'''
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    '''GET index'''
    return "Holberton School"


@app.route("/c", strict_slashes=False)
def get_c():
    '''GET /c'''
    return "C is fun!"


if __name__ == '__main__':
    app.run(host='0.0.0.0')
