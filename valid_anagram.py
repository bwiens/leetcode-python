#!/usr/bin/python
#Benjamin Wiens
#Valid Anagram (https://leetcode.com/problems/valid-anagram/)
#Leetcode Accepted 
s = "anagram"
t = "nagaram"
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #create dict with occurences:
        if s and not t:
            return False
        wdict = {}
        value = 0
        for i in t:
            if i not in wdict:
                wdict[i] = 1
            else:
                value = wdict.get(i)
                wdict[i] = value + 1
                
        for i in s:
            if i not in wdict:
                return False
            else:
                value = wdict.get(i)
                if value < 1:
                    return False
                if value == 1:
                    del wdict[i]
                else:
                    wdict[i] = value -1
                    
        #if we have letters left in the dict, we do
        #not have a valid anagram
        if len(wdict) > 0:
            return False
        else:
            return True
print(Solution().isAnagram(s, t))
#O(n) Runtime (linear), fastest solituin, with constant space O(1) 
