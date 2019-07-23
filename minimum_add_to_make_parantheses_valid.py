#!/usr/bin/python
# Benjamin Wiens
# Minimum Add to Make Parentheses Valid (https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/)

brackets = "()))(("

class Solution:
    def minAddToMakeValid(self, S):
        result, left = 0, 0
        for bracket in S:
            if bracket == '(':
                left += 1
            elif bracket == ')':
                if left == 0:
                    result += 1
                else:
                    left -= 1
        return left + result

print(Solution().minAddToMakeValid(brackets))
