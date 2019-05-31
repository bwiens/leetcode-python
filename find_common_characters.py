#!/usr/bin/python
# Benjamin Wiens
# Find Common Characters (https://leetcode.com/problems/find-common-characters)
# Leetcode Accepted

words = ["bella","label","roller"]
class Solution:
    def commonChars(self, A):
        hmap, hmap2, hmap3 = {}, {}, {}
        result = []
        #first hashmap
        for string in A[0]:
            for char in string:
                if char not in hmap:
                    hmap[char] = 1
                else:
                    hmap[char] += 1
        #second, rolling hashmap
        for string in A[1:]:
            for char in string:
                if char not in hmap2:
                        hmap2[char] = 1
                else:
                    hmap2[char] += 1
            #use a copy because we cannot change hmap during iteration
            hmap3 = hmap.copy()
            for key, value in hmap3.items():
                if key in hmap2:
                    hmap[key] = min(value, hmap2.get(key))
                else:
                    del hmap[key]
            hmap2 = {}
        #assemble result
        for key, value in hmap.items():
            for i in range(value):
                result.append(key)
        return result
print(Solution().commonChars(words))
