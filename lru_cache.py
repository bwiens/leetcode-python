#!/usr/bin/python
#Benjamin Wiens
#LRU Cache https://leetcode.com/problems/lru-cache/

LRU = {}
last_used = []
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        capacity = 2
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        #print(LRU.get(key))
        v = LRU.get(key)
        #put this key last (append) since we just used it
        if key in last_used:
            last_used.append(last_used.pop(last_used.index(key)))
        return v

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if len(LRU) < 2:
            LRU[key] = value
            last_used.append(key)
        else:
            del_key = last_used[0]
            del LRU[del_key]
            del last_used[0]
            LRU[key] = value
            last_used.append(key)

LRUCache(2).put(1, 1)
LRUCache(2).put(2, 2)
print(LRUCache(2).get(1)) #returns 1
LRUCache(2).put(3, 3) #evicts 2
print(LRUCache(2).get(2)) #returns None
LRUCache(2).put(4, 4) #evicts key 1
print(LRUCache(2).get(1)) #returns None
print(LRUCache(2).get(3)) #returns 3
print(LRUCache(2).get(4)) #returns 4
