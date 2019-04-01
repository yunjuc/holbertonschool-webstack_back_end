#!/usr/bin/python3
'''auth module'''
from flask import request


class Auth():
    '''Auth class'''

    def require_auth(self, path, excluded_paths):
        '''require_auth() - return True if path is not in excluded_paths'''
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path in excluded_paths or path + '/' in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None):
        '''authorization_header() - get authorizatin header'''
        if request is None:
            return None
        if not request.headers.get('Authorization'):
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None):
        '''current_user() - '''
        return None
