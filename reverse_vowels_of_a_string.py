#!/usr/bin/python
# Benjamin Wiens
# Reverse Vowels of a String
# https://leetcode.com/problems/reverse-vowels-of-a-string

input = "leetcode"

class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['e', 'a', 'u', 'o', 'i', 'A', 'E', 'U', 'O', 'I']
        s_list = list(s)
        l = 0
        r = len(s_list) - 1
        while l < r:
            if s_list[l] in vowels and s_list[r] not in vowels:
                r -= 1
            elif s_list[r] in vowels and s_list[l] not in vowels:
                l += 1
            elif s_list[r] in vowels and s_list[l] in vowels:
                s_list[r], s_list[l] = s_list[l], s_list[r]
                r -= 1
                l += 1
            #none are in vowels
            else:
                r -= 1
                l += 1
        return ''.join(s_list)

print(Solution().reverseVowels(input))
