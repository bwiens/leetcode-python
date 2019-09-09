#!/usr/bin/python
#Benjamin Wiens
#https://leetcode.com/problems/happy-number/
input = 3

class Solution:
    def isHappy(self, n: int) -> bool:
        hmap = {}
        while n != 1:
            result = 0
            for char in str(n):
                result += int(char) * int(char)
            if result in hmap:
                return False
            else:
                hmap[result] = None
            n = result
        return True

print(Solution().isHappy(input))
