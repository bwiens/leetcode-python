#!/usr/bin/python
#Benjamin Wiens
#Kth Largest Element in an Array (https://leetcode.com/submissions/detail/205397877/)
#Leetcode Accepted


input = [3,2,3,1,2,4,5,5,6]
k = 4
import heapq
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        heapq.heapify(heap)
        for number in nums:
            heapq.heappush(heap,number)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]

print(Solution().findKthLargest(input, k))
