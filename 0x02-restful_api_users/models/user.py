#!/usr/bin/python3
'''user model module'''
import hashlib
from datetime import datetime
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String


class User(BaseModel, Base):
    '''User model class'''
    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    _password = Column(String(128), nullable=False)

    def display_name(self):
        '''display name of user'''
        if self.email is None and self.first_name is None and\
           self.last_name is None:
            return ""
        elif self.first_name is None and self.last_name is None:
            return self.email
        elif self.last_name is None:
            return self.first_name
        elif self.first_name is None:
            return self.last_name
        return "{} {}".format(self.first_name, self.last_name)

    def __str__(self):
        '''string representation'''
        return "[User] {} - {} - {}".format(self.id, self.email,
                                            self.display_name())

    @property
    def password(self):
        '''_password getter'''
        return self._password

    @password.setter
    def password(self, value):
        '''_password setter'''
        if value is None or type(value) != str:
            self._password = None
        else:
            m = hashlib.md5()
            m.update(value.encode('utf-8'))
            self._password = m.hexdigest()

    def is_valid_password(self, pwd):
        '''check if password is valid'''
        if pwd is None or type(pwd) != str or self.password is None:
            return False
        else:
            m = hashlib.md5()
            m.update(pwd.encode('utf-8'))
            if self.password == m.hexdigest():
                return True
            else:
                return False

    def to_dict(self):
        '''serialize user instance'''
        obj = {}
        obj['id'] = str(self.id)
        obj['email'] = str(self.email)
        obj['first_name'] = str(self.first_name)
        obj['last_name'] = str(self.last_name)
        obj['created_at'] = str(datetime.strftime(self.created_at,
                                                  '%Y-%m-%d %H:%M:%S'))
        obj['updated_at'] = str(datetime.strftime(self.updated_at,
                                                  '%Y-%m-%d %H:%M:%S'))
        return obj
