#!/usr/bin/python
#Benjamin Wiens
#Valid Parentheses (https://leetcode.com/problems/valid-parentheses/solution/)
#Leetcode Accepted

input = "{[[[()]]]}"

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for bracket in s:
            if bracket in ["(", "{", "["]:
                stack.append(bracket)
            #if stack is empty, stop
            elif not stack:
                return False
            elif bracket == ")":
                if stack[-1] in ["{", "["]:
                    return False
                else: 
                    stack.pop()
            elif bracket == "}":
                if stack[-1] in ["(", "["]:
                    return False
                else: 
                    stack.pop()
            elif bracket == "]":
                if stack[-1] in ["(", "{"]:
                    return False
                else: 
                    stack.pop()
                    
        if not stack:
            return True
        else:
            return False

print(Solution().isValid(input))
