#!/usr/bin/python
#Benjamin Wiens
#Sliding Window Maximum https://leetcode.com/problems/sliding-window-maximum/
#Leetcode Accepted

input = [1,3,-1,-3,5,3,6,7]
k = 3

class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = []
        max, current, c = 0, 0, 1
        if not nums:
            return []
        if k == 1:
            return nums  
        for index, i in enumerate(nums):
            max = i
            while c < k:
                if index + k < len(nums) +1:
                    if max < nums[index + c]:
                        max = nums[index + c]
                    c += 1
                else:
                    return result
            result.append(max)
            c = 1

print(Solution().maxSlidingWindow(input, k))
