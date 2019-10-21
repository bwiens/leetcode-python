#!/usr/bin/python
# Divide Chocolate (https://leetcode.com/problems/divide-chocolate/)

sweetness = [1,2,3,4,5,6,7,8,9]
K = 5
class Solution:
    def maximizeSweetness(self, sweetness, K):
        K2 = K+1
        #given minimum m, can we divide into K pieces
        def possible(x):
            k, temp = 0, 0
            for a in sweetness:
                temp += a
                if temp >= x:
                    k, temp = k + 1, 0
            return k >= K2
    
        l, h = min(sweetness), sum(sweetness)
        while l < h:
            m = (l + h + 1) // 2
            if possible(m):
                l = m
            else:
                h = m - 1
        return l

print(Solution().maximizeSweetness(sweetness,K))
