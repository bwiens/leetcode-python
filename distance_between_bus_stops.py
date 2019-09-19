#!/usr/bin/python
# Benjamin Wiens
# Distance Between Bus Stops (https://leetcode.com/problems/distance-between-bus-stops/)

distance = [1,2,3,4]
start = 0
destination = 3

class Solution:
    def distanceBetweenBusStops(self, distance, start, destination) -> int:
        station1 = min(start, destination)
        station2 = max(start, destination)
        return min(sum(distance[station1:station2]), sum(distance) -sum(distance[station1:station2]))

print(Solution().distanceBetweenBusStops(distance,start,destination))
