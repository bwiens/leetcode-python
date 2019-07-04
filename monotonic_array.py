#!/usr/bin/python
# Benjamin Wiens
# Monotonic Array (https://leetcode.com/problems/monotonic-array/)
# Leetcode Accepted

input = [1,2,2,3]

class Solution:
    def isMonotonic(self, A):
        i = 0
        lower = False
        higher = False
        for number in A[1:]:
            if number < A[i]:
                lower = True
            elif number > A[i]:
                higher = True
            if higher == True and lower == True:
                return False
            i += 1
        return True

print(Solution().isMonotonic(input))
