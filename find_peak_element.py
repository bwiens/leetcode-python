#!/usr/bin/python
#Benjamin Wiens
#Find Peak Element (https://leetcode.com/problems/find-peak-element/)
#Leetcode Accepted

nums = [1,2,1,3,5,6,4]
import sys
class Solution:
    def findPeakElement(self, nums):
        """Find the peak element (element greater than neighbors)
        
        """
        max, max_index = -sys.maxsize, -sys.maxsize
        for index, num in enumerate(nums):
            if num > max:
                max = num
                max_index = index
            if index > 0 and index < len(nums) -1:
                if num > nums[index-1] and num > nums[index+1] and num:
                    return index
        #if there is no solution, there are few elements and we simply return the max
        return max_index

print(Solution().findPeakElement(nums))
