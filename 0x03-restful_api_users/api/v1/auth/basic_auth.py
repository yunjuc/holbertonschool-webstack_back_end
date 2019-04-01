#!/usr/bin/python3
'''basic_auth module'''
from flask import request
from api.v1.auth.auth import Auth
from models import db_session
from models.user import User
import base64


class BasicAuth(Auth):
    '''BasicAuth class'''

    def extract_base64_authorization_header(self, authorization_header):
        '''extract_base64_authorization_header() - return basic header'''
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if authorization_header.split()[0] != 'Basic':
            return None
        return authorization_header.split()[1]

    def decode_base64_authorization_header(self, base64_authorization_header):
        '''decode_base64_authorization_header() - decode header'''
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) is not str:
            return None
        try:
            return base64.b64decode(base64_authorization_header)\
                   .decode('utf-8')
        except Exception:
            pass

    def extract_user_credentials(self, decoded_base64_authorization_header):
        '''extract_user_credentials() - return decoded user/password'''
        if decoded_base64_authorization_header is None:
            return None, None
        if type(decoded_base64_authorization_header) is not str:
            return None, None
        if(':' in decoded_base64_authorization_header) is False:
            return None, None
        s = decoded_base64_authorization_header.split(':')
        return s[0], s[1]

    def user_object_from_credentials(self, user_email, user_pwd):
        '''user_object_from_credentials() - create user object'''
        if user_email is None or type(user_email) is not str:
            return None
        if user_pwd is None or type(user_pwd) is not str:
            return None
        user = db_session.query(User).filter_by(email=user_email).first()
        if not user:
            return None
        if user.is_valid_password(user_pwd) is False:
            return None
        return user

    def current_user(self, request=None):
        '''current_user() - return user'''
        request_header = self.authorization_header(request)
        base64_header = self.extract_base64_authorization_header(
                        request_header)
        decode_header = self.decode_base64_authorization_header(base64_header)
        user_info = self.extract_user_credentials(decode_header)
        user = self.user_object_from_credentials(user_info[0], user_info[1])
        return user
