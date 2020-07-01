#!/usr/bin/python

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        # create array
        result = []
        ans = start
        for i in range(1,n):
            ans = ans ^ (start + (i*2))
        return ans

print(Solution().xorOperation(5, 0))
