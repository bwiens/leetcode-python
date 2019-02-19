#!/usr/bin/python
import math
#Benjamin Wiens
#https://leetcode.com/problems/binary-search/
#Leetcode Accepted
input = [-1,0,3,5,9,12]
target = 2
class Solution:
    def search(self, nums: 'List[int]', target: 'int') -> 'int':
        left = 0
        right = len(nums) -1
        while left <= right:
            #find middle
            m = math.floor((left + right) //2)
            if nums[m] < target:
                left = m + 1
            elif nums[m] > target:
                right = m -1
            else: 
                if nums[m] == target:
                    #return the index
                    return nums.index(target)
        return -1

print(Solution().search(input, target))
