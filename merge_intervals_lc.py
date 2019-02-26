#!/usr/bin/python
#Benjamin Wiens
#Merge Intervals (https://leetcode.com/problems/merge-intervals/)
#Leetcode Accepted
#The odd leetcode variant with intervals as objects


#input = [[1,3],[2,6],[8,10],[15,18]]
#input = [Interval(1,3),Interval(2,6),Interval(8,10),Interval(15,18)]
# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
#    def __repr__(self):
#        return f"Interval({self.start}, {self.end})"

class Solution:
    def merge(self, intervals):
        #sort the intervals
        #for i in intervals:
        #    Interval(*i)
        intervals = [Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15, 18)]
        intervals.sort(key=lambda x: x.start)
        result, merged = [], []
        tmp = []
        for i in intervals:
            if not merged:
                merged.append(i)
            elif i.start <= merged[-1].end:
                    tmp = merged[-1]
                    if merged[-1].end < i.end:
                        merged[-1].end = i.end
            else:
                merged.append(i)
        return merged

print(Solution().merge(input))
