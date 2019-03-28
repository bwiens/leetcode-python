#!/usr/bin/python
#Benjamin Wiens
#House Robber (https://leetcode.com/problems/house-robber/)
#Leetcode Accepted
houses = [1,2,3,1]

class Solution:
    def rob(self, nums):
        # bottom-up processing
        # if 1 or 0
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        #check how much money can be robbed up to ith house
        dp = {}
        dp[0] = nums[0]
        #select max of first two
        dp[1] = max(nums[0], nums[1])
        #start at index 2, 
        for i in range(2,len(nums)):
            #starting 3rd house, do we rob 1st and current house, or the second house?
            dp[i] = max((dp[i-2]+nums[i]),dp[i-1])
        return dp[len(nums)-1]

print(Solution().rob(houses))
