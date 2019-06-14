#!/usr/bin/python
# Benjamin Wiens
# Fibonacci Number (https://leetcode.com/problems/fibonacci-number)
# Leetcode Accepted 

number = 15

class Solution:
    def fib(self, N: int) -> int:
        hmap = {}
        def helper(N):
            if N in hmap:
                return hmap[N]
            elif N < 2:
                return N
            else:
                value = helper(N-1) + helper(N-2)
                hmap[N] = value
                return value
        return helper(N)

print(Solution().fib(number))
