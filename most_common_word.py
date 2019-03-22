#!/usr/bin/python
# Benjamin Wiens
# Most Common Word (https://leetcode.com/problems/most-common-word/)
# Leetcode Accepted

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

import re 
class Solution:
    def mostCommonWord(self, paragraph, banned):
        #remove punctuation
        cdict = {}
        max = 0
        max_word = ''
        paragraph = re.sub("[.,;!?'']",' ', paragraph)
        paragraph = paragraph.lower()
        paragraph_list = paragraph.split()
        for i in paragraph_list:
            if i not in banned:
                if i not in cdict:
                    cdict[i] = 1
                else:
                    cdict[i] += 1
        for key, value in cdict.items():
            if max < value:
                max_word = key
                max = value
        return max_word

print(Solution().mostCommonWord(paragraph,banned))
