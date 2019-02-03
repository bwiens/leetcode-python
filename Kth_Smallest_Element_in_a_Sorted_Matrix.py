#!/usr/bin/python
#Benjamin Wiens
#Kth Smallest Element in a Sorted Matrix
#Leetcode Accepted (https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/)

input = [[1,2],[1,3]]
k = 2

class Solution:
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        numbers =[]
        for rows in matrix:
            for columns in rows:
                numbers.append(columns)
        numbers = sorted(numbers, reverse=False)
        return numbers[k-1]

print(Solution().kthSmallest(input,k))
