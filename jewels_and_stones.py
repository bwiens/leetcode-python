#!/usr/bin/python
#Benjamin Wiens
#Jewels and Stones (https://leetcode.com/problems/jewels-and-stones/)
#Leetcode Accepted

#Jewels
J1 = "aA"
J2 = "z"
#Stones
S1 = "aAAbbbb"
S2 = "ZZ"

class Solution:
    def numJewelsInStones(self, J: 'str', S: 'str') -> 'int':
        if not J:
            return 0
        jewels = 0
        for i in S:
            if i in J:
                jewels += 1
        return jewels

print(Solution().numJewelsInStones(J1, S1))
print(Solution().numJewelsInStones(J2, S2))
