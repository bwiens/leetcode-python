#!/usr/bin/python
# Benjamin Wiens
# Leetcode (https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

numbers = [2,7,11,15]
target = 9
class Solution:
    def twoSum(self, numbers, target):
        right = len(numbers) - 1
        left = 0
        while left < right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers [right] > target: 
                right -= 1
            else:
                return [left+1,right+1]
print(Solution().twoSum(numbers,target))
#O(n) time, #O(1) space
