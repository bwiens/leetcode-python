#!/usr/bin/python
# Benjamin Wiens
# Array Partition I (https://leetcode.com/problems/array-partition-i/)
# Leetcode Accepted
 
numbers = [1,4,3,2]

class Solution:
    def arrayPairSum(self, nums):
        sum = 0
        nums.sort()
        #print(nums)
        for i in range(0,len(nums),2):
            sum += min(nums[i],nums[i+1])
        return sum

print(Solution().arrayPairSum(numbers))

#O(nlogn)
