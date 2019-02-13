#!/usr/bin/python
# Benjamin Wiens
# Find All Numbers (https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/)
# Leetcode Accepted
input = [4,3,2,7,8,2,3,1]
class Solution:
    def findDisappearedNumbers(self, nums: 'List[int]') -> 'List[int]':
        if not nums:
            return []
        compare, missing = {}, []
        length = (len(nums))
        #insert complete range into dict
        for i in nums:
            if i not in compare:
                compare[i] = None
        for i in range(1, length+1):
            if i not in compare:
                missing.append(i)
        return missing

print(Solution().findDisappearedNumbers(input))
