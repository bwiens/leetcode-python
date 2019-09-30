#!/usr/bin/python
# Benjamin Wiens
# Unique Number of Occurrences (https://leetcode.com/problems/unique-number-of-occurrences/)

arr = [-3,0,1,-3,1,1,1,-3,10,0]

from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr):
        hmap = Counter(arr)
        values = {}
        for key, value in hmap.items():
            if value not in values:
                values[value] = 1
            else:
                return False
        return True
        #return len(set(hmap.keys())) == len(set(hmap.values()))

print(Solution().uniqueOccurrences(arr))
