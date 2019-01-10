#!/usr/bin/python
#Benjamin Wiens
#Reverse Integer
#https://leetcode.com/problems/reverse-integer/submissions/
#Leetcode Accepted

input = -7331
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = ""
        result_int = 0
        for i in reversed(str(abs(x))):
            result = result + i
        result_int = int(result)
        #check for "overflow"
        if result_int > pow(2, 31) - 1 or result_int < - pow(2, 31):
            return 0
        else:
            #if initial number is negative
            if x < 0:
                return(result_int * -1)
            else:
                return(result_int)

print(Solution().reverse(input))
