#!/usr/bin/python
#Benjamin Wiens
#https://leetcode.com/problems/first-unique-character-in-a-string/
#Leetcode Accepted

input = "loveleetcode"
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        countchars = {}
        if not s:
            return -1
        for i in s:
            if i not in countchars:
                countchars[i] = 1
            else:
                countchars[i] += 1
        for index, i in enumerate(s):
            if countchars.get(i) == 1:
                return index
        return -1

print(Solution().firstUniqChar(input))
'''
super fast version:
from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        hmap = Counter(s)
        for key, value in hmap.items():
            if value == 1:
                return s.find(key)
        return -1
'''
