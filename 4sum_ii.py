#!/usr/bin/python
# Benjamin Wiens
# 4Sum II (https://leetcode.com/problems/4sum-ii/)

A = [-1,-1]
B = [-1,1]
C = [-1,1]
D = [1,-1]
class Solution:
    def fourSumCount(self, A, B, C, D) -> int:
        abcount = {}
        total = 0
        for a in A:
            for b in B:
                if a+b in abcount:
                    abcount[a+b] += 1
                else:
                    abcount[a+b] = 1
        for c in C:
            for d in D:
                #lookup inverse
                tmp = c + d
                if -tmp in abcount:
                    total += abcount[-tmp]
        return total

print(SOlution().fourSumCount(A,B,C,D))
