#!/usr/bin/env python3
""" LFUCache module"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache class"""

    def __init__(self):
        """ Initialize the LFU Cache"""
        super().__init__()
        self.frequency = {}
        self.order = []

    def put(self, key, item):
        """ Add an item in the cache"""
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                min_freq = min(self.frequency.values())
                candidates = [k for k, v in self.frequency.items()
                              if v == min_freq]
                if len(candidates) > 1:
                    lru_key = self.order.pop(0)
                    candidates.remove(lru_key)
                    print("DISCARD:", lru_key)
                discarded_key = candidates[0]
                del self.cache_data[discarded_key]
                del self.frequency[discarded_key]
                print("DISCARD:", discarded_key)

            self.cache_data[key] = item
            self.order.append(key)
            self.frequency[key] = self.frequency.get(key, 0) + 1

    def get(self, key):
        """ Get an item by key"""
        if key is not None:
            if key in self.cache_data:
                self.order.remove(key)
                self.order.append(key)
                self.frequency[key] = self.frequency.get(key, 0) + 1
                return self.cache_data[key]
        return None
