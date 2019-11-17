#!/usr/bin/python
# Benjamin Wiens
# Compare Strings by Frequency of the Smallest Character (https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/)

queries = ["bbb","cc"]
words = ["a","aa","aaa","aaaa"]

class Solution:
    def numSmallerByFrequency(self, queries, words):
        result = []
        #compare frequencies of smallest character
        f_q = []
        for query in queries:
            f_q.append(query.count(min(query)))
        f_w = []
        for word in words:
            f_w.append(word.count(min(word)))
        for number in f_q:
            count = 0
            for number2 in f_w:
                if number < number2:
                    count += 1
            result.append(count)
        return result   
print(Solution().numSmallerByFrequency(queries, words))
