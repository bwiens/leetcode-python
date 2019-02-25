#!/usr/bin/python
#Benjamin Wiens
#Reverse String (https://leetcode.com/problems/reverse-string)
#Leetcode Accepted
input = ["h","e","l", "l","o"]

class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) -1
        while left <= right:
            #swap
            s[left], s[right] = s[right], s[left]
            left  += 1
            right -= 1
        return s

print(Solution().reverseString(input))
