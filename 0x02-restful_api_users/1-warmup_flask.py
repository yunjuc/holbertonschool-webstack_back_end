#!/usr/bin/python3
'''start a flask app'''
from flask import Flask


app = Flask(__name__)


@app.route("/c", strict_slashes=False)
def get_c():
    '''get_c() - GET /c'''
    return "C is fun!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
