#!/usr/bin/python
# Benjamin Wiens
# Subarray Sum Equals K (https://leetcode.com/problems/subarray-sum-equals-k/)
# Leetcode Accepted

nums = [1, 1, 1]
k = 2

class Solution:
    def subarraySum(self, nums, k):
        count = 0
        for index, number in enumerate(nums):
            subarray = number
            c = 1
            if number == k:
                count +=1
            while index + c <= len(nums) -1:
                subarray += nums[index+c]
                c += 1
                if subarray == k:
                    count += 1
                elif subarray > k:
                    break
        return count

print(Solution().subarraySum(nums,k))
