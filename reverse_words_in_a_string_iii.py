#!/usr/bin/python
# Benjamin Wiens
# Reverse Words in a String III (https://leetcode.com/problems/reverse-words-in-a-string-iii/)

input = "Let's take LeetCode contest"

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ''
        s_list = s.split()
        for word in s_list:
            word = word[::-1]
            result = result + ' ' + word
        return result[1:]

print(Solution().reverseWords(input))
