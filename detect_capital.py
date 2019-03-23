#!/usr/bin/python
# Benjamin Wiens
# Detect Capital (https://leetcode.com/problems/detect-capital/)
# Leetcode Accepted

word = "Leetcode" 
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        count = 0 
        capdict = {"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"}
        for char in word:
            if char in capdict:
                count += 1
        if len(word) == count:
            return True
        elif count == 1 and word[0] in capdict:
            return True
        elif count == 0:
            return True
        else:
            return False

print(Solution().detectCapitalUse(word))
