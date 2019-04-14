#!/usr/bin/python3
'''pymongo module'''
import pymongo


def list_all(mongo_collection):
    '''list_all() - list documenets in the collection'''
    return mongo_collection.find()
