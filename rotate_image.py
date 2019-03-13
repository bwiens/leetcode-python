#!/usr/bin/python
#Benjamin Wiens
#Rotate an Image (https://leetcode.com/problems/rotate-image/)
#Leetcode Accepted
matrix = [[1,2,3],[4,5,6],[7,8,9]]
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
	#reverse
        matrix.reverse()
	#transpose
        for i in range (len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix
print(Solution().rotate(matrix))
