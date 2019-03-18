#!/usr/bin/python3
'''start a flask app'''
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    '''GET index'''
    return "Holberton School"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
