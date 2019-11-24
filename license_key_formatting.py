#!/usr/bin/python
#Benjamin Wiens
#License Key Formatting (https://leetcode.com/problems/license-key-formatting/)
#Leetcode Accepted
input = "2-4A0r7-4k"
K = 4

class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S2 = S.replace('-', '')
        result = ''
        for index, char in enumerate(S2[::-1], 1):
            result += char.upper()
            if index % K == 0 and index != len(S2):
                result += '-'
        result = result[::-1]
        if not result: return ""
        if result[-1] == '-':
            return result[:len(result)-1]
        return result

print(Solution().licenseKeyFormatting(input, K))
