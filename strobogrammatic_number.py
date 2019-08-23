#!/usr/bin/python
# Benjamin Wiens
# Strobogrammatic Number (https://leetcode.com/problems/strobogrammatic-number/)

number = "88"

class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        hmap = {"0": "0", "1": "1", "6": "9", "9": "6", "8": "8" }
        strobo = ''
        for number in num:
            if number not in hmap:
                return False
            else:
                strobo = strobo + hmap.get(number)
        return strobo[::-1] == num

print(Solution().isStrobogrammatic(number))
