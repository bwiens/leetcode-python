#!/usr/bin/python
# Benjamin Wiens
# Top K Frequent Elements (https://leetcode.com/problems/top-k-frequent-elements/)
# Leetcode Accepted

k = 2
numbers = [4,1,-1,2,-1,2,3]

from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums, k):
        heap, result = [], []
        counted = Counter(nums)
        for key, value in counted.items():
            if len(heap) < k:
                heapq.heappush(heap, (value, key))
            else: 
                if heap[0][0] < value:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (value, key))
        for i in range(len(heap)):
            result.append(heap[i][1])
        return result
print(Solution().topKFrequent(numbers,k))
