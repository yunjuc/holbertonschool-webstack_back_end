#!/usr/bin/python3
"""
app.py - app file sdklfa sklflasdf lasdflkj sadflk asdfasjk fd
"""
import os
from api.v1.views import app_views
from flask import Flask, jsonify
from models import db_session


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_db(error):
    '''close_db() - close database after api call'''
    db_session.close()


@app.errorhandler(404)
def page_not_found(e):
    """ page_not_found() - handle 404 error """
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    host = os.environ.get('HBNB_API_HOST')
    port = int(os.environ.get('HBNB_API_PORT'))
    app.run(host=host, port=port)
    doctest.testmod(verbose=True)
