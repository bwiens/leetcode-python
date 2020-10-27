#!/usr/bin/python

class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0: return '0'
        result = ''
        digit = 0
        if num < 0:
            sign = '-'
        else:
            sign = ''
        num = abs(num)
        while num:
            digit = num%7
            result += str(digit)
            num//=7
        return sign + result[::-1]
print(Solution().convertToBase7(100))
