#!/usr/bin/python
# Benjamin Wiens
# Top K Frequent Words (https://leetcode.com/problems/top-k-frequent-words/)

input = ["i", "love", "leetcode", "i", "love", "coding"]
k = 3
from collections import Counter
class Solution:
    def topKFrequent(self, words, k):
        result = []
        count = 0
        c_list = Counter(words)
        for key, value in sorted(c_list.items(), key=lambda item: (-item[1], item[0])):
            result.append(key)
            count += 1
            if count == k:
                return result

print(Solution().topKFrequent(input,k))
# O(nlogn)
