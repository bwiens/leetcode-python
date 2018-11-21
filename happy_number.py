#!/usr/bin/python
#Benjamin Wiens
#https://leetcode.com/problems/happy-number/
import math
input = 19
class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        sum = 0
        #create a hash table
        numbers = dict(enumerate(str(input)))
        while sum != 1:
            sum = 0
            #take the square
            for key, value in numbers.items():
                sum += int(value) * int(value)
            #update the hash table
            numbers = dict(enumerate(str(sum)))
        return True

print(Solution().isHappy(input))
