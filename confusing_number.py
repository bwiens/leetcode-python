#!/usr/bin/python
# Benjamin Wiens
# Confusing Number (https://leetcode.com/problems/confusing-number)

number = 619

class Solution:
    def confusingNumber(self, N):
        rotatable = {'0': '0', '1': '1', '8': '8', '6': '9', '9': '6'}
        string = str(N)
        result = ''
        for char in string:
            if char not in rotatable:
                return False
            else:
                result = result + rotatable[char]
        #compare the reverse to the original
        if N != int(result[::-1]):
            return True
        else:
            return False

print(Solution().confusingNumber(number))
