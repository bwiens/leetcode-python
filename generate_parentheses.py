#!/usr/bin/python
# Benjamin Wiens
# Generate Parenthesis ()
# Leetcode Accepted

n = 3

class Solution:
    def generateParenthesis(self, n):
        # goal: place "(" or ")"
        # constraint: cannot close until we have an open
        # key: result is n*2 brackets
        
        #bruteforce: generate all possible combinations and then validate
        left, right = 0, 0
        result = []
        s = ''
        
        def backtrack(s, left, right):
            if len(s) == 2 * n:
                result.append(s)
                return
            if left < n:
                #do not modify the parameters!
                backtrack(s + '(', left +1, right)
            #only place a right if left is open
            if right < left:
                #do not modify the parameters!
                backtrack(s + ')', left, right+1)
                
        backtrack(s, left, right)
        return result
print(Solution().generateParenthesis(n))
