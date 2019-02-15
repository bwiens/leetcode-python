#!/usr/bin/python
#Benjamin Wiens
#https://leetcode.com/problems/happy-number/
#Leetcode Accepted
input = 3
class Solution:
    def happyAux(self, n, dict) -> 'bool':
        y=0
        for i in str(n):
            y += int(i) **2
        if y == 1:
            return True
        else:
            if y in dict:
                return False
            else:
                dict[y] = None
                return self.happyAux(y, dict)
    def isHappy(self, n: 'int') -> 'bool':
        dict = {}
        return self.happyAux(n, dict)
print(Solution().isHappy(input))
