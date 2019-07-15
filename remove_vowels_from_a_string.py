#!/usr/bin/python
# Benjamin Wiens
# Remove Vowels From a String (https://leetcode.com/problems/remove-vowels-from-a-string/)

input = "leetcodeisacommunityforcoders"
class Solution:
    def removeVowels(self, S):
        result = ''
        for char in S:
            if char not in ('a','e','i','o','u'):
                result = result + char
        return result

print(Solution().removeVowels(input))
