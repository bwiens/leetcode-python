#!/usr/bin/python
# Benjamin Wiens
# Peak Index in a Mountain Array (https://leetcode.com/problems/peak-index-in-a-mountain-array/)

mountain = [0,1,0]

class Solution:
    def peakIndexInMountainArray(self, A):
        for index, number in enumerate(A[1:-1], 1):
            if number > A[index-1] and number > A[index+1]:
                return index

print(Solution().peakIndexInMountainArray(mountain))
