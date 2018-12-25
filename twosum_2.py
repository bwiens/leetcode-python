#!/usr/bin/python
#Benjamin Wiens
#Two Sum (Non-BruteForce) https://leetcode.com/problems/two-sum
#Leetcode Accepted 
nums = [2, 7, 11, 15]
target = 9
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for index, i in enumerate(nums):
            if target - i in dict:
                return dict[target - i], index
            dict[i] = index

print(Solution().twoSum(nums, target))
