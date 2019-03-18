#!/usr/bin/python3
'''index module'''
from api.v1.views import app_views
from flask import jsonify
from models.user import User


@app_views.route('/status', strict_slashes=False)
def get_status():
    '''get_status() - get ok status'''
    return jsonify(status='OK')


@app_views.route('/stats', strict_slashes=False)
def get_stats():
    '''get_stats() - get number of User'''
    return jsonify(users=User.count())
