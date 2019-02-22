#!/usr/bin/python
#Benjamin Wiens
#Climbing Stairs (https://leetcode.com/problems/climbing-stairs/)
#Leetcode Accepted
input = 38
class Solution:
    stairsdict = {}
    def calc(self, n):
        if n in self.stairsdict:
            return self.stairsdict.get(n)
        elif n == 0 or n == 1:
            return 1
        else:
            value = self.calc(n-1) + self.calc(n-2) 
            self.stairsdict[n] = value
            return self.calc(n-1) + self.calc(n-2)
        
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = self.calc(n)
        return result
print(Solution().climbStairs(input))
