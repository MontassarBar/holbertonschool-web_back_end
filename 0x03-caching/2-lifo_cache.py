#!/usr/bin/python3
'''LIFOCache class'''

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    '''inherits from BaseCaching and is a caching system'''
    def __init__(self):
        self.rm = ""
        super().__init__()

    def put(self, key, item):
        ''' assign to the dictionary self.cache_data
            the item value for the key'''
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            print(self.rm)
            if key not in self.cache_data.keys():
                print("DISCARD:", self.rm)
                del(self.cache_data[self.rm])
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.rm = key

    def get(self, key):
        '''return the value in self.cache_data linked to key'''
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        else:
            return None
