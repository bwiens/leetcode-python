#!/usr/bin/python
#Benjamin Wiens
#Word Break II (https://leetcode.com/problems/word-break-ii/description/)
from itertools import combinations

#input
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
#arrays to store combinations
contained = []
output = []
class Solution (object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        #get all substrings matching words in the dict
        for i in range(len(s)):
            for j in range(len(s)+1):
                sub = s[i:j]
                if sub in wordDict:
                        contained.append(s[i:j])

        #iterate through matched words
        for n in range (1, len (contained) + 1):
            #use itertools.combinations to bruteforce the possibilities
            for combination in combinations(contained, n):
                #it's a match
                if s == (''.join((combination))):
                    to_str = ((' '.join((combination))))
                    output.append(to_str)

        return output

print(Solution().wordBreak(s,wordDict))
