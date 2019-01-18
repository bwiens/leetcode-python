#!/usr/bin/python
#Benjamin Wiens
#Longest Substring With At Most Two Distinct Characters (https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters)
#Leetcode Accepted
input = "eceba"

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        maximum = 0
        c = 1
        if len(set(s)) <= 2:
            return len(s)
        for index, i in enumerate(s):
            c = 1
            while c + index <= len(s):
                #print(s[index:index + c])
                if len(set(s[index:index + c])) <= 2:
                    c = len(s[index:index +c])
                    if c > maximum:
                        maximum = c
                    c += 1
                if len(set(s[index:index + c])) > 2:
                    c = 1
                    break
        return maximum

print(Solution().lengthOfLongestSubstringTwoDistinct(input))
