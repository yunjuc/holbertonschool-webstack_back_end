#!/usr/bin/python3
'''start a flask app'''
import os
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def get_index():
    '''get_index() - GET /'''
    return "Holberton School"


@app.route("/c", strict_slashes=False)
def get_c():
    '''get_c() - GET /c'''
    return "C is fun!"


if __name__ == '__main__':
    vhost = os.getenv('HBNB_API_HOST')
    vport = int(os.getenv('HBNB_API_PORT'))
    app.run(host=vhost, port=vport)
