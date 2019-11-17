#!/usr/bin/python
import math
#Benjamin Wiens
#https://leetcode.com/problems/binary-search/
#Leetcode Accepted
input = [-1,0,3,5,9,12]
target = 2
class Solution:
    def search(self, nums, target):
        l = 0
        r = len(nums) -1
        while l <= r:
            m = r + l // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return -1
print(Solution().search(input, target))
