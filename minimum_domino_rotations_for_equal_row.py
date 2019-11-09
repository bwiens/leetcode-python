#!/usr/bin/python
# Benjamin Wiens
# Minimum Domino Rotations for Equal Row (https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/)

A = [2,1,2,4,2,2]
B = [5,2,6,2,3,2]

import sys
class Solution:
    def minDominoRotations(self, A, B):
        count, result = 0, sys.maxsize
        for i in range(1, 7):
            count = 0
            rotations = 0
            for idx, num in enumerate(A):
                # process row A
                if num == i:
                    count += 1
                elif B[idx] == i:
                        rotations += 1
            if count == len(A):
                return 0
            if rotations + count == len(A):
                result = min(result, rotations)
            count = 0
            rotations = 0
            for idx, num in enumerate(B):
                # process row A
                if num == i:
                    count += 1
                elif A[idx] == i:
                        rotations += 1
            if count == len(A):
                return 0
            if rotations + count == len(A):
                result = min(result, rotations)
        if result == sys.maxsize:
            return -1
        return result

print(Solution().minDominoRotations(A,B))
