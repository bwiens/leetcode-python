#!/usr/bin/python
#Benjamin Wiens
#Roman To Integer
#Leetcode Accepted (https://leetcode.com/problems/roman-to-integer)
input = "LVIII"
class Solution:
    def romanToInt(self, s: 'str') -> 'int':
#The trick is that the last letter is always added. Except the last one, if one letter is less than its latter one, this letter is subtracted.
        dict = {'I': 1,'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sum = 0
        #don't include last character
        for i in range(0, len(s)-1):
            if dict[s[i]] < dict[s[i+1]]:
                sum -= dict[s[i]]
            else: 
                sum += dict[s[i]]
        #last one is always added
        sum = dict[s[-1]] + sum
        return sum
print(Solution().romanToInt(input))
