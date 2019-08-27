#!/usr/bin/python
# Benjamin Wiens
# Single Number II (https://leetcode.com/problems/single-number-ii)

numbers = [2,2,3,2]

class Solution:
    def singleNumber(self, nums):
        hmap = {}
        for number in nums:
            if number in hmap:
                hmap[number] += 1
            else:
                hmap[number] = 1
        for number in nums:
            if hmap.get(number) == 1:
                return number

print(Solution().singleNumber(numbers))
