#!/usr/bin/python
# Benjamin Wiens
# Find All Duplicates in an Array (https://leetcode.com/problems/find-all-duplicates-in-an-array/)

numbers = [4,3,2,7,8,2,3,1]
class Solution:
    def findDuplicates(self, nums):
        result = []
        for index, number in enumerate(nums):
            if nums[abs(number)-1] < 0:
                result.append(abs(number))
            else:
                nums[abs(number)-1] = -1*nums[abs(number)-1]
        return result

print(Solution().findDuplicates(numbers))

