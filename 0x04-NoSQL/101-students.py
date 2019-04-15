#!/usr/bin/python3
'''pymongo module'''
import pymongo


def top_students(mongo_collection):
    '''top_students() - return stuents and sort by socre'''
    return mongo_collection.aggregate([{'$unwind': '$topics'},
                                       {'$group': {'_id': '$_id',
                                        'name': {'$first': '$name'},
                                        'averageScore':
                                        {'$avg': '$topics.score'}}},
                                       {'$sort': {'averageScore': -1}}])
