#!/usr/bin/python
#Benjamin Wiens
#Binary Gap
#Given a positive integer N, find and return the longest distance between two consecutive 1's in the binary representation of N.
#Example 22 should give 2 (bin:10110) 
x = 22

class Solution:
        def binaryGap(self, n):
            """
            :type n: int
            :rtype: int
            """
            c = distance = 0
            counting = not True
            #convert to binary and add 0 padding
            n = bin(x)[2:].zfill(8)
            for i in range(len(n)):
                if (n[i] == "1") & (counting is True):
                    #print("cons. 1 found at:" , i, n[i])
                    #consec. 1 found
                    c += 1
                    #determine the longer consec. distance of 1's
                    if distance < c:
                        distance = c
                        #reset
                        c = 0
                if (n[i] == "1") & (counting is not True):
                    #first 1 found
                        counting = True
                        c = 0
                if (n[i] == "0") & (counting is True):
                #if no 1 then count distance
                     c =+ 1
            n = distance
            return n

print(Solution().binaryGap(x))
