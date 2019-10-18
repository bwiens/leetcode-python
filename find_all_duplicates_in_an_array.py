#!/usr/bin/python
# Benjamin Wiens
# Find All Duplicates in an Array (https://leetcode.com/problems/find-all-duplicates-in-an-array/)

numbers = [4,3,2,7,8,2,3,1]
class Solution:
    def findDuplicates(self, nums):
        hmap = {}
        result = []
        for number in nums:
            if number not in hmap:
                hmap[number] = 1
            else:
                result.append(number)
        return result

print(Solution().findDuplicates(numbers))
