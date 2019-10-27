#!/usr/bin/python
# Benjamin Wiens
# Find Positive Integer Solution For a Given Equation (https://leetcode.com/problems/find-positive-integer-solution-for-a-given-equation/)

class Solution:
    def findSolution(self, customfunction, z):
        result = []
        for i in range(1, z+1):
            x = i
            for j in range(1, z+1):
                y = j
                if customfunction.f(x,y) == z:
                    result.append([x,y])
                if customfunction.f(x,y) > z:
                    break
        return result
