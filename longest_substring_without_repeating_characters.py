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
        repeats = set()
        maximum = 0
        left, right = 0, 0
        while left < len(s) and right < len(s):
            # safely expand to the right if char not in set
            if s[right] not in repeats:
                repeats.add(s[right])
                right += 1
                maximum = max(maximum, right - left)
            else:
            # if char is in set, we remove and move left pointer until right is clear
                repeats.remove(s[left])
                left += 1
        return maximum

print(Solution().lengthOfLongestSubstring(input))
