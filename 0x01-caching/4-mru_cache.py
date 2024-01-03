#!/usr/bin/env python3
""" MRUCache module"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache class"""

    def __init__(self):
        """ Initialize the MRU Cache"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item in the cache"""
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                mru_key = self.order.pop()
                del self.cache_data[mru_key]
                print("DISCARD:", mru_key)
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """ Get an item by key"""
        if key is not None:
            if key in self.cache_data:
                self.order.remove(key)
                self.order.append(key)
                return self.cache_data[key]
        return None
