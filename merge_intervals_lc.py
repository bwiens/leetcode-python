#!/usr/bin/python
# Benjamin Wiens
# Merge Intervals (https://leetcode.com/problems/merge-intervals/)

input = [[1,4],[2,3]]

class Solution:
    def merge(self, intervals):
        if not intervals:
            return []
        intervals.sort()
        result = [intervals[0]]
        for interval in intervals[1:]:
            if interval[0] <= result[-1][1]:
                result[-1][1] = max(interval[1],result[-1][1])
            else:
                result.append(interval)
        return result

print(Solution().merge(input))
