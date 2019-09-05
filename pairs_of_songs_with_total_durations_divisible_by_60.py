#!/usr/bin/python
# Benjamin Wiens
# Pairs of Songs With Total Durations Divisible by 60 (https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/)

input = [30,20,150,100,40]

class Solution:
    def numPairsDivisibleBy60(self, time):
        hmap = {}
        result = 0
        x = 0
        for number in time:
            remainder = number % 60
            # get complement
            x = (60-remainder) % 60
            if x in hmap:
                result += hmap.get(x)
            if remainder in hmap:
                hmap[remainder] += 1
            else:
                hmap[remainder] = 1
        return result

print(Solution().numPairsDivisibleBy60(input))
