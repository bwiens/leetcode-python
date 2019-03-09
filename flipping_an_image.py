#!/usr/bin/python
#Benjamin Wiens
#Flipping an Image (https://leetcode.com/problems/flipping-an-image/submissions/)
#Leetcode Accepted 
input = [[1,1,0],[1,0,1],[0,0,0]]
class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        #flip horizontally (swap)
        for rows in A:
            left = 0
            right = len(A[0])-1
            while left < right:
                rows[left], rows[right] = rows[right], rows[left]
        #invert so 1's become 0's, 0's become 1's
                left+=1
                right-=1
        for rows in A:
            for index, i in enumerate(rows):
                if i == 1:
                    rows[index] = 0
                else: 
                    rows[index] = 1
        return A

#O(n) time
print(Solution().flipAndInvertImage(input))
