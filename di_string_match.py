#!/usr/bin/python
# Benjamin Wiens
# DI String Match (https://leetcode.com/problems/di-string-match)
# Leetcode Accepted

input = "DIDI"

class Solution:
    def diStringMatch(self, S):
        result = []
        low = 0
        high = len(S)
        for i in range(len(S)):
            if S[i] == 'I':
                result.append(low)
                low += 1
            else:
                result.append(high)
                high -=1
        #append high or low
        return result + [high]

print(Solution().diStringMatch(input))
