#!/usr/bin/python
# Benjamin Wiens
# Add Digits (https://leetcode.com/problems/add-digits/)

number = 38
class Solution:
    def addDigits(self, num):
        result = ''
        while len(str(num)) != 1:
            for char in str(num):
                if result:
                    result = str(int(result)+int(char))
                else:
                    result = char
            num = int(result)
            result = ''
        return num

print(Solution().addDigits(number))
