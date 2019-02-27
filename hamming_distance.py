#!/usr/bin/python
#Benjamin Wiens
#Hamming Distance (https://leetcode.com/problems/hamming-distance)
#Leetcode Accepted 
x = 1
y = 4

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        hamming = 0
        binx = bin(x)[2:]
        biny = bin(y)[2:]
        if len(binx) > len(biny):
            biny = biny.zfill(len(binx))
        elif len(biny) > len(binx):
            binx = binx.zfill(len(biny))
        #print(binx,biny)
        for index, i in enumerate(binx):
            if i != biny[index]:
                hamming += 1
        return hamming
print(Solution().hammingDistance(x, y))
