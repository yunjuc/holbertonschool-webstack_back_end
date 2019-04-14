#!/usr/bin/python3
'''pymongo module'''
import pymongo


def insert_school(mongo_collection, **kwargs):
    '''insert_school() - insert documenet to collection'''
    new = mongo_collection.insert_one(kwargs)
    return new.inserted_id
