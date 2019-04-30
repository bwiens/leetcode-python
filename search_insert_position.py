#!/usr/bin/python
# Benjamin Wiens
# Search Insert Position (https://leetcode.com/problems/search-insert-position/)
# Leetcode Accepted

numbers = [1,3,5,6]
target = 2

class Solution:
    def searchInsert(self, nums, target):
        for index, num in enumerate(nums):
            if num == target:
                return index
            if target < num:
                return index
        return len(nums)

print(Solution().searchInsert(numbers, target))            
