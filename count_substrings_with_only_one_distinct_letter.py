#!/usr/bin/python
# Benjamin Wiens
# Count Substrings With Only One Distinct Letter (https://leetcode.com/problems/count-substrings-with-only-one-distinct-letter/)

S = "aaaba"

class Solution:
    def countLetters(self, S):
        count = 0
        i = 0
        while i <= len(S) - 1:
            count += 1
            c = 1
            #
            while i + c <= len(S) -1 and S[i] == S[i + c]:
                count += 1
                c += 1
            i += 1
        return count

print(Solution().countLetters(S))
