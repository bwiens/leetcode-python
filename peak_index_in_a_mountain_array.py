#!/usr/bin/python
# Benjamin Wiens
# Peak Index in a Mountain Array (https://leetcode.com/problems/peak-index-in-a-mountain-array/)

mountain = [0,1,0]

class Solution:
    def peakIndexInMountainArray(self, A):
        left = 0
        right = len(A) -1
        while left < right:
            m = (left+right)//2
            if A[m] > A[m-1] and A[m] > A[m+1]:
                return m
            elif A[m] < A[m+1]:
                left = m + 1
            else:
                right = m

print(Solution().peakIndexInMountainArray(mountain))
