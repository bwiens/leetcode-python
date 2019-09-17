#!/usr/bin/python
# Benjamin Wiens
# Duplicate Zeros (https://leetcode.com/problems/duplicate-zeros)

numbers = [1,0,2,3,0,4,5,0]

class Solution:
    def duplicateZeros(self, arr):
        """
        Do not return anything, modify arr in-place instead.
        """
        length, i = len(arr), 0
        while i < length -1:
            if arr[i] == 0:
                #if we are one prior to last item
                if i == length -2:
                    arr[i+1] = 0
                else:
                    #loop backwards
                    j = length -1
                    while j > i+1:
                        arr[j] = arr[j-1]
                        j -= 1
                    arr[i+1] = 0
                    #skip 2 if changed
                    i += 2
                    continue
            i += 1
        return arr

print(Solution().duplicateZeros(numbers))
