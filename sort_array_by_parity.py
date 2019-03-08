#!/usr/bin/python
#Benjamin Wiens
#Sort Array by Parity (https://leetcode.com/problems/sort-array-by-parity/)
#Leetcode Accepted

nums = [3,1,2,4]

class Solution:
    def sortArrayByParity(self, A):
        if not A: 
            return []
        result = []
        for i in A:
            if i % 2 == 0:
                result.append(i)
        for i in A:
            if i % 2 != 0:
                result.append(i)
        return result

print(Solution().sortArrayByParity(nums))
