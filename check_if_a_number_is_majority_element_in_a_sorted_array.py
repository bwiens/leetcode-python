#!/usr/bin/python
# Benjamin Wiens
# Check if a Number is Majority Element in a Sorted Array (https://leetcode.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array/)

nums = [2,4,5,5,5,5,5,6,6]
target = 5

class Solution:
    def isMajorityElement(self, nums, target) -> bool:
        return nums.count(target) > len(nums) //2

print(Solution().isMajorityElement(nums, target))
