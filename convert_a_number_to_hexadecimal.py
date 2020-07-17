#!/usr/bin/python

number = 26

class Solution:
    def toHex(self, num: int) -> str:
        if num == 0: return '0'
        map = '0123456789abcdef'
        result = ''
        #if negative (two's compliment)
        if num<0: num += 2 ** 32
        while num > 0:
            digit = num % 16
            num = (num-digit) // 16
            result += str(map[digit])
        return result[::-1]

print(Solution().toHex(number))
