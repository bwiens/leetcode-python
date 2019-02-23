#!/usr/bin/python
#Benjamin Wiens
#Move Zeroes (https://leetcode.com/problems/move-zeroes)
#Leetcode Accepted
input = [0,1,0,3,4,0,5]
class Solution:
    def moveZeroes(self, nums: 'List[int]') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        for index, i in enumerate(nums):
            if i == 0:
                nums.remove(nums[index])
                nums.append(i)

        return nums
print(Solution().moveZeroes(input))
