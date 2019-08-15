#!/usr/bin/python
# Benjamin Wiens
# Sorted Distance to a Character (https://leetcode.com/problems/shortest-distance-to-a-character/)

S = "loveleetcode"
C = 'e'
import sys
class Solution:
    def shortestToChar(self, S, C):
        found, result = [], []
        for index, char in enumerate(S):
            if char == C:
                found.append(index)
        for index, char in enumerate(S):
            minimum = sys.maxsize
            for number in found:
                minimum = min(minimum, abs(index-number))
            result.append(minimum)
        return result

print(Solution().shortestToChar(S,C))
