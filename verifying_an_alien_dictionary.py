#!/usr/bin/python

words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"

class Solution:
    def isAlienSorted(self, words, order) -> bool:
        dict = {}
        # map each char in the alien dictionary to its position
        for index, char in enumerate(order):
            dict[char] = index
        # compare adjacent words
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            # words that are the same can be skipped
            if word1 == word2:
                continue
            # longer words, that start with the adjacent words, should not come first
            if len(word1) > len(word2):
                if word1.startswith(word2):
                    return False
            # compare each character, it must be smaller or equal to that of the adjacent word
            for j in range(min(len(word1), len(word2))):
                if dict.get(word1[j]) < dict.get(word2[j]):
                    break
                elif dict.get(word1[j]) == dict.get(word2[j]):
                    continue
                else:
                    return False
        return True

print(Solution().isAlienSorted(words, order))
