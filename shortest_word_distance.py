#!/usr/bin/python
# Benjamin Wiens
# Shortest Word Distance (https://leetcode.com/problems/shortest-word-distance/)

words = ["practice", "makes", "perfect", "coding", "makes"]
word1 = "coding"
word2 = "practice"

import sys
class Solution:
    def shortestDistance(self, words, word1, word2: str):
        w1, w2 = False, False
        result = sys.maxsize
        for index, word in enumerate(words):
            if word == word1:
                w1_index = index
                w1 = True
            if word == word2:
                w2_index = index
                w2 = True
            if w1 and w2:
                result = min(abs(w1_index - w2_index), result)
        return result

print(Solution().shortestDistance(words,word1,word2))
