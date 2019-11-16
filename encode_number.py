#!/usr/bin/python
# Benjamin Wiens
# Encode Number (https://leetcode.com/problems/encode-number/)

input = 23

class Solution:
    def encode(self, num):
        return bin(num + 1)[3:]

print(Solution().encode(input))
