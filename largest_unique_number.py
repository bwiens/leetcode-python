#!/usr/bin/python
# Benjamin Wiens
# Largest Unique Number (https://leetcode.com/contest/biweekly-contest-5/problems/largest-unique-number/)

numbers = [5,7,3,9,4,9,8,3,1]

class Solution:
    def largestUniqueNumber(self, A):
        hmap, ruled_out = {}, {}
        max_nr = -1
        for number in A:
            if number in hmap:
                ruled_out[number] = None
            else:
                hmap[number] = None
        for number in A:
            if number not in ruled_out:
                max_nr = max(max_nr, number)
        return max_nr
print(Solution().largestUniqueNumber(numbers))                
