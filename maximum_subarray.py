#!/usr/bin/python
#Benjamin Wiens
#Maximum Subarray (https://leetcode.com/problems/maximum-subarray/)
#Leetcode Accepted

input = [-2,1,-3,4,-1,2,1,-5,4]

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum = nums[0]
        rolling_max = nums[0]
        for e in nums[1:]:
            #we can drop the rolling max when 
            #the current element is bigger
            rolling_max = max(e, rolling_max+e)
            if maximum < rolling_max:
                maximum = rolling_max
        return maximum

print(Solution().maxSubArray(input))
