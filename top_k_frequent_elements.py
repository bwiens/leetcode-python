#!/usr/bin/python
# Benjamin Wiens
# Top K Frequent Elements (https://leetcode.com/problems/top-k-frequent-elements/)
# Leetcode Accepted

k = 2
numbers = [4,1,-1,2,-1,2,3]

from collections import Counter
import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counted = Counter(nums)
        result, heap = [], []
        for key, value in counted.items():
            heap.append((-value, key))
        heapq.heapify(heap)
        while heap:
            pair = heapq.heappop(heap)
            result.append(pair[1])
            if len(result) == k:
                return result

print(Solution().topKFrequent(numbers,k))
