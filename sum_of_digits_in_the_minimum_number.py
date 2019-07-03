#!/usr/bin/python
# Benjamin Wiens
# Sum of Digits in the Minimum Number (https://leetcode.com/problems/sum-of-digits-in-the-minimum-number/)
# Leetcode Accepted

input = [99,77,33,66,55]
import sys
class Solution:
    def sumOfDigits(self, A):
        minimum = sys.maxsize
        result = 0
        #get smallest element
        for number in A:
            minimum = min(minimum, number)
        #get sum of digits
        for digit in str(minimum):
            result = result + int(digit)
		#by checking remainder, see if odd or even
        if result % 2 == 0:
            return 1
        else:
            return 0

print(Solution().sumOfDigits(input))
