#!/usr/bin/python
# Benjamin Wiens
# Return Squares of a Sorted Array (https://leetcode.com/problems/squares-of-a-sorted-array/)
# Leetcode Accepted

squares = [-4,-1,0,3,10]
class Solution:
    def sortedSquares(self, A):
        result = []
        for i in A:
            x = i * i
            result.append(x)
        return sorted(result)

print(Solution().sortedSquares(squares))
