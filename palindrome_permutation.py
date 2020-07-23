#!/usr/bin/python

input = "code"

class Solution:
    def canPermutePalindrome(self, s) -> bool:
        dict, odds = {}, 0
        for char in s:
            if char in dict:
                dict[char] += 1
            else:
                dict[char] = 1
        for key, value in dict.items():
            if value % 2 != 0:
                odds += 1
        return odds <= 1

print(Solution().canPermutePalindrome(input))
