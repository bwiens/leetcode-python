#!/usr/bin/python
# Benjamin Wiens
# Reverse Vowels of a String
# https://leetcode.com/problems/reverse-vowels-of-a-string
# Leetcode Accepted

input = "leetcode"

class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['e', 'a', 'u', 'o', 'i', 'A', 'E', 'U', 'O', 'I']
        s_list = list(s)
        stack = []
        for i in s_list:
            if i in vowels:
                stack.append(i)
        #print(stack)
        for index, i in enumerate(s_list):
            if i in vowels:
                s_list[index] = stack[-1]
                stack.pop()
        return(''.join(s_list))


print(Solution().reverseVowels(input))
