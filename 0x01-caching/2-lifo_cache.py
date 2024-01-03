#!/usr/bin/env python3
""" LIFOCache module"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache class"""

    def __init__(self):
        """ Initialize the LIFO Cache"""
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache"""
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                discarded_key = next(reversed(self.cache_data))
                del self.cache_data[discarded_key]
                print("DISCARD:", discarded_key)
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key"""
        if key is not None:
            return self.cache_data.get(key)
