#!/usr/bin/python
#Benjamin Wiens
#https://leetcode.com/problems/reverse-words-in-a-string/
#Leetcode Accepted
import re
input = " the sky  is blue"
class Solution(object):
    def reverseWords(self, s):
        """
        :param s: str
        :return: str
        """
        #remove leading and trailing spaces
        s = s.strip()
        rv, rv2 = [], []
        word, s2 = '', ''
        for index, i in enumerate(s):
            if i != ' ' or index == s[-1]:
                word = word + i
            else:
                rv2.append(word)
                word = ''
        #append the last word
        rv2.append(word)
        #reverse list
        rv = rv2[::-1]
        #join to string
        s2 = ' '.join(rv)
        #remove extra spaces with re
        s2 = re.sub (' +', ' ', s2)
        if s2 == ' ':
            s2 = ''
        return s2

print(Solution().reverseWords(input))
