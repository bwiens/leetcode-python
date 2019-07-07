#!/usr/bin/python
# Find the Difference (https://leetcode.com/problems/find-the-difference/)
# Benjamin Wiens
# Leetcode Accepted

s = "abcd"
t = "abcde"

class Solution:
    def findTheDifference(self, s, t):
        result, hmap = '', {}
        for i in s:
            if i in hmap:
                hmap[i] += 1
            else:
                hmap[i] = 1
        for i in t:
            if i not in hmap:
                result = result + i
            else:
                tmp = hmap.get(i)
                if tmp == 1:
                    del hmap[i]
                else:
                    hmap[i] -= 1
        return result

print(Solution().findTheDifference(s,t))
