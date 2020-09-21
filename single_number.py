#!/usr/bin/python
# Benjamin Wiens
# Single Number (https://leetcode.com/problems/single-number/)
# Leetcode Accepted

numbers = [2,2,1]

class Solution:
    def singleNumber(self, nums):
        hmap = {}
        candidate = -1
        for number in nums:
            if number in hmap:
                hmap.pop(number)
            else:
                hmap[number] = 1
        for key, value in hmap.items():
                return key
        return -1

class Solution2:
    def singleNumber(self, nums):
        # The most crucial trick here is to recognize that if you XOR any same number together, you cancel it out (=0).
        result = 0
        for number in nums:
            result ^= number
        return result

print(Solution().singleNumber(numbers))
print(Solution2().singleNumber(numbers))
#O(n) time and space
