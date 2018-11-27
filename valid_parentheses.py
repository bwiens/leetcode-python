#!/usr/bin/python
#Benjamin Wiens
#Valid Parentheses (https://leetcode.com/problems/valid-parentheses/solution/)
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        #process from outside inwards with a stack
        for i in s:
            if i == "{" or i == "[" or i == "(":
                stack.append(i)
            #if i in ["}", ")", "]"]:
            elif i == ")":
                if len(stack) == 0:
                    return False
                elif stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            elif i == "]":
                if len(stack) == 0:
                    return False
                elif stack[-1] == "[":
                    stack.pop()
                else:
                    return False
            elif i == "}":
                if len(stack) == 0:
                    return False
                elif stack[-1] == "{":
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False

input = "{[[[()]]]}"
print(Solution().isValid(input))
