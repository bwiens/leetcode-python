#!/usr/bin/python
#Benjamin Wiens
#Longest Palindromic Substring (https://leetcode.com/problems/longest-palindromic-substring/)
#Leetcode Accepted

string = "babad"

class Solution:
    def longestPalindrome(self, s: str) -> str:
        i2 = 1
        temp_sub, max_sub = '',''
        if not s:
            return ''
        if len(s) == len(set(s)):
            return s[0]
        #go through s, expand window and store the subsequence, overwrite if there's larger subsequence
        for j in range(0,len(s)):
            while i2 <= len(s) -1:
                s1 = s[j:i2+1]
                s2 = s1[::-1]
                if s1 == s2:
                    temp_sub = s1
                i2+=1
            else:
                if len(max_sub) < len(temp_sub):
                    max_sub = temp_sub
                    temp_sub = ''
            i2 = 1
        return max_sub
print(Solution().longestPalindrome(string))
