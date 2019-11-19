#!/usr/bin/python
# Benjamin Wiens
# Minimum Domino Rotations for Equal Row (https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/)

A = [2,1,2,4,2,2]
B = [5,2,6,2,3,2]

class Solution:
    def minDominoRotations(self, A, B):
        result = []
        for i in range(2):
            if i == 0:
                k = A[0]
            else:
                k = B[0]
            count_a = 0
            rotate_a = 0
            count_b = 0
            rotate_b = 0
            for j in range(len(A)):
                # side A
                if A[j] == k:
                    count_a += 1
                elif B[j] == k:
                    rotate_a += 1
                # side B
                if B[j] == k:
                    count_b += 1
                elif A[j] == k:
                    rotate_b += 1
            # Both Sides might be equal with rotating. return the minimum
            if count_a + rotate_a == len(A):    
                result.append(min(count_a, rotate_a))
            if count_b + rotate_b == len(A):    
                result.append(min(count_b, rotate_b))
            if result:
                return min(result)
        return -1
print(Solution().minDominoRotations(A,B))
