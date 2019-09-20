#!/usr/bin/python
# Benjamin Wiens
# Car Pooling (https://leetcode.com/problems/car-pooling/)

trips = [[2,1,5],[3,3,7]]
capacity = 5

class Solution:
    def carPooling(self, trips, capacity):
        hmap = {}
        hmap_end = {}
        minimum = trips[0][1]
        maximum = trips[0][2]
        for trip in trips:
            minimum = min(minimum, trip[1])
            if trip[1] in hmap:
                hmap[trip[1]] += trip[0]
            else:
                hmap[trip[1]] = trip[0]
        for trip in trips:
            maximum = max(maximum, trip[2])
            if trip[2] in hmap_end:
                hmap_end[trip[2]] += trip[0]
            else:
                hmap_end[trip[2]] = trip[0] 
        rolling = 0
        for i in range(minimum, maximum+1):
            if i in hmap:
                rolling += hmap[i]
            if i in hmap_end:
                rolling -= hmap_end[i]
            if capacity < rolling:
                return False
        return True

print(Solution().carPooling(trips,capacity))
