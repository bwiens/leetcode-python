#!/usr/bin/python
#Benjamin Wiens
#https://leetcode.com/problems/plus-one/
#Leetcode Accepted


input = [1, 2, 3]

class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s = ""
        s2 = 0
        output = []
        for i in digits:
            s = s + str(i)
        s2 = int(s) + 1
        output = [int(x) for x in str(s2)]
        return output

print(Solution().plusOne(input))
