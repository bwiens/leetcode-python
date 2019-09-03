#!/usr/bin/python
# Benjamin Wiens
# Maximum Swap (https://leetcode.com/problems/maximum-swap/)
# O(n^2) version / Bruteforce

number = 2736

class Solution:
    def maximumSwap(self, num):
        A = list(str(num))
        # make weird copy of A
        result = A[:]
        for i in range(len(A)):
            for j in range(i+1,len(A)):
                A[i],A[j] = A[j],A[i]
                tmp = A[:]
                result = max(result, tmp)
                # swap back
                A[i],A[j] = A[j],A[i]
        return ''.join(result)

print(Solution().maximumSwap(number))
