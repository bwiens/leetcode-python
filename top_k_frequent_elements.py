#!/usr/bin/python
# Benjamin Wiens
# Top K Frequent Elements (https://leetcode.com/problems/top-k-frequent-elements/)
# Leetcode Accepted

k = 2
numbers = [4,1,-1,2,-1,2,3]

from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hmap = Counter(nums)
        result = []
        for key, value in hmap.most_common(k):
            result.append(key)
        return result
print(Solution().topKFrequent(numbers,k))
