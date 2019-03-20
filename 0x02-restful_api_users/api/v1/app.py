#!/usr/bin/python3
"""
app.py - app file sdklfa sklflasdf lasdflkj sadflk asdfasjk fd
"""
import os
from api.v1.views import app_views
from flask import Flask, jsonify

app = Flask(__name__)
app.register_blueprint(app_views)


@app.errorhandler(404)
def page_not_found(e):
    """ page_not_found() - handle 404 error """
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    envHost = os.environ.get('HBNB_API_HOST')
    envPort = int(os.environ.get('HBNB_API_PORT'))
    app.run(host=envHost, port=envPort)
    import doctest
    doctest.testmod(verbose=True)
