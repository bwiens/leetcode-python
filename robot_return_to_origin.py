#!/usr/bin/python
#Benjamin Wiens
#Robot Return to Origin
#https://leetcode.com/problems/robot-return-to-origin/
#Leetcode Accepted

input = "UDLR"

class Solution:
    def judgeCircle(self, move):
        """
        :param move: str
        :return: bool
        """
        u, d, l, r = 0, 0, 0, 0
        if len(move) % 2 != 0:
            return False
        for i in move:
            if i == "U":
                u+=1
            if i == "D":
                d += 1
            if i == "L":
                l += 1
            if i == "R":
                r += 1
        if u == d and l == r:
            return True
        else:
            return False


print(Solution().judgeCircle(input))
