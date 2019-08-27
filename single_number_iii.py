#!/usr/bin/python
# Benjamin Wiens
# Single Number III (https://leetcode.com/problems/single-number-iii)

numbers = [1,2,1,3,2,5]

class Solution:
    def singleNumber(self, nums):
        result, hmap = [], {}
        for number in nums:
            if number in hmap:
                hmap[number] += 1
            else:
                hmap[number] = 1
        for number in nums:
            if hmap.get(number) == 1:
                result.append(number)
        return result

print(Solution().singleNumber(numbers))
