#!/usr/bin/python
# Benjamin Wiens
# Minimum Cost to Connect Sticks (https://leetcode.com/problems/minimum-cost-to-connect-sticks/)

sticks = [1,8,3,5]

import heapq 
class Solution:
    def connectSticks(self, sticks):
        heapq.heapify(sticks)
        total = 0
        while len(sticks) >= 2:
            a = heapq.heappop(sticks)
            b = heapq.heappop(sticks)
            total += a + b
            c = a + b
            heapq.heappush(sticks,c)
        return total

print(Solution().connectSticks(sticks))
