#!/usr/bin/python3
'''start a flask app'''
from flask import Flask, jsonify
import os

app = Flask(__name__)
app.url_map.strict_slashes = False
host = os.getenv('HBNB_API_HOST')
port = os.getenv('HBNB_API_PORT')

data = {"C": "is fun", "Python": "is cool", "Sysadmin": "is hiring"}


@app.route("/hbtn")
def get_hbtn():
    '''get_hbtn() - GET /hbtn'''
    return jsonify(data)


if __name__ == '__main__':
    app.run(host=host, port=port)
