#!/usr/bin/python
# Benjamin Wiens
# Longest Continuous Increasing Subsequence (https://leetcode.com/problems/longest-continuous-increasing-subsequence)

numbers = [1,3,5,4,7]
class Solution:
    def findLengthOfLCIS(self, nums):
        rolling, i, result = 0, 0, 0
        while i < len(nums):
            rolling = 1
            while i+1 <= len(nums)-1:
                if nums[i] < nums[i+1]:
                    rolling += 1
                    i +=1
                else:
                    break
            i+= 1
            result = max(rolling, result)
        return result

print(Solution().findLengthOfLCIS(numbers))
