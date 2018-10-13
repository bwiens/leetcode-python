#!/usr/bin/python
#Benjamin Wiens
#Jewels and Stones case sensitive iteratively

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
        c=0
        i = j = 0
        #iterate through stones for each jewel
        for i in range(len(J)):
            for j in range(len(S)):
                if J[i] == S[j]:
                    c+=1
        return c

print(Solution().numJewelsInStones(J1, S1))
print(Solution().numJewelsInStones(J2, S2))
#Since we have two for loops, the time complexity is O(n^2)
