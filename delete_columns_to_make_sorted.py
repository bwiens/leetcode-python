#!/usr/bin/python
# Benjamin Wiens
# Delete Columns to Make Sorted (https://leetcode.com/problems/delete-columns-to-make-sorted/)

input = ["zyx","wvu","tsr"]
class Solution:
    def minDeletionSize(self, A):
        result = 0
        by_column = (list(zip(*A)))
        for row in by_column:
            for index, char in enumerate(row[1:], 1):
                if char < row[index-1]:
                    result += 1
                    break
        return result

print(Solution().minDeletionSize(input))
