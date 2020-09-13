#!/usr/bin/python
# Benjamin Wiens

a = "1"
b = "1"

class Solution:
    def addBinary(self, a, b):
        a_list = list(a)
        b_list = list(b)
        carry = 0
        result = ''
        while a_list or b_list or carry:
            if a_list:
                carry += int(a_list.pop())
            if b_list:
                carry += int(b_list.pop())
            result += str(carry % 2)
            carry = carry // 2
        return result[::-1]

print(Solution().addBinary(a, b))
