#!/usr/bin/python
#Benjamin Wiens
#Robot Return to Origin
#https://leetcode.com/problems/robot-return-to-origin/
#Leetcode Accepted

input = "LL"

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        if len(moves) % 2 != 0:
            return False
        x,y = 0, 0
        for move in moves:
            if move == 'U':
                y += 1
            if move == 'D':
                y -= 1
            if move == 'L':
                x -= 1
            if move == 'R':
                x += 1
        if x == 0 and y == 0:
            return True
        return False

print(Solution().judgeCircle(input))
