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
        c = Counter()
        result = []
        for i in nums:
            if i not in c:
                c[i] = 1
            else: 
                value = c.get(i)
                c[i] = value + 1
        #print(c)
        for index, number in enumerate(c.most_common()):
            if index < k:
                result.append(number[0])
            else:
                break
        return result

print(Solution().topKFrequent(numbers,k))
