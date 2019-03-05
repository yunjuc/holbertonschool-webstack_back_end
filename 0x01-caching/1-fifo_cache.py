#!/usr/bin/python3
'''FIFOCache module'''
from base_caching import BaseCaching
from datetime import datetime


class FIFOCache(BaseCaching):
    '''FIFOCache classs'''

    def print_cache(self):
        '''print cache'''
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key).get('data')))

    def put(self, key, item):
        '''add item to the cache'''
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data[key]['data'] = item
            self.cache_data[key]['time'] = datetime.now()
            return
        if len(self.cache_data) == self.MAX_ITEMS:
            keys = []
            values = []
            for k, v in self.cache_data.items():
                keys.append(k)
                values.append(v.get('time'))
            index = values.index(min(values))
            first = keys[index]
            del self.cache_data[first]
            print("DISCARD: {}".format(first))
        obj = {}
        obj['data'] = item
        obj['time'] = datetime.now()
        self.cache_data[key] = obj

    def get(self, key):
        '''get item from the cache'''
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key).get('data')
