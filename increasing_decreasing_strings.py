#!/usr/bin/python
# Benjamin Wiens
# Increasing Decreasing String (https://leetcode.com/problems/increasing-decreasing-string/)

s = "aaaabbbbcccc"


from collections import Counter
class Solution:
    def sortString(self, s: str) -> str:
        counted = Counter(s)
        forward = True
        result = ''
        while counted:
            if forward:
                sorted(counted.keys())
            else:
                sorted(counted.keys(), reverse = True)
            for char in sorted(counted.keys()) if forward else reversed(sorted(counted.keys())):
                result += char
                counted[char] -= 1
                if counted.get(char) == 0:
                    del counted[char] 
            forward = not forward
        return result

print(Solution().sortString(s))
