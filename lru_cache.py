#!/usr/bin/python
#Benjamin Wiens
#LRU Cache https://leetcode.com/problems/lru-cache/
#Leetcode Accepted

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.LRU = {}
        self.last_used = []

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # print(LRU.get(key))
        v = self.LRU.get(key)
        if v == None:
            return -1
        # put this key last (append) since we just used it
        else:
            self.last_used.append(self.last_used.pop(self.last_used.index(key)))
        return v

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        #if key already in dict
        if key in self.LRU:
            del self.LRU[key]
            #update
            self.LRU[key] = value
            self.last_used.remove(key)
            self.last_used.append(key)

        #key not in dict yet
        else:
            if len(self.LRU) < self.capacity:
                self.LRU[key] = value
                self.last_used.append(key)

            else:
            #full
                try:
                    del self.LRU[self.last_used[0]]
                except KeyError:
                    print("Key not found")

                del (self.last_used[0])
                self.LRU[key] = value
                self.last_used.append(key)


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
