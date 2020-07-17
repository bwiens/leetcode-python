#!/usr/bin/python

string1 = "aabcc"
string2 = "ccdee"

class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2:
            return True
        if len(str1) != len(str2):
            return False
        #cannot map to any new char
        if len(set(str2)) == 26:
            return False
        dict = {}
        for index, char in enumerate(str1):
            if char in dict and dict[char] != str2[index]:
                return False
            dict[char] = str2[index]
        return True

print(Solution().canConvert(string1, string2))
