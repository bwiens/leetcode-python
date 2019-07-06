#!/usr/bin/python
# Contains Duplicates (https://leetcode.com/problems/contains-duplicate)
# Leetcode Accepted

input = [1,2,3,1]

class Solution:
    def containsDuplicate(self, nums):
        hmap = {}
        for number in nums:
            if number in hmap:
                return True
            else:
                hmap[number] = None
        return False

print(Solution().containsDuplicate(input))
