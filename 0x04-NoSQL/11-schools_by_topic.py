#!/usr/bin/python3
'''pymongo module'''
import pymongo


def schools_by_topic(mongo_collection, topic):
    '''schools_by_topic() - search school with certain topics'''
    return mongo_collection.find({'topics': topic})
