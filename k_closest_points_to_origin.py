#!/usr/bin/python
# Benjamin Wiens
# K Closest Points to Origin (https://leetcode.com/problems/k-closest-points-to-origin/submissions/)
# Leetcode Accepted
import heapq

coordinates = [[3,3],[5,-1],[-2,4]]
K = 2
class Solution:
    def kClosest(self, points, K):
        heap = []
        for point in points:
            dist = point[0] * point[0] + point[1] * point[1] 
            # adding negative so the largest number becomes smallest
            heapq.heappush(heap,(-dist, point[0], point[1]))
            if len(heap) > K:
                heapq.heappop(heap)
        result = []
        for x, y, z in heap:
            result.append((y, z))
        return result
print(Solution().kClosest(coordinates,K))
