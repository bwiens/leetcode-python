#!/usr/bin/python
#Benjamin Wiens
#License Key Formatting (https://leetcode.com/problems/license-key-formatting/)
#Leetcode Accepted
input = "2-4A0r7-4k"
K = 4
class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        list2, result = [], []
        formatted = ""
        S = S.upper()
        list2 = list(S)
        list2.reverse()
        c = 0
        Flag = False
        for i in list2:
            if c == K:
                if i == "-":
                    result.append(i)
                    c = 0
                else:
                    result.append("-")
                    result.append(i)
                    c = 1
                    Flag = True
            if c < K and Flag == False:
                if i != "-":
                    result.append(i)
                    c+=1
            Flag = False
        #special cases
        if len(result) > 0:
            if result[-1] == "-":
                result.pop()
        result.reverse()
        #format back to string
        formatted = ''.join(result)
        return formatted

print(Solution().licenseKeyFormatting(input, K))
