#!/usr/bin/python3
'''start a flask app'''
from flask import Flask, jsonify
import os

app = Flask(__name__)
host = os.getenv('HBNB_API_HOST')
port = int(os.getenv('HBNB_API_PORT'))


@app.route("/", strict_slashes=False)
def get_index():
    '''get_index() - GET /'''
    return "Holberton School"


@app.route("/c", strict_slashes=False)
def get_c():
    '''get_c() - GET /c'''


@app.route("/hbtn", strict_slashes=False)
def get_hbtn():
    '''get_hbtn() - GET /hbtn'''
    data = {"C": "is fun", "Python": "is cool", "Sysadmin": "is hiring"}
    return jsonify(data)


if __name__ == '__main__':
    app.run(host=host, port=port)
