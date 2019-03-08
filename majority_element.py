#!/usr/bin/python
#Benjamin Wiens
#Majority Element (https://leetcode.com/problems/majority-element/)
#Leetcode Accepted

nums = [3,2,3]
class Solution:
    def majorityElement(self, nums):
        dict = {}
        length = len(nums)//2
        if len(nums) == 1:
            return nums[0]
        for i in nums:
            if i in dict:
                value = dict.get(i)+1
                if value > length:
                    return i
                dict[i] = value
            else:
                dict[i] = 1

print(Solution().majorityElement(nums))
