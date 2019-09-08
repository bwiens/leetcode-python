#!/usr/bin/python
# Benjamin Wiens
# Two City Scheduling (https://leetcode.com/problems/two-city-scheduling)

input = [[10,20],[30,200],[400,50],[30,20]]

class Solution:
    def twoCitySchedCost(self, costs):
        # sort by savings
        costs.sort(key=lambda cost: cost[0] - cost[1])
        # then go greedy
        result = 0
	# add the first half with cheapest to get to city A first, then B
	# remember the requirement is half go to A, half to B
        for cost in costs[:len(costs)//2]:
            result += cost[0]
        for cost in costs[len(costs)//2:]:
            result += cost[1]
        return result

print(Solution().twoCitySchedCost(input))
