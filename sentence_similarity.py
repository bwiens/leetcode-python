#!/usr/bin/python
# Benjamin Wiens
# Sentence Similarity (https://leetcode.com/problems/sentence-similarity/)

words1 = ["great","acting","skills"]
words2 = ["fine","drama","talent"]
pairs = [["great","fine"],["drama","acting"],["skills","talent"]]

from collections import defaultdict
class Solution:
    def areSentencesSimilar(self, words1, words2, pairs):
        if not pairs:
            return words1 == words2
        if len(words1) != len(words2):
            return False
        hmap = defaultdict(list)
        for pair in pairs:
            hmap[pair[0]].append(pair[1])
            hmap[pair[1]].append(pair[0])
        ##########################################
        for index, word in enumerate(words1):
            if words1[index] == words2[index]:
                continue
            if word not in hmap or words2[index] not in hmap[word]:
                return False
        return True
print(Solution().areSentencesSimilar(words1, words2, pairs))
