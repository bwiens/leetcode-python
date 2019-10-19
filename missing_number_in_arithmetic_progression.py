#!/usr/bin/python
# Benjamin Wiens
# Missing Number in Arithmetic Progression (https://leetcode.com/problems/missing-number-in-arithmetic-progression/)

arr = [15,13,12] 

class Solution:
    def missingNumber(self, arr):
        stride = (arr[-1] - arr[0]) // len(arr)
        for index, number in enumerate(arr[1:], 1):
            if number - arr[index-1] != stride:
                return number - stride
        return arr[0]

print(Solution().missingNumber(arr))
