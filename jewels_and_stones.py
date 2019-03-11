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

class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        dict, count = {}, 0
        for e in J:
            if e not in dict:
                dict[e] = None
        for e in S:
            if e in dict:
                count+=1
        return count

#Runtime: O(n+m) Space O(n)
print(Solution().numJewelsInStones(J1, S1))
print(Solution().numJewelsInStones(J2, S2))
