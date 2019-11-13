#!/usr/bin/python
# Benjamin Wiens
# Number of Closed Islands (https://leetcode.com/problems/number-of-closed-islands/)

grid =[ [1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
class Solution:
    def closedIsland(self, grid):
        def close(rid, cid, grid):
            if rid < 0 or cid < 0 or rid > len(grid)-1 or cid > len(grid[0])-1 or grid[rid][cid] != 0:
                return
            grid[rid][cid] = 1
            close(rid+1, cid, grid)
            close(rid, cid+1, grid)
            close(rid-1, cid, grid)
            close(rid, cid-1, grid)
        def countI(rid, cid, grid):
            if rid < 0 or cid < 0 or rid > len(grid)-1 or cid > len(grid[0])-1 or grid[rid][cid] != 0:
                return
            grid[rid][cid] = 1
            countI(rid+1, cid, grid)
            countI(rid, cid+1, grid)
            countI(rid-1, cid, grid)
            countI(rid, cid-1, grid)
        # "close" the islands at the edge
        for rid, row in enumerate(grid):
            for cid, column in enumerate(row):
                if cid == 0 or rid == 0 or rid == len(grid)-1 or cid == len(grid[0])-1:
                    if column == 0:
                        close(rid,cid,grid)
        # cound number of closed islands
        count = 0
        for rid, row in enumerate(grid):
            for cid, column in enumerate(row):
                if column == 0:
                    count += 1
                    countI(rid,cid,grid)
        return count
print(Solution().closedIsland(grid))
