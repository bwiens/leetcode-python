#!/usr/bin/python
#Benjamin Wiens
#Floodfill (https://leetcode.com/problems/flood-fill/)
#Leetcode Accepted
input = [[0,0,1],[1,1,0]]

class Solution:

    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        def fill(row, column):
            if image[row][column] == color:
                image[row][column] = newColor
                # up
                if row - 1 >= 0:
                    fill(row - 1, column)
                # down
                if row + 1 < len(image):
                    fill(row + 1, column)
                # left
                if column - 1 >= 0:
                    fill(row, column - 1)
                # right
                if column + 1 < len(image[0]):
                    fill(row, column + 1)
        color = image[sr][sc]
        if color == newColor:
            return image
        fill(sr, sc)
        return image

print(Solution().floodFill(input, 1, 1, 2))
