#!/usr/bin/python
# Benjamin Wiens
# Remove Outer Parentheses (https://leetcode.com/problems/remove-outermost-parentheses)
# Leetcode Accepted

input = '(()())'

class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        ballance = 0
        result = ''
        s_list = list(S)
        for bracket in s_list:
            if bracket == '(':
                if ballance > 0:
                    result = result + bracket 
                ballance += 1
            #bracket is ')'
            else: 
                ballance -= 1
                if ballance > 0:
                    result = result + bracket
        return result

print(Solution().removeOuterParentheses(input))
