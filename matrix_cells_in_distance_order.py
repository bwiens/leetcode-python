#!/usr/bin/python
# Benjamin Wiens
# Matrix Cells in Distance Order (https://leetcode.com/problems/matrix-cells-in-distance-order)

R = 3
C = 4 
r0 = 0
c0 = 1
class Solution:
    def allCellsDistOrder(self, R, C, r0, c0):
        # create matrix
        column = [0] * C
        grid, result = [], []
        # populate the coordinates
        for i in range(0,R):
            grid.append(column)
        for rid, row in enumerate(grid):
            for cid, column in enumerate(row):
                result.append([rid,cid])
        #sort based on distance
        result.sort(key=lambda x: abs(x[0]-r0) + abs(x[1]-c0)) 
        return result

print(Solution().allCellsDistOrder(R,C,r0,c0))
