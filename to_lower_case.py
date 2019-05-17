#!/usr/bin/python
# Benjamin Wiens
# To Lower Case (https://leetcode.com/problems/to-lower-case/)
# Leetcode Accepted 

str = 'Hello'

class Solution:
    def toLowerCase(self, str: str) -> str:
        udict = {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'e', 'F': 'f', 'G': 'g', 'H': 'h', 'I': 'i', 'J': 'j', 'K': 'k', 'L': 'l', 'M': 'm', 'N': 'n', 'O': 'o', 'P': 'p', 'Q': 'q', 'R': 'r', 'S': 's', 'T': 't', 'U': 'u', 'V': 'v', 'W': 'w', 'X': 'x', 'Y': 'y', 'Z': 'z'}
        result = ''
        for i in str:
            if i in udict:
                result += (udict.get(i))
            else:
                result += i
        return result
print(Solution().toLowerCase(str))        
