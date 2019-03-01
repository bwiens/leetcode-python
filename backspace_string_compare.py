#!/usr/bin/python
#Benjamin Wiens
#Backspace String Compare (https://leetcode.com/problems/backspace-string-compare/submissions/)
#Leetcode Accepted

s = "ab##"
t = "c#d#"
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        c=0
        sstack, tstack, result = [], [], []
        for i in S:
            if i != '#':
                sstack.append(i)
            else:
                #make sure stack is not empty
                if sstack:
                    sstack.pop()
        for i in T:
            if i != '#':
                #make sure stack is not empty
                tstack.append(i)
            else:
                if tstack:
                    tstack.pop()
        if sstack == tstack:
            return True
        else:
            return False
print(Solution().backspaceCompare(s,t))
