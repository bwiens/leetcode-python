#!/usr/bin/python
# Benjamin Wiens
# 1100. Find K-Length Substrings With No Repeated Characters (https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters)

S = "havefunonleetcode"
K = 5
class Solution:
    def numKLenSubstrNoRepeats(self, S, K):
        result = 0
        for index, char in enumerate(S[:len(S)-K+1]):
            if len(set(S[index:index+K])) == K:
                result += 1
        return result

print(Solution().numKLenSubstrNoRepeats(S,K))
