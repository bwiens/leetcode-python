#!/usr/bin/python
# Benjamin Wiens
# Leetcode (https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

numbers = [2,7,11,15]
target = 9
class Solution:
    def twoSum(self, numbers, target):
        l = 0
        r = len(numbers)-1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return (l+1, r+1)
            if s < target:
                l += 1
            else:
                r -= 1
print(Solution().twoSum(numbers,target))
#O(n) time, #O(1) space
