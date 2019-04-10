#!/usr/bin/python
# Benjamin Wiens
# Summary Ranges (https://leetcode.com/problems/summary-ranges/)
# Leetcode Accepted

input = [0,2,3,4,6,8,9]
class Solution:
    def summaryRanges(self, nums):
        left, right = 0, len(nums) -1
        result = []
        end = False
        while left <= right:
            end = False
            start = nums[left]
            while left + 1 <= len(nums)-1 and nums[left+1] == nums[left] +1:
                    end = nums[left+1]
                    left += 1
            if end:
                result.append(str(start) + '->' + str(end))
            else:
                result.append(str(start))
            left += 1
        return result
print(Solution().summaryRanges(input))
