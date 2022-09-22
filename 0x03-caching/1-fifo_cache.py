#!/usr/bin/python3
'''FIFOCache class'''

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    '''inherits from BaseCaching and is a caching system'''
    def put(self, key, item):
        ''' assign to the dictionary self.cache_data
            the item value for the key'''
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if key not in self.cache_data.keys():
                print("DISCARD:", list(self.cache_data.keys())[0])
                del(self.cache_data[(list(self.cache_data.keys())[0])])
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        '''return the value in self.cache_data linked to key'''
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        else:
            return None
