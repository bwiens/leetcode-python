#!/usr/bin/python
# Benjamin Wiens
# Reverse Substrings Between Each Pair of Parantheses (https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/)

s = "(u(love)i)"

class Solution:
    def reverseParentheses(self, s):
        stack = ['']
        for char in s:
            # start if of a sub string
            if char == '(':
                stack.append('')
            # end of a sub string
            elif char == ')':
                add = stack.pop()[::-1]
                stack[-1] += add
            else:
                stack[-1] += char
        return stack.pop()

print(Solution().reverseParentheses(s))
