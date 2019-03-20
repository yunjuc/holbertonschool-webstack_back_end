#!/usr/bin/python3
'''start a flask app'''
from flask import Flask, jsonify
import os

app = Flask(__name__)
host = os.getenv('HBNB_API_HOST')
port = int(os.getenv('HBNB_API_PORT'))

data = {"C": "is fun", "Python": "is cool", "Sysadmin": "is hiring"}


@app.route("/hbtn", strict_slashes=False)
def get_hbtn():
    '''get_hbtn() - GET /hbtn'''
    return jsonify(data)


if __name__ == '__main__':
    app.run(host=host, port=port)
