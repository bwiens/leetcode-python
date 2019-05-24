#!/usr/bin/python
# Benjamin Wiens
# N-Repeated Element in Size 2N Array(https://leetcode.com/problems/n-repeated-element-in-size-2n-array/)
# Leetcode Accepted

numbers = [1,2,3,3]
class Solution:
    def repeatedNTimes(self, A):
        n = (len(A)) //2
        count = {}
        #print(n)
        for number in A:
            if number in count:
                return number
            else:
                count[number] = 1
print(Solution().repeatedNTimes(numbers))
