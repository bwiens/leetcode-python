#!/usr/bin/python
# Benjamin Wiens
# Max Increase to Keep City Skyline (https://leetcode.com/problems/max-increase-to-keep-city-skyline)
# Leetcode Accepted

city = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]

class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        rmax, cmax, height = 0, 0, 0
        rows, columns = [], []
        # left and right max buildings (max of each row)
        for rindex, row in enumerate(grid):
            rows.append(max(row))
            cmax = 0
        # find top and bottom max buildings (max of each columns)
        columns = [max(cmax) for cmax in zip(*grid)]
        # calculate the difference of the min of left/right and top/bottom view
        for rindex, row in enumerate(grid):
            for cindex, column in enumerate(row):
                height += min(rows[rindex],columns[cindex]) - column
        return height
#Runtime O(n^2) where NN is the number of rows (and columns) of the grid.

print(Solution().maxIncreaseKeepingSkyline(city))
