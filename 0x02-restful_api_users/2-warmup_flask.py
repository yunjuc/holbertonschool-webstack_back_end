#!/usr/bin/python3
'''start a flask app'''
import os
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False
host = os.getenv('HBNB_API_HOST')
port = os.getenv('HBNB_API_PORT')


@app.route("/")
def get_index():
    '''GET /'''
    return "Holberton School"


@app.route("/c")
def get_c():
    '''GET /c'''
    return "C is fun!"


if __name__ == '__main__':
    app.run(host=host, port=port)
