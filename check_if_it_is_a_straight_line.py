#!/usr/bin/python
# Benjamin Wiens
# 1232 Check if it is a Straight Line (https://leetcode.com/problems/check-if-it-is-a-straight-line/)

coordinates = [[-7,-3],[-7,-1],[-2,-2],[0,-8],[2,-2],[5,-6],[5,-5],[1,7]] 

class Solution:
    def checkStraightLine(self, coordinates):
        # calculate slope ( y = mx + b) from first two points, starting with m
        # the special case to watch out for is if there is a vertical line as we cannot divide by 0
        if (coordinates[1][0] - coordinates[0][0]) == 0:
            m = 0
        else:
            m = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])
        # now get b by substituting
        b = coordinates[0][1] - ( m * coordinates[0][0])
        #print(m, b)
        for index, coordinate in enumerate(coordinates[1:], 1):
            if (coordinates[index][0] - coordinates[0][0]) == 0:
                m2 = 0
            else:
                m2 = (coordinates[index][1] - coordinates[0][1]) / (coordinates[index][0] - coordinates[0][0])
            b2 = coordinates[index][1] - ( m2 * coordinates[index][0])
            if b == b2 and m == m2:
                continue
            else:
                return False
        return True

print(Solution().checkStraightLine(coordinates))
