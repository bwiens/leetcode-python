#!/usr/bin/python
#Benjamin Wiens
#Find First and Last Position of Element in Sorted Array (https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)
#Leetcode Accepted
nums = [2,2]
target = 2

class Solution:
    def searchRange(self, nums, target):
        result = []
        #no numbers given
        if not nums and len(str(target)) >= 1:
            return [-1, -1]
        #if target equals nums
        if len(nums) == 1 and nums[0] == target:
            return [0,0]
        found = False
        length = len(nums) - 1
        for index, i in enumerate(nums):
            if i == target and found == False:
                result.append(index)
                found = True
                #end of list
            if found == True and i != target:
                result.append(index-1)
                found = False
            #if the target was at the end of the list
            if found == True and index == length:
                result.append(index)
        if not result:
            return [-1, -1]
        return result

print(Solution().searchRange(nums,target))
