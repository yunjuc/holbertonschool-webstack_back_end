#!/usr/bin/python3
'''start a flask app'''
import os
from flask import Flask


app = Flask(__name__)
host = os.getenv('HBNB_API_HOST')
port = os.getenv('HBNB_API_PORT')


@app.route("/", strict_slashes=False)
def get_index():
    '''get_index() - GET /'''
    return "Holberton School"


@app.route("/c", strict_slashes=False)
def get_c():
    '''get_c() - GET /c'''
    return "C is fun!"


if __name__ == '__main__':
    app.run(host=host, port=port)
