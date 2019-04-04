#!/usr/bin/python3
"""
app.py - app module
"""
import os
from api.v1.views import app_views
from flask import Flask, jsonify, request, abort
from models import db_session
from api.v1.auth.auth import Auth
from api.v1.auth.basic_auth import BasicAuth


app = Flask(__name__)
app.register_blueprint(app_views)
app.url_map.strict_slashes = False

if os.environ.get('HBNB_YELP_AUTH') == 'basic_auth':
    auth = BasicAuth()
else:
    auth = Auth()


@app.before_request
def before_request():
    ''''before_request() - check auth route'''
    paths = ['/api/v1/status/', '/api/v1/unauthorized/', '/api/v1/forbidden/']
    if auth.require_auth(request.path, paths) is False:
        return
    if auth.authorization_header(request) is None:
        abort(401)
    if auth.current_user(request) is None:
        abort(403)


@app.errorhandler(404)
def page_not_found(e):
    """ page_not_found() - handle 404 error """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(e):
    """ unauthorized() - handle 401 error """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(e):
    """ forbidden() - handle 401 error """
    return jsonify({"error": "Forbidden"}), 403


@app.teardown_appcontext
def close_db(error):
    '''close_db() - close database after api call'''
    db_session.close()


if __name__ == "__main__":
    host = os.environ.get('HBNB_API_HOST')
    port = int(os.environ.get('HBNB_API_PORT'))
    app.run(host=host, port=port)
