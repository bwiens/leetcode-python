#!/usr/bin/python
# Benjamin Wiens
# Occurrences After Bigram (https://leetcode.com/problems/occurrences-after-bigram/)
# Leetcode Accepted

first = 'a'
second = 'good'
text = 'alice is a good girl she is a good student'

class Solution:
    def findOcurrences(self, text: str, first: str, second: str):
        result = []
        text_list = text.split()
        for index, word in enumerate(text_list):
            if word == first:
                if index < len(text_list) - 2:
                    if text_list[index+1] == second:
                        result.append(text_list[index+2])
        return result

print(Solution().findOcurrences(text, first, second))
