#!/usr/bin/python
# Benjamin Wiens
# Number of Lines to Write String (https://leetcode.com/problems/number-of-lines-to-write-string/)

widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
S = "abcdefghijklmnopqrstuvwxyz"
class Solution:
    def numberOfLines(self, widths, S):
        alphabet = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
        count = 1
        total = 0
        for char in S:
            value = widths[alphabet[char]]
            # could also use value = widths[ord(char)-97]
            # ord('a') is 97
            if total + value <= 100:
                total += value
            else:
                count += 1
                total = value
        return [count, total]

print(Solution().numberOfLines(widths,S))
