#!/usr/bin/python
# Benjamin Wiens
# Repeated String Match (https://leetcode.com/problems/repeated-string-match/)
A = "abcd"
B = "cdabcdab"

import math
class Solution:
    def repeatedStringMatch(self, A, B):
	#the key here is to use the ceiling!!!!!!
        maximum = math.ceil(len(B)/len(A))
        A2 = A[:]
        if B in A:
            return 1
        i = 1
        for j in range(maximum):
            i += 1
            A += A2
            if B in A:
                return i
        return -1

print(Solution().repeatedStringMatch(A, B))

