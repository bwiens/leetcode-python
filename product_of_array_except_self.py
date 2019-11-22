#!/usr/bin/python
# Product of Array Except Self (https://leetcode.com/problems/product-of-array-except-self/)

numbers = [1,2,3,4]
class Solution:
    def productExceptSelf(self, nums):
        left_products = [1] * len(nums)
        for index, number in enumerate(nums[1:], 1):
            left_products[index] = nums[index-1] * left_products[index-1]
        
        right_products = [1] * len(nums)
        # loop backwards
        # plus index
        for index in range(len(nums)-2, -1, -1):
            right_products[index] = nums[index+1] * right_products[index+1]
        
        result = []
        #multiply, each index stores what is right and left respectively
        for index, number in enumerate(nums):
            result.append(left_products[index] * right_products[index])
        return result

print(Solution().productExceptSelf(numbers))
