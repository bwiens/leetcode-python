#!/usr/bin/python
#Benjamin Wiens
#Sort Characters by Frequency (https://leetcode.com/problems/sort-characters-by-frequency/)
#Leetcode Accepted

word = "tree"
from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        hmap = Counter(s)
        result = []
        for key, value in hmap.most_common():
            for i in range(value):
                result.append(key)
        return ''.join(result)

print(Solution().frequencySort(word))
