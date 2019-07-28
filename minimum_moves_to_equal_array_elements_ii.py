#!/usr/bin/python
# Benjamin Wiens
# Minimum Moves to Equal Array Elements II (https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/)

numbers = [1,2,3]

class Solution:
    def minMoves2(self, nums):
        # sort
        nums.sort()
        # find median
        array_length = len(nums)
        if len(nums) % 2 == 0:
            median = (nums[((array_length // 2) - 1)] + nums[array_length // 2]) // 2
        else:
            median = nums[array_length//2]
        # sum of differences to mean
        total = 0
        for number in nums:
            total += abs(number-median)
        return total

print(Solution().minMoves2(numbers))

#O(nlogn)
