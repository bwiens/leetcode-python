#!/usr/bin/python
#Benjamin Wiens
#Maximum Subarray (https://leetcode.com/problems/maximum-subarray/)
#Leetcode Accepted

input = [-2,1,-3,4,-1,2,1,-5,4]

class Solution:
    def maxSubArray(self, nums):
        rolling = nums[0]
        maximum = nums[0]
        for n in nums[1:]:
            rolling = max(n, rolling+n)
            maximum = max(maximum, rolling)
        return maximum

print(Solution().maxSubArray(input))
