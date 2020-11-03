#!/usr/bin/python

input = [10, 15, 20]
class Solution:
    def minCostClimbingStairs(self, cost):
        dp = (len(cost)) * [0]
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, len(cost)):
            dp[i] = min(dp[i-1] + cost[i], dp[i-2] + cost[i])
        return min(dp[-1], dp[-2])

print(Solution().minCostClimbingStairs(input))
