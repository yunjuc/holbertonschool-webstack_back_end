#!/usr/bin/python3
'''base model module'''
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()


class BaseModel:
    '''BaseModel class'''
    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self):
        '''constructor'''
        self.id = str(uuid.uuid4())
        self.created_at = str(datetime.utcnow())
        self.updated_at = str(datetime.utcnow())

    @classmethod
    def all(cls):
        '''return all instances of a class'''
        from models import db_session

        objs = db_session.query(cls).order_by(cls.created_at.asc()).all()
        return objs

    @classmethod
    def count(cls):
        '''count number of instances of a class'''
        from models import db_session

        n = db_session.query(cls).count()
        return n

    @classmethod
    def get(cls, id):
        '''return all instances of a class'''
        from models import db_session

        if id is None or type(id) != str:
            return None
        obj = db_session.query(cls).filter(cls.id == id).first()
        if obj is None:
            return None
        return obj

    @classmethod
    def first(cls):
        '''return an instanc by'''
        from models import db_session

        obj = db_session.query(cls).order_by(cls.created_at.asc()).first()
        if obj is None:
            return None
        return obj

    @classmethod
    def last(cls):
        '''return last instance of a class'''
        from models import db_session

        obj = db_session.query(cls).order_by(cls.created_at.desc()).first()
        return obj
