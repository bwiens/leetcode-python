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
        l, position = 0, 0
        while l < len(nums):
            if nums[l] == 0:
                position += 1
            else:
                if position > 0:
                    #swap
                    nums[l], nums[l-position] = nums[l-position], nums[l]
                    #NO position -= 1
            l += 1
        return nums
print(Solution().moveZeroes(input))
