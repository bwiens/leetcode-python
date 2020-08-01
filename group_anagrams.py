#!/usr/bin/python

input = ["eat", "tea", "tan", "ate", "nat", "bat"]

class Solution:
    def groupAnagrams(self, strs):
        dict, result, tmp = {}, [], []
        for string in strs:
            string2 = ''.join(sorted(string))
            if string2 in dict:
                dict[string2].extend([string])
            else:
                dict[string2] = [string]
        for key, value in dict.items():
            tmp = []
            for v in value:
                tmp.append(v)
            result.append(tmp)
        return result

print(Solution().groupAnagrams(input))
