#!/usr/bin/python
#Benjamin Wiens
#Number of Islands https://leetcode.com/problems/number-of-islands/
#Leetcode Accepted

input = [["1","1","0","0","0"],
         ["1","1","0","0","0"],
         ["0","0","1","0","0"],
         ["0","0","0","1","1"]]


def landToWater(grid, rindex, index, column_length, row2_length):
    if rindex < 0 or index < 0 or rindex > (row2_length - 1) or index > (column_length - 1) or grid[rindex][index] != "1":
        return
    grid[rindex][index] = "0"
    # down
    landToWater(grid, rindex - 1, index, column_length, row2_length)
    # left
    landToWater(grid, rindex, index - 1, column_length, row2_length)
    # up
    landToWater(grid, rindex + 1, index, column_length, row2_length)
    # right
    landToWater(grid, rindex, index + 1, column_length, row2_length)

class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        row2_length = len(grid)
        c=0
        for rindex, row in enumerate(grid):
            print(row)
            for index, i in enumerate(row):
                column_length = len(row)
                print("rindex ", rindex, "index: " , index, "i ", i)
                if i == "1":
                    c+=1
                    landToWater(grid, rindex, index, column_length, row2_length)
        print(grid)
        return c


print(Solution().numIslands(input))
