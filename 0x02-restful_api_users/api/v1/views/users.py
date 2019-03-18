#!/usr/bin/python3
'''index module'''
from api.v1.views import app_views
from flask import jsonify, abort, request, make_response
from models.user import User
from models import db_session


@app_views.route('/users', methods=['GET', 'POST'], strict_slashes=False)
def get_users():
    '''get all users or add a new user'''
    if request.method == 'GET':
        users = User.all()
        return jsonify([user.to_dict() for user in users])
    if request.method == 'POST':
        if not request.json:
            return make_response(jsonify(error='Wrong format'), 400)
        if 'email' not in request.json:
            return make_response(jsonify(error='email missing'), 400)
        if 'password' not in request.json:
            return make_response(jsonify(error='password missing'), 400)
        user = User()
        user.email = request.json.get('email')
        user.password = request.json.get('password')
        user.first_name = request.json.get('first_name')
        user.last_name = request.json.get('last_name')
        try:
            db_session.add(user)
            db_session.commit()
            return make_response(jsonify(user.to_dict()), 201)
        except Exception as e:
            message = "Can't create User: {}".format(e)
            return make_response(jsonify(error=message), 400)


@app_views.route('/users/<user_id>', methods=['GET', 'DELETE', 'PUT'],
                 strict_slashes=False)
def get_user(user_id):
    '''get user info, delete user and udpate user info by id'''
    user = User.get(user_id)
    if user is None:
        abort(404)
    if request.method == 'GET':
        return jsonify(user.to_dict())
    if request.method == 'DELETE':
        db_session.delete(user)
        db_session.commit()
        return jsonify({})
    if request.method == 'PUT':
        if not request.json:
            return make_request(jsonify(error="Wrong format"), 400)
        if request.json.get('first_name'):
            user.first_name = request.json.get('first_name')
        if request.json.get('last_name'):
            user.last_name = request.json.get('last_name')
        db_session.commit()
        return jsonify(user.to_dict())
