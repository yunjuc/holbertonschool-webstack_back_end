#!/usr/bin/python3
'''pymongo module'''
import pymongo


def update_topics(mongo_collection, name, topics):
    '''update_topics() - update documenet data'''
    return mongo_collection.update({'name': name}, {'$set': {'topics': topics}})
