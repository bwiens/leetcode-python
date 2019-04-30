#!/usr/bin/python
# Benjamin Wiens
# Find Pivot Index (https://leetcode.com/problems/find-pivot-index/)
# Leetcode Accepted

numbers = [1, 7, 3, 6, 5, 6]

class Solution:
    def pivotIndex(self, nums):
        if not nums:
            return -1
        total, lhs = 0, 0
        for num in nums:
            total += num
        for index, num in enumerate(nums):
            if lhs == total - num - lhs:
                return index
            lhs += num
        return -1
            
print(Solution().pivotIndex(numbers))            
            
            
