#!/usr/bin/python

string = "abca"

class Solution:
    def isValid(self, s, k, l):
        while k < l:
            if s[k] == s[l]:
                k += 1
                l -= 1
            else:
                return False
        return True
            
    def validPalindrome(self, s):
            
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return self.isValid(s, i+1, j) or self.isValid(s, i, j-1)
        return True
    
print(Solution().validPalindrome(string))
