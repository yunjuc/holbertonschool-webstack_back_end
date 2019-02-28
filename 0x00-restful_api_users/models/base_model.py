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
