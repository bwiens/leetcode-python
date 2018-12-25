#!/usr/bin/python
#Benjamin Wiens
#Two Sum Problem
#See Version 2 for Non-Bruteforce (twosum_2.py)
   
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
	for i in range(len(nums)):
        	for j in range(j, len(nums)):
                	if nums[i] + nums[j] == target:
                        	return (i, j)
				



print(Solution().twoSum(nums, target))
#two for loops indicate O(n^2) time, see Version 2 for O(n) solution
