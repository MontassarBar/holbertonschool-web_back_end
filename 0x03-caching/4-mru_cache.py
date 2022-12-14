#!/usr/bin/python3
'''MRUCache class'''

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    '''inherits from BaseCaching and is a caching system'''
    def __init__(self):
        self.rm = []
        super().__init__()

    def put(self, key, item):
        ''' assign to the dictionary self.cache_data
            the item value for the key'''
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if key not in self.cache_data.keys():
                print("DISCARD:", self.rm[len(self.rm) - 1])
                del(self.cache_data[self.rm[len(self.rm) - 1]])
                del(self.rm[len(self.rm) - 1])
        if key is not None and item is not None:
            self.cache_data[key] = item
            for k in range(0, len(self.rm) - 1):
                if self.rm[k] == key:
                    del(self.rm[k])
            self.rm.append(key)

    def get(self, key):
        '''return the value in self.cache_data linked to key'''
        if key is not None and key in self.cache_data.keys():
            for k in range(0, len(self.rm) - 1):
                if self.rm[k] == key:
                    del(self.rm[k])
            self.rm.append(key)
            return self.cache_data[key]
        else:
            return None
