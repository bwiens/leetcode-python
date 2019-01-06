#!/usr/bin/python
# Benjamin Wiens
# Island Perimeter
# Leetcode Accepted (https://leetcode.com/problems/island-perimeter/)

input = [
 [0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

#for every 1, count how many 0s or borders are adjacent
def hasNeighbour(grid, rindex, cindex, c):
    #up
    if rindex - 1 >= 0:
        if (grid[rindex - 1][cindex]) == 0:
            c += 1
    else:
        c += 1
    #down
    if rindex + 1 <= (len(grid) -1):
        if (grid[rindex + 1][cindex]) == 0:
            c += 1
    else:
        c += 1
    #left
    if cindex - 1 >= 0:
        if (grid[rindex][cindex - 1]) == 0:
            c += 1
    else:
        c += 1
    #right
    if cindex + 1 <= len(grid[0]) - 1:
        if (grid[rindex][cindex + 1]) == 0:
            c += 1
    else:
        c += 1
    return c

class Solution:
    def islandPerimeter(self, grid):
        """
        :param grid: List[List[int]]
        :return: int
        """
        c = 0
        for rindex, row in enumerate(grid):
            for cindex, column in enumerate(row):
               if column == 1:
                   c = hasNeighbour(grid, rindex, cindex, c)
        return c
print(Solution().islandPerimeter(input))
