#!/usr/bin/python
# Benjamin Wiens
# Maximum Product of Three Numbers (https://leetcode.com/problems/maximum-product-of-three-numbers/)

import sys

numbers = [1,2,3, -100, -100]

class Solution:
    def maximumProduct(self, nums):
        nums.sort(reverse = True)
        return max(nums[0]*nums[1]*nums[2], nums[0]*nums[-1]*nums[(len(nums))-2])

print(Solution().maximumProduct(numbers))
