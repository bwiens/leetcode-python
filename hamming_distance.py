#!/usr/bin/python
#Benjamin Wiens
#Hamming Distance

x = 1
y = 4

class Solution():
    def hammingDisatance(self, x, y):
        """
        :type: x int
        :type: y int
        :rtype: int
        """
        c = 0
        #convert to binary
        x = bin(x)[2:].zfill(8)
        y = bin(y)[2:].zfill(8)
        #count different bits
        for i in range(len(x)):
            if x[i] != y[i]:
                c += 1
        return c

print(Solution().hammingDisatance(x, y))
