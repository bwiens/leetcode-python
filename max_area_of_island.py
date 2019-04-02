#!/usr/bin/python
# Benjamin Wiens
# Max Area of Island (https://leetcode.com/problems/max-area-of-island/)
# Leetcode Accepted

island = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]

class Solution:
    def maxAreaOfIsland(self, grid):
        def count_neighbors(rindex, cindex, count):
            #print(rindex, cindex)
            if rindex < 0 or rindex > len(grid) -1 or cindex < 0 or cindex > len(grid[0])-1 or grid[rindex][cindex] != 1:
                return count
            grid[rindex][cindex] = 0
	    # mark the island as visited if it passes the big bounds check
            # increment count and recursively do count = count_neighbors
            count += 1
            #up
            count = count_neighbors(rindex-1, cindex, count)
            #down
            count = count_neighbors(rindex+1, cindex, count)
            #left
            count = count_neighbors(rindex, cindex-1, count)
            #right
            count = count_neighbors(rindex, cindex+1, count)
            
            return count
            
            
        count, maximum = 0, 0
        for rindex, row in enumerate(grid):
            for cindex, c in enumerate(row):
                count = 0
                if c == 1:
                    count = count_neighbors(rindex, cindex, count)
                #print(count)
                if count > maximum:
                    maximum = count
        return maximum

print(Solution().maxAreaOfIsland(island))
