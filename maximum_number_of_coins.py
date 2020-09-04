#!/usr/bin/python

coins = [9,8,7,6,5,1,2,3,4]
class Solution:
    def maxCoins(self, piles):
        piles.sort()
        end = len(piles)-2
        result = 0
        for i in range(len(piles)//3):
            result += piles[end]
            end -= 2
        return result

print(Solution().maxCoins(coins))
