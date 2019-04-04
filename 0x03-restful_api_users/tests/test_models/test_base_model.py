#!/usr/bin/python3
'''tests for base model'''
import datetime
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    '''test base model'''

    def setUp(self):
        '''create new instance'''
        self.base = BaseModel()

    def test_is_BaseModel(self):
        '''test new object is BaseModel instance'''
        self.assertIsInstance(self.base, BaseModel)

    def test_id_exist(self):
        '''test id exists'''
        self.assertIsNotNone(self.base.id)

    def test_id_is_string(self):
        '''test id is string instance'''
        self.assertIsInstance(self.base.id, str)

    def test_id_unique(self):
        '''test id is unique'''
        base2 = BaseModel()
        self.assertNotEqual(self.base.id, base2.id)

    def test_created_exist(self):
        '''test create date exist'''
        self.assertIsNotNone(self.base.created_at)

    def test_created_at_is_datetime(self):
        '''test created_at is datetime instance'''
        self.assertIsInstance(self.base.created_at, datetime.datetime)

    def test_updated_exist(self):
        '''test udpate date exist'''
        self.assertIsNotNone(self.base.updated_at)

    def test_updated_at_is_datetime(self):
        '''test updated_at is datetime instance'''
        self.assertIsInstance(self.base.updated_at, datetime.datetime)
