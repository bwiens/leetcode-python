#!/usr/bin/python
# Benjamin Wiens
# Implement strStr() (https://leetcode.com/problems/implement-strstr/) 

haystack = "hello"
needle = "ll"

class Solution:
    def strStr(self, haystack, needle) -> int:
        if not needle or needle == haystack:
            return 0
        for index, hay in enumerate(haystack):
            if needle[0] == hay and index + len(needle) -1 <= len(haystack):
                if len(needle) == 1:
                    return index
                #found first match, look for rest
                i = 1
                while index+i < len(haystack) and needle[i] == haystack[index+i]:
                    #check if last matched
                    if i == len(needle) -1:
                        return index
                    i += 1
        return -1

print(Solution().strStr(haystack,needle))
