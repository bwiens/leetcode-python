#!/usr/bin/python
# Benjamin Wiens
# Positions of Large Groups (https://leetcode.com/problems/positions-of-large-groups/)

group = "abcdddeeeeaabbbcd"
class Solution:
    def largeGroupPositions(self, S):
        result = []
        i = 0
        while i < len(S)-1:
            #print(S[i])
            start = i
            j = 1
            while i+j < len(S) and S[i+j] == S[i]:
                j+=1
            end = start+j
            x = abs(end - start)
            if abs(end-start) >= 3:
                result.append([start, end-1])
            i = i+j
        return result

print(Solution().largeGroupPositions(group))
