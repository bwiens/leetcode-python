#!/usr/bin/python

num1 = "10"
num2 = "12"

class Solution:
    def addStrings(self, num1, num2):
        lista = list(num1)
        listb = list(num2)
        carry = 0
        result = ''
        while lista or listb or carry:
            if lista:
                carry += int(lista.pop())
            if listb:
                carry += int(listb.pop())
            result += str(carry % 10)
            carry = carry // 10
        return result[::-1]

print(Solution().addStrings(num1, num2))
