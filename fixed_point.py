#!/usr/bin/python
# Benjamin Wiens
# Fixed Point (https://leetcode.com/problems/fixed-point/)
# Leetcode Accepted

numbers = [-10,-5,0,3,7]

class Solution:
       def fixedPoint(self, A):
            l, r = 0, len(A)-1
            while l < r:
                m = l + (r - l) // 2
                #condition not met
                if A[m] == m:
                    return m
                elif A[m] > m:
                    r = m
                else:
                    l = m + 1
            return -1

print(Solution().fixedPoint(numbers))
