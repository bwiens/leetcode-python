#!/usr/bin/python
# Benjamin Wiens
# 1232 Check if it is a Straight Line (https://leetcode.com/problems/check-if-it-is-a-straight-line/)

coordinates = [[-7,-3],[-7,-1],[-2,-2],[0,-8],[2,-2],[5,-6],[5,-5],[1,7]] 

class Solution:
    def checkStraightLine(self, coordinates):
        # calculate m, special case for vertical line
        if (coordinates[1][0] - coordinates[0][0]) == 0:
            m = 0
        else:
            m = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])
        # substitute to get b
        b = coordinates[0][1] - ( m * coordinates[0][0])
        for index, coordinate in enumerate(coordinates[1:], 1):
            if (coordinates[index][0] - coordinates[0][0]) == 0:
                m2 = 0
            else:
                m2 = (coordinates[index][1] - coordinates[0][1]) / (coordinates[index][0] - coordinates[0][0])
            b2 = coordinates[index][1] - ( m2 * coordinates[index][0])
            if b != b2 or m != m2:
                return False
        return True

print(Solution().checkStraightLine(coordinates))
