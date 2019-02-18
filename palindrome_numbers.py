#!/usr/bin/python
#Benjamin Wiens
#Palindrome Numbers (https://leetcode.com/problems/palindrome-number/)
#Leetcode Accepted
input = -131
class Solution:
    def isPalindrome(self, x: 'int') -> 'bool':
        s = str(x)
        if len(s) == 1:
            return True
        s2 = s[::-1]
        for index, i in enumerate(s):
            if i != s2[index]:
                return False
        return True
                       
print(Solution().isPalindrome(input))
