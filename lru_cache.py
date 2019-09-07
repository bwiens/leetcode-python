#!/usr/bin/python
#Benjamin Wiens
#LRU Cache https://leetcode.com/problems/lru-cache/
#Leetcode Accepted

from collections import OrderedDict
class LRUCache:
    """discards the least recenlty used item first"""    
    def __init__(self, capacity: int):
        """set capacity"""
        self.capacity = capacity
        self.odict = OrderedDict()
    def get(self, key: int):
        if len(self.odict) > 0:
            if key in self.odict:
                tmp = self.odict.get(key)
                #insert again, to put least recently used at the bottom
                del self.odict[key]
                self.odict[key] = tmp
                return tmp
            else:
                return -1
        else:
            return -1
    def put(self, key: int, value: int) -> None:
        #update the key if it already exists
        if key in self.odict:
            del self.odict[key]
            self.odict[key] = value
        elif len(self.odict) >= self.capacity:
	    #this is the key to pop the item that was least recently used (!)
            self.odict.popitem(last=False)
            self.odict[key] = value
        else:
            self.odict[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

object = LRUCache(2)
print(object.get(2))
object.put(2,6)
print(object.get(1))
object.put(1,5)
object.put(1,2)
print(object.get(1))
print(object.get(2))

#["LRUCache","get","put","get","put","put","get","get"]
#[[2],[2],[2,6],[1],[1,5],[1,2],[1],[2]]
