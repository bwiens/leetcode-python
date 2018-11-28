#!/usr/bin/python
#Benjamin Wiens
#https://leetcode.com/problems/first-unique-character-in-a-string/
#Leetcode Accepted

import collections

input = "loveleetcode"

class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        c = collections.Counter(list(s))
        for index, item in enumerate(s):
            if c[item] == 1:
                return index
        return -1

print(Solution().firstUniqChar(input))
