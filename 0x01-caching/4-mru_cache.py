#!/usr/bin/python3
'''MRUCache module'''
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    '''MRUCache classs'''
    count = 0

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
            self.count += 1
            self.cache_data[key]['data'] = item
            self.cache_data[key]['count'] = self.count
            return
        if len(self.cache_data) == self.MAX_ITEMS:
            keys = []
            values = []
            for k, v in self.cache_data.items():
                keys.append(k)
                values.append(v.get('count'))
            index = values.index(max(values))
            most = keys[index]
            del self.cache_data[most]
            print("DISCARD: {}".format(most))
        self.count += 1
        obj = {}
        obj['data'] = item
        obj['count'] = self.count
        self.cache_data[key] = obj

    def get(self, key):
        '''get item from the cache'''
        if key is None or self.cache_data.get(key) is None:
            return None
        self.count += 1
        self.cache_data[key]['count'] = self.count
        return self.cache_data.get(key).get('data')
