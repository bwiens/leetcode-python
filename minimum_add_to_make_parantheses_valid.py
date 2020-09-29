#!/usr/bin/python
# Benjamin Wiens
# Minimum Add to Make Parentheses Valid (https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/)

brackets = "()))(("

class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        stacksize = 0
        miss_match = 0
        for char in S:
            if char == ')':
                if stacksize > 0:
                    stacksize -= 1
                else:
                    miss_match += 1
            elif char == '(':
                stacksize += 1
        return stacksize + miss_match

print(Solution().minAddToMakeValid(brackets))
