# Benjamin Wiens
# Insert Delete GetRandom O(1) (https://leetcode.com/problems/insert-delete-getrandom-o1)
# Leetcode Accepted

import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hmap = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.hmap:
            self.hmap[val] = None
            return True
        else:
            return False
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.hmap:
            del self.hmap[val]
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        #print(list(self.hmap.keys()))
        return random.choice(list(self.hmap.keys()))
