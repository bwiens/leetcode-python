#!/usr/bin/python
# Benjamin Wiens
# Sentence Similarity (https://leetcode.com/problems/sentence-similarity/)

words1 = ["great","acting","skills"]
words2 = ["fine","drama","talent"]
pairs = [["great","fine"],["drama","acting"],["skills","talent"]]
class Solution:
    def areSentencesSimilar(self, words1, words2, pairs):
        if not pairs:
            return words1 == words2
        if len(words1) != len(words2):
            return False
        hmap = {}
        for pair in pairs:
            if pair[0] not in hmap:
                hmap[pair[0]] = []
                hmap[pair[0]].append(pair[1])
            else:
                hmap[pair[0]].append(pair[1])
            if pair[1] not in hmap:
                hmap[pair[1]] = []
                hmap[pair[1]].append(pair[0])
            else:
                hmap[pair[1]].append(pair[0])
        ##########################################
        for index, word in enumerate(words1):
            if words1[index] == words2[index]:
                continue
            if word not in hmap or words2[index] not in hmap[word]:
                return False
        return True

print(Solution().areSentencesSimilar(words1, words2, pairs))
