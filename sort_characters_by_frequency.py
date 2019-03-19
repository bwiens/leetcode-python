#!/usr/bin/python
#Benjamin Wiens
#Sort Characters by Frequency (https://leetcode.com/problems/sort-characters-by-frequency/)
#Leetcode Accepted

word = "tree"
from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        """Sort string by frequency of characters with counter"""
        count = Counter(s)
        result = ''
        for key, value in count.most_common():
            i=0
            while i < value:
                result = result + key
                i += 1
        return result

    def frequencySort2(self, s: str) -> str:
        """Sort without Counter"""
        dict = {}
        result = ""
        for char in s:
            if char not in dict:
                dict[char] = 1
            else:
                dict[char] += 1
        sdict = sorted(dict.items(), key=lambda x: x[1], reverse=True)
        for char in sdict:
            x=char[1]
            i = 0
            while i < x:
                result = result + char[0]
                i += 1
        return result
print(Solution().frequencySort(word))
print(Solution().frequencySort2(word))
