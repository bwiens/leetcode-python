#!/usr/bin/python
#Benjamin Wiens
#Palindrome Numbers (https://leetcode.com/problems/palindrome-number/)
#Leetcode Accepted
input = -131
class Solution:
    def isPalindrome(self, x: 'int') -> 'bool':
        s = str(x)
        s_list = list(s)
        reverse_s = ''
        for i in range(0,len(s_list)):
            reverse_s += s_list.pop()
        if s == reverse_s:
            return True
        else:
            return False
                        
print(Solution().isPalindrome(input))
