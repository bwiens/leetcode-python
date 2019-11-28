#!/usr/bin/python
# Benjamin Wiens
# Path With Maximum Gold (https://leetcode.com/problems/path-with-maximum-gold/)

path = [[0,6,0],[5,8,7],[0,9,0]]

class Solution:
    def getMaximumGold(self, grid):
        result, maximum, mx = 0, 0, 0
        #use mx locally in thus function
        def findGold(rid, cid, sum):
            if rid < 0 or cid < 0 or rid >= len(grid) or cid >= len(grid[0]) or grid[rid][cid] == 0 or grid[rid][cid] > 100:
                return sum
            mx = 0
            sum += grid[rid][cid]
            grid[rid][cid] += 1000
            mx = max(findGold(rid+1, cid, sum), mx)
            mx = max(findGold(rid, cid+1, sum), mx)
            mx = max(findGold(rid-1, cid, sum), mx)
            mx = max(findGold(rid, cid-1, sum), mx)
            grid[rid][cid] -= 1000
            return mx
            
        for rid, row in enumerate(grid):
            for cid, column in enumerate(row):
                if column != 0:
                    sum = 0
                    result = findGold(rid, cid, sum)
                    maximum = max(result, maximum)
        return maximum

print(Solution().getMaximumGold(path))
