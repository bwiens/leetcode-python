#!/usr/bin/python

s = "leEeetcode"

class Solution:
    def makeGood(self, s):
        stack = []
        for char in s: 
            # upper char
            if stack and stack[-1].isupper() and stack[-1].lower() == char:
                stack.pop()
            # lower char
            elif stack and stack[-1].islower() and stack[-1].upper() == char:
                if char.isupper():
                    stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)
    
print(Solution().makeGood(s))
