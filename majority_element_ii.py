#!/usr/bin/python
# Benjamin Wiens
# Majority Element II (https://leetcode.com/problems/majority-element-ii/)

input = [1,1,1,3,3,2,2,2]

from collections import Counter
class Solution:
    def majorityElement(self, nums):
        count = Counter(nums)
        result = []
        for key, value in count.items():
            if value > len(nums) // 3:
                result.append(key)
        return result

print(Solution().majorityElement(input))
