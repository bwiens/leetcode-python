#!/usr/bin/python
# Benjamin Wiens
# Generate a String with Characters that Have Odd Counts (https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/)

n = 24

class Solution:
    def generateTheString(self, n: int) -> str:
        result = 'a' * n
        if n % 2 == 0:
            result = result[:-1]
            result += 'b'
        return result

print(Solution().generateTheString(n))

