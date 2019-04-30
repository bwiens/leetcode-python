#!/usr/bin/python
# Benjamin Wiens
# Guess Number Higher or Lower 
# Leetcode Accepted (https://leetcode.com/problems/guess-number-higher-or-lower/)

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        right = n
        left = 1
        while left <= right:
            m =  (left + right) // 2
            result = guess(m)
            if result == 0: 
                return m
            elif result == -1:
                right = m - 1
            else:
                left = m + 1
        return -1
