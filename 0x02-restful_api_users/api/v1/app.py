#!/usr/bin/python3
'''app module'''
import os
from api.v1.views import app_views
from flask import Flask, jsonify
from models import db_session


app = Flask(__name__)
app.register_blueprint(app_views)
host = os.getenv('HBNB_API_HOST')
port = int(os.getenv('HBNB_API_PORT'))


@app.teardown_appcontext
def close_db(error):
    '''close_db() - close db'''
    db_session.close()


@app.errorhandler(404)
def error_page(e):
    '''error_page() - handle 404 not found'''
    return jsonify({"error": "Not found"}), 404


if __name__ == '__main__':
    app.run(host=host, port=port)
