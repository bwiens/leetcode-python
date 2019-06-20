#!/usr/bin/python
# Benjamin Wiens
# Shortest Unsorted Continuous Subarray (https://leetcode.com/problems/shortest-unsorted-continuous-subarray/)
# Leetcode Accepted

numbers = [2, 6, 4, 8, 10, 9, 15]
class Solution:
    def findUnsortedSubarray(self, nums):
        nums_sorted = sorted(nums)
        start, end = len(nums), 0
        #special case (already sorted)
        if nums_sorted == nums:
            return 0
        for index, number in enumerate(nums):
            if number != nums_sorted[index]:
                start = min(index,start) 
                end = max(index,end)
        return end - start + 1

print(Solution().findUnsortedSubarray(numbers))

#O(nlogn)
