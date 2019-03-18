#!/usr/bin/python3
'''tests for user model'''
import unittest
from models.base_model import BaseModel
from models.user import User


class TestUserModel(unittest.TestCase):
    '''test user model'''

    def setUp(self):
        '''create new instance'''
        self.user = User()
        self.betty = User()
        self.betty.first_name = "Betty"
        self.betty.last_name = "Holberton"
        self.betty.email = "betty@holberton.com"

    def test_is_BaseModel(self):
        '''test new object is BaseModel instance'''
        self.assertIsInstance(self.user, BaseModel)

    def test_is_User(self):
        '''test new object is User instance'''
        self.assertIsInstance(self.user, User)

    def test_empty_user(self):
        '''test no email or first and last name'''
        self.assertEqual(self.user.display_name(), "")

    def test_empty_name(self):
        '''test only has email'''
        self.user.email = "test@gmail.com"
        self.assertEqual(self.user.display_name(), self.user.email)

    def test_empty_frist_name(self):
        '''test first name is None'''
        self.user.last_name = "Jane"
        self.assertEqual(self.user.display_name(), "Jane")

    def test_empty_last_name(self):
        '''test last name is None'''
        self.user.first_name = "Mary"
        self.assertEqual(self.user.display_name(), "Mary")

    def test_display__name(self):
        '''test display full name'''
        self.user.first_name = "Mary"
        self.user.last_name = "Jane"
        self.assertEqual(self.user.display_name(), "Mary Jane")

    def test_str_empty(self):
        '''print when user is empty'''
        self.assertEqual(str(self.user), "[User] {} - {} - {}"
                         .format(self.user.id, None, ""))

    def test_str_has_email(self):
        '''print when user has only email'''
        self.user.email = "test@gmail.com"
        self.assertEqual(str(self.user), "[User] {} - {} - {}"
                         .format(self.user.id, self.user.email,
                                 self.user.display_name()))

    def test_str_has_name(self):
        '''print when user has both email and name'''
        self.user.email = "test@gmail.com"
        self.user.first_name = "Mary"
        self.user.last_name = "Jane"
        self.assertEqual(str(self.user), "[User] {} - {} - {}"
                         .format(self.user.id, self.user.email,
                                 self.user.display_name()))

    def test_default_password(self):
        '''when no password is set'''
        self.assertEqual(self.user._password, None)

    def test_set_password_not_str(self):
        '''when set password with none str'''
        self.user.password = 888
        self.assertEqual(self.user._password, None)

    def test_password_none(self):
        '''check when no password'''
        res = self.user.is_valid_password('hello')
        self.assertEqual(res, False)

    def test_password_not_str(self):
        '''check non str password'''
        self.user.password = 'hello'
        res = self.user.is_valid_password(888)
        self.assertEqual(res, False)

    def test_password_empty(self):
        '''check password is none'''
        self.user.password = 'hello'
        res = self.user.is_valid_password(None)
        self.assertEqual(res, False)

    def test_wrong_password(self):
        '''check wrong password'''
        self.user.password = 'hello'
        res = self.user.is_valid_password('world')
        self.assertEqual(res, False)

    def test_corrret_password(self):
        '''check correct password'''
        self.user.password = 'hello'
        res = self.user.is_valid_password('hello')
        self.assertEqual(res, True)

    def test_is_dict(self):
        '''check if to_dict return dict'''
        self.assertIsInstance(self.betty.to_dict(), dict)

    def test_is_str_id(self):
        '''check if id exists'''
        self.assertTrue(self.betty.to_dict()['id'])

    def test_is_str_email(self):
        '''check if email exists'''
        self.assertTrue(self.betty.to_dict()['email'])

    def test_is_str_first_name(self):
        '''check if first name exists'''
        self.assertTrue(self.betty.to_dict()['first_name'])

    def test_is_str_last_name(self):
        '''check if last name exists'''
        self.assertTrue(self.betty.to_dict()['last_name'])

    def test_is_str_created_at(self):
        '''check if created_at exists'''
        self.assertTrue(self.betty.to_dict()['created_at'])

    def test_is_str_updated_at(self):
        '''check if updated_at exists'''
        self.assertTrue(self.betty.to_dict()['updated_at'])
