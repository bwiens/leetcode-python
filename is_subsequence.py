#!/usr/bin/python
#Benjamin Wiens
#Is Subsequence (https://leetcode.com/problems/is-subsequence)
#Leetcode Accepted
s = "abc"
t = "ahbgdc"
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        lastindex = 0
        found = False
        for index, i in enumerate(s):
            found = False
			#start after index of last found
            for j in range(lastindex,len(t)):
                if i == t[j]:
                    found = True
                    lastindex+=1
                    break
                lastindex+=1
            if found == False:
                return False
        return True

print(Solution().isSubsequence(s,t))
