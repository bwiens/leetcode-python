#!/usr/bin/python
# Benjamin Wiens
# K Closest Points to Origin (https://leetcode.com/problems/k-closest-points-to-origin/submissions/)
# Leetcode Accepted
import math

coordinates = [[3,3],[5,-1],[-2,4]]
K = 2
class Solution:
    def kClosest(self, points, K):
        distance = []
        for p in points:
            #this is based on pythagoreon theorem
            x = math.sqrt(p[0]**2 + p[1]**2)
            #create tuple of distance and coordinate
            distance.append((x, p))
        #sort by distance
        distance.sort(key=lambda x: x[0])
        #print second part of tuple
        return [x[1] for x in distance[:K]]
    #O(nlogn) time
    #O(n) space

print(Solution().kClosest(coordinates,K))
