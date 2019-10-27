#!/usr/bin/python
# Benjamin Wiens
# Maximum Length of a String With Unique Characters (https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/)

arr = ["cha","r","act","ers"]

class Solution:
    def maxLength(self, arr):
        maximum = 0
        for index, string in enumerate(arr):
            if len(string) != len(set(string)):
                continue
            tmp = string
            for index2, string2 in enumerate(arr):
                if index != index2:
                    if len(tmp + string2) == len(set(tmp + string2)):
                        tmp = tmp + string2 
            maximum = max(len(tmp), maximum)
            tmp = 0
        return maximum

print(Solution().maxLength(arr))
