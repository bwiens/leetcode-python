#!/usr/bin/python
# Benjamin Wiens
# Sentence Similarity II (https://leetcode.com/problems/sentence-similarity-ii)

words1 = ["a","very","delicious","meal"]
words2 = ["one","really","good","dinner"]
pairs = [["great","good"],["extraordinary","good"],["well","good"],["wonderful","good"],["excellent","good"],["fine","good"],["nice","good"],["any","one"],["some","one"],["unique","one"],["the","one"],["an","one"],["single","one"],["a","one"],["truck","car"],["wagon","car"],["automobile","car"],["auto","car"],["vehicle","car"],["entertain","have"],["drink","have"],["eat","have"],["take","have"],["fruits","meal"],["brunch","meal"],["breakfast","meal"],["food","meal"],["dinner","meal"],["super","meal"],["lunch","meal"],["possess","own"],["keep","own"],["have","own"],["extremely","very"],["actually","very"],["really","very"],["super","very"]]

class Solution:
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        if len(words1) != len(words2):
            return False
        hmap = {}
        for pair in pairs:
            if pair[0] not in hmap:
                hmap[pair[0]] = [pair[1]]
            else:
                hmap.get(pair[0]).append(pair[1])
                
            if pair[1] not in hmap:
                hmap[pair[1]] = [pair[0]]
            else:
                hmap.get(pair[1]).append(pair[0])
        
        
        for index, word in enumerate(words1):
            if word == words2[index]:
                continue
            stack = []
            stack.append(word)
            seen = set()
            while stack:
                wordy = stack.pop()
                if wordy == words2[index]:
                    break
                seen.add(wordy)
                transitives = hmap.get(wordy)
                if transitives:
                    for new in hmap.get(wordy):
                        if new not in seen:
                            seen.add(new)
                            stack.append(new)
            else:
                return False
        return True

print(Solution().areSentencesSimilarTwo(words1, words2, pairs))
