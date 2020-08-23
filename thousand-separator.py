#!/usr/bin/python

number = 1234

class Solution:
    def thousandSeparator(self, n):
        if len(str(int)) < 3:
            return str(n)
        string = str(n)[::-1]
        i = len(string) -1
        result = ''
        for index, s in enumerate(string, 1):
            result += s
            if index % 3 == 0:
                result += '.'
            i -= 1
        if result[-1] == '.':
            return result[:-1][::-1]
        return result[::-1]

print(Solution().thousandSeparator(number)) 
