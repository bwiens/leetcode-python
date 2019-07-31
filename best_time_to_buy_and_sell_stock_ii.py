#!/usr/bin/python
# Benjamin Wiens
# Best Time to Buy and Sell Stock II (https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)

stock = [7,1,5,3,6,4]
class Solution:
    def maxProfit(self, prices):
        # problem comes down to is finding any time where we can make a profit
        result = 0
        for index, price in enumerate(prices[1:],1):
            # check if we can make a profit
            if price > prices[index-1]:
                result += price - prices[index-1]
        return result

print(Solution().maxProfit(stock))
