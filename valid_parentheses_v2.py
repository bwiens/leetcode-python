#!/usr/bin/python
#Benjamin Wiens
#Valid Parentheses (https://leetcode.com/problems/valid-parentheses/solution/)
#Leetcode Accepted

input = "{[[[()]]]}"

class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 
        hmap = {')': '(', ']':'[', '}': '{'}
        for bracket in s:
            if bracket in hmap:
                if not stack:
                    return False
                else:
                    if stack[-1] == hmap[bracket]:
                        stack.pop()
                    else:
                        return False
            else:
                stack.append(bracket)
        if not stack:
            return True
        else:
            return False
                    
print(Solution().isValid(input))
