#!/usr/bin/python
# Benjamin Wiens
# Number Complement (https://leetcode.com/problems/number-complement/)

number = 5
class Solution:
    def findComplement(self, num):
        result = ''
        x = str(bin(num))
        for i in x[2:]:
            if i == '1':
                result = '0' + result
            else:
                result = '1' + result
        factor = 2**(len(result)-1)
        final = 0
        for i in result[::-1]:
            final = final + (int(i) * factor)
            factor = factor // 2
        return final

print(Solution().findComplement(number))
