#!/usr/bin/python
# Benjamin Wiens
# Custom Sort String (https://leetcode.com/problems/custom-sort-string/)
# Leetcode Accepted

s = "cba"
t = "abcd"

class Solution:
    def customSortString(self, S, T):
        hmap, result = {}, ''
        #get a count of T
        for index, char in enumerate(T):
            if char in hmap:
                hmap[char] += 1
            else:
                hmap[char] = 1
        #write S first (each char times occurence in T), then remainder of T
        for char in S:
            if char in hmap:
                for i in range(hmap.get(char)):
                    result += char
                del hmap[char]
        for char in T:
            if char in hmap:
                for i in range(hmap.get(char)):
                    result += char
                del hmap[char]
        return result

print(Solution().customSortString(s,t))
