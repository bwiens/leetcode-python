#!/usr/bin/python
# Benjamin Wiens
# Find Smallest Common Element in All Rows (https://leetcode.com/problems/find-smallest-common-element-in-all-rows/)

mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]

class Solution:
    def smallestCommonElement(self, mat):
        for number in mat[0]:
            i = 1
            found = True
            while i < len(mat)-1:
                if number in mat[i]:
                    i += 1
                    continue
                else:
                    found = False
                    break
            if i == len(mat)-1 and found:
                return number
        return -1

#Check if each number in row 0 exists in row 1 - N. If at any point we don't find the number from row 0 in a row, we can break. If we complete the last row without breaking, we have found the min number in all rows and return.

print(Solution().smallestCommonElement(mat))
