#!/usr/bin/python
# Benjamin Wiens
# Count Substrings With Only One Distinct Letter (https://leetcode.com/problems/count-substrings-with-only-one-distinct-letter/)

S = "aaaba"

class Solution:
    def countLetters(self, S):
        result, current = 1, 1
        for index, char in enumerate(S[1:],1):
            if char == S[index-1]:
                current += 1
            else:
                current = 1
            result += current
        return result
            
print(Solution().countLetters(S))
