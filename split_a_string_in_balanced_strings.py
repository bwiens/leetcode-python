#!/usr/bin/python
# Split a String in Balanced Strings (https://leetcode.com/problems/split-a-string-in-balanced-strings/)

s = "RLRRLLRLRL"

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balance, splits = 0, 0
        for char in s:
            if char == 'L':
                balance += 1
            else:
                balance -= 1
            if balance == 0:
                splits += 1
        return splits

print(Solution().balancedStringSplit(s))
