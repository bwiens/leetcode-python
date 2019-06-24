#!/usr/bin/python
# Benjamin Wiens
# Max Consecutive Ones (https://leetcode.com/problems/max-consecutive-ones/)
# Leetcode Accepted

input = [1,0,1,1,0,1]

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        ones, maximum = 0, 0
        for number in nums:
            if number == 1:
                ones += 1
            else:
                maximum = max(ones, maximum)
                ones = 0
        maximum = max(ones, maximum)
        return maximum

print(Solution().findMaxConsecutiveOnes(input))

#O(n) time
