#!/usr/bin/python
# Benjamin Wiens
# Wiggle Sort II
# Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]...
import random

nums = [1, 3, 2, 2, 3, 1]


class Solution:
    def wiggle_sort(self, nums):
        """
        :param nums: List(int)
        :return: : List(int)
        """
        print("Unsorted: ", nums)
        while (nums[0] >= nums[1] or
               nums[1] <= nums[2] or
               nums[2] >= nums[3] or
               nums[3] <= nums[4] or
               nums[4] >= nums[5]):
            id = range(len(nums))
            # swap two numbers randomly
            i1, i2 = random.sample(id, 2)
            nums[i1], nums[i2] = nums[i2], nums[i1]
        print("Wiggle Sorted:", nums)
        return nums


print(Solution().wiggle_sort(nums))

