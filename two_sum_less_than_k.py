#!/usr/bin/python
# Benjamin Wiens
# Two Sum Less than K (https://leetcode.com/problems/two-sum-less-than-k/)

A = [34,23,1,24,75,33,54,8]
K = 60
class Solution:
    def twoSumLessThanK(self, A, K):
        A.sort()
        left, right = 0, len(A) -1 
        maximum = 0
        while left < right:
            if A[left] + A[right] < K:
                maximum = max(maximum, A[left] + A[right])
                left += 1 
            else:
                right -= 1
        if maximum == 0:
            return -1
        return maximum

print(Solution().twoSumLessThanK(A,K))
