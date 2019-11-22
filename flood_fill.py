#!/usr/bin/python
#Benjamin Wiens
#Floodfill (https://leetcode.com/problems/flood-fill/)
#Leetcode Accepted
input = [[0,0,1],[1,1,0]]

class Solution:
    def fill(self, image, rid, cid, newColor, oldColor):
        if rid < 0 or cid < 0 or rid > len(image) -1 or cid > len(image[0]) -1 or image[rid][cid] != oldColor:
            return
        image[rid][cid] = newColor
        #down
        self.fill(image, rid+1, cid, newColor, oldColor)
        #right
        self.fill(image, rid, cid+1, newColor, oldColor)
        #up
        self.fill(image, rid-1, cid, newColor, oldColor)
        #left
        self.fill(image, rid, cid-1, newColor, oldColor)
    def floodFill(self, image, sr, sc, newColor):
        if image[sr][sc] == newColor:
            return image
        oldColor = image[sr][sc]
        self.fill(image, sr, sc, newColor, oldColor)
        return image

print(Solution().floodFill(input, 1, 1, 2))
