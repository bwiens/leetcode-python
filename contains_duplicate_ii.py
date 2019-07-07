#!/usr/bin/python
# Benjamin Wiens
# Contains Duplicate II (https://leetcode.com/problems/contains-duplicate-ii/)
# Leetcode Accepted

input = [1,2,3,1]
k = 3
from collections import OrderedDict
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        hmap = OrderedDict()
        for number in nums:
            if len(hmap) > k:
                hmap.popitem(last=False)
            if number not in hmap:
                hmap[number] = None
            else:
                return True
        return False 

print(Solution().containsNearbyDuplicate(input,k))           
