#!/usr/bin/python
# Benjamin Wiens
# Increasing Triplet Subsequence (https://leetcode.com/problems/increasing-triplet-subsequence/)

import sys
input = [1,2,3,4,5]

class Solution:
    def increasingTriplet(self, nums):
        first, second = sys.maxsize, sys.maxsize
        for number in nums:
            # don't count duplicates the equal is the key
            if number <= first:
                first = number
            elif number <= second:
                second = number
            elif number > first and number > second:
                return True
        return False

print(Solution().increasingTriplet(input))
