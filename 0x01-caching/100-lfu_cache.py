#!/usr/bin/python3
'''LFUCache module'''
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    '''LFUCache classs'''

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
            self.cache_data[key]['count'] += 1
            return
        if len(self.cache_data) == self.MAX_ITEMS:
            keys = []
            values = []
            for k, v in sorted(self.cache_data.items()):
                keys.append(k)
                values.append(v.get('count'))
            index = values.index(min(values))
            least = keys[index]
            del self.cache_data[least]
            print("DISCARD: {}".format(least))
        obj = {}
        obj['data'] = item
        obj['count'] = 0
        self.cache_data[key] = obj

    def get(self, key):
        '''get item from the cache'''
        if key is None or self.cache_data.get(key) is None:
            return None
        self.cache_data[key]['count'] += 1
        return self.cache_data.get(key).get('data')
