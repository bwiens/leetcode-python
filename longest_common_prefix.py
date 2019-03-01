#!/usr/bin/python
#Benjamin Wiens
#Longest Common Prefix (https://leetcode.com/problems/longest-common-prefix/)
#Leetcode Accepted

input = ["aa","a","andromeda"]

class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
		#sort in ascending order 
        strs.sort(key=len)
        strings = len(strs)
        longest = ''
        same = True
        c, c2 = 0, 1
        for index, i in enumerate(strs[0]):
            if same != True:
                break
			#compare each character of the shortest word with the remaining word's corresponding character
            for j in strs[0:]:
                if not j:
                    same = False
                    break    
                if i != j[index]:
                    same = False
                    break
            if same == True:
                longest += i 
        return longest

print(Solution().longestCommonPrefix(input))
