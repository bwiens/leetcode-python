#!/usr/bin/python
# Benjamin Wiens
# Uncommon Words from Two Sentences (https://leetcode.com/problems/uncommon-words-from-two-sentences/)

A = "this apple is sweet"
B = "this apple is sour"

from collections import Counter
class Solution:
    def uncommonFromSentences(self, A, B):
        countA = Counter(A.split())
        countB = Counter(B.split())
        result = []
        for key, value in countA.items():
            if value == 1:
                if key not in countB:
                    result.append(key)
        for key, value in countB.items():
            if value == 1:
                if key not in countA:
                    result.append(key)
        return result

print(Solution().uncommonFromSentences(A,B))
