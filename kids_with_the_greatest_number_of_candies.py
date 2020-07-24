#!/usr/bin/python

candies = [2,3,5,1,3]
extraCandies = 3

class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        result = []
        maximum = max(candies)
        for candy in candies:
            if candy + extraCandies >= maximum:
                result.append(True)
            else:
                result.append(False)
        return result

print(Solution().kidsWithCandies(candies, extraCandies))
