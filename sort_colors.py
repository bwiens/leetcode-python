#!/usr/bin/python

input = [2,0,2,1,1,0]

#not optimal using Bubble Sort
class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        changed = True
        while changed:
            changed = False
            for index, number in enumerate(nums[1:], 1):
                if nums[index-1] > nums[index]:
                    nums[index-1], nums[index] = nums[index], nums[index-1]
                    changed = True
        return nums
print(Solution().sortColors(input))
