#!/usr/bin/python
# Benjamin Wiens
# Counting Bits (https://leetcode.com/problems/counting-bits)
number = 2

class Solution:
    def countBits(self, num):
        result = []
        for i in range(0,num+1):
            binary = bin(i)[2:]
            count = 0
            for digit in binary:
                if int(digit) == 1: 
                    count += 1
            result.append(count)
        return result

print(Solution().countBits(number))
