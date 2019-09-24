#!/usr/bin/python
# Benjamin Wiens
# Teemo Attacking (https://leetcode.com/problems/teemo-attacking/)

timeseries = [1,2]
duration = 2
class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        if not timeSeries:
            return 0
        if len(timeSeries) == 1:
            return duration
        summation = 0
        for index, number in enumerate(timeSeries[1:], 1):
            summation += min(duration,number-timeSeries[index-1])
        return summation + duration

print(Solution().findPoisonedDuration(timeseries,duration))
