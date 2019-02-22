#!/usr/bin/python
#Benjamin Wiens
#Missing Number (https://leetcode.com/problems/missing-number/)
#Leetcode Accepted
input = [3,0,1]
class Solution:
    def missingNumber(self, nums: 'List[int]') -> 'int':
        nums = sorted(nums, reverse=True)
        if nums == [0]:
            return 1
        if nums == [1]:
            return 0
        for index, i in enumerate(nums):
            if index + 1 <= len(nums) -1:
                if i - nums[index+1] > 1:
                    return i - 1
        if nums[-1] != 0:
            return 0
        else:
            return nums[0] + 1
print(Solution().missingNumber(input))
