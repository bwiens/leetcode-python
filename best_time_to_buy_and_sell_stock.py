#!/usr/bin/python3
# Benjamin Wiens
# Best Time to Buy and Sell Stock (https://leetcode.com/problems/best-time-to-buy-and-sell-stock/solution/)
# Leetcode Accepted
import sys
input = [7,1,5,3,6,4]
class Solution:
    def maxProfit(self, prices: 'List[int]') -> 'int':
        max_price = 0
        min = sys.maxsize
        for index,i in enumerate(prices):
            if i < min:
                min = i
            if i - min > max_price:
                max_price = i - min
        return max_price

print(Solution().maxProfit(input))
