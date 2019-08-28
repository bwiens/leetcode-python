#!/usr/bin/python
# Benjamin Wiens
# Compare Strings by Frequency of the Smallest Character (https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/)

queries = ["bbb","cc"]
words = ["a","aa","aaa","aaaa"]

class Solution:
    def numSmallerByFrequency(self, queries, words):
        result, answ = [], 0
        word_count_array = []
        for word in words:
                smallest_w = min(word)
                smallest_w_count = word.count(smallest_w)
                word_count_array.append(smallest_w_count)
        for query in queries:
            answ = 0
            smallest = min(query)
            smallest_count = query.count(smallest)
            for smallest_w_count in word_count_array:
                if smallest_count < smallest_w_count:
                    answ += 1
            result.append(answ)
        return result

print(Solution().numSmallerByFrequency(queries, words))
