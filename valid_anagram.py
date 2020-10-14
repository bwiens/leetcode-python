#!/usr/bin/python
#Benjamin Wiens
#Valid Anagram (https://leetcode.com/problems/valid-anagram/)
#Leetcode Accepted 
s = "anagram"
t = "nagaram"
class Solution:
    def isAnagram(self, s: str, t: str):
        count1 = [0] * 26
        count2 = [0] * 26
        for c in s:
            count1[ord(c) - ord('a')] += 1
        for c in t:
            count2[ord(c) - ord('a')] += 1
        return count1 == count2
print(Solution().isAnagram(s, t))
#O(n) Runtime (linear), fastest solituin, with constant space O(1) 
