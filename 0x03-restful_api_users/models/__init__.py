#!/usr/bin/python3
'''engine config'''
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base, BaseModel
from models.user import User

db_engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                          .format(os.getenv('HBNB_YELP_MYSQL_USER'),
                                  os.getenv('HBNB_YELP_MYSQL_PWD'),
                                  os.getenv('HBNB_YELP_MYSQL_HOST'),
                                  os.getenv('HBNB_YELP_MYSQL_DB')))

if os.getenv('HBNB_YELP_ENV') == 'test':
    Base.metadata.drop_all(db_engine)

Base.metadata.create_all(db_engine)

factory = sessionmaker(bind=db_engine, expire_on_commit=False)
Session = scoped_session(factory)
db_session = Session()
