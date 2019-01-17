#!/usr/bin/python
#Benjamin Wiens
#Longest Substring Without Repeating Characters (https://leetcode.com/problems/longest-substring-without-repeating-characters)
#Leetcode Accepted

input = "pwwkew"

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        repeats = []
        maximum = 0
        c = 0
        for index, i in enumerate(s):
            while c + index <= len(s) -1:
                # duplicate detected
                if s[index + c] in repeats:
                    if len(repeats) > maximum:
                        maximum = len(repeats)
                    repeats = []
                    c = 0
                    break
                else:
                    repeats.append(s[index + c])
                    c += 1
                    if len(repeats) > maximum:
                        maximum = len(repeats)
        return maximum

print(Solution().lengthOfLongestSubstring(input))
