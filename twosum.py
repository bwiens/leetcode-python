#!/usr/bin/python

#Benjamin Wiens
#Two Sum Problem
#Given an array of integers, return indices of the two numbers such that they add up to a specific target.
   
nums = [2, 7, 11, 15]
target = 9

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
	i=0
	j=1
	#the range() function has two sets of parameters start and stop.
	for i in range(len(nums)):
#        	print i
        	for j in range(j, len(nums)):
#                	print j
                	if nums[i] + nums[j] == target:
#                        	print(i, j,"Success")
                        	return (i, j)
				



print(Solution().twoSum(nums, target))
#two for loops indicate O(n^2) time
