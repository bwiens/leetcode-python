#!/usr/bin/python
# Benjamin Wiens
# Minimum Moves to Equal Array Elements (https://leetcode.com/problems/minimum-moves-to-equal-array-elements/)
import sys 

numbers = [1,1,2147483647]

class Solution:
    def minMoves(self, nums):
        min_nr = sys.maxsize
        moves = 0
        for number in nums:
            moves += number
            min_nr = min(min_nr, number)
        return moves - min_nr * len(nums)

print(Solution().minMoves(numbers))
