#!/usr/bin/python
# Benjamin Wiens
# Repeated DNA Sequences (https://leetcode.com/problems/repeated-dna-sequences/)
# Leetcode Accepted
s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
class Solution:
    def findRepeatedDnaSequences(self, s):
        length = len(s)
        hmap, result, output = {}, {}, []
        for index, char in enumerate(s):
            if length - index >= 0:
                #print(s[index:index+10])
                if s[index:index+10] not in hmap:
                    hmap[s[index:index+10]] = None
                else:
                    if s[index:index+10] not in result:
                        result[s[index:index+10]] = None
                        output.append(s[index:index+10])
        return output

print(Solution().findRepeatedDnaSequences(s))
