#!/usr/bin/python
# Benjamin Wiens
# Array Transformation (https://leetcode.com/problems/array-transformation/)

input = [2,1,2,1,1,2,2,1] 

class Solution:
    def transformArray(self, arr):
        changes = True
        while changes:
            changes = False
            arr_copy = arr[:]
            for index, number in enumerate(arr[1:-1], 1):

                if number < arr_copy[index-1] and number < arr_copy[index+1]:
                    arr[index] = number + 1
                    changes = True
                if number > arr_copy[index-1] and number > arr_copy[index+1]:
                    arr[index] = number - 1
                    changes = True
        return arr

print(Solution().transformArray(input))
