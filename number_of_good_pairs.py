#!/usr/bin/python

import collections
nums = [1,2,3,1,1,3]
class Solution:
    def numIdenticalPairs(self, nums) -> int:
        result = 0
        count = collections.Counter(nums)
        for value in count.values():
            if value > 1:
                result += value * (value -1) // 2 
        return result

print(Solution().numIdenticalPairs(nums))
