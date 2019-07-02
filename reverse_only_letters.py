#!/usr/bin/python
# Benjamin Wiens
# Reverse Only Letters (https://leetcode.com/problems/reverse-only-letters)
# Leetcode Accepted

input = "Test1ng-Leet=code-Q!"
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        stack = []
        result = ''
        hmap = {}
        for index, char in enumerate(S):
            if not char.isalpha():
                hmap[index] = char
            else:
                stack.append(char)
        i = 0
        for i in range(len(S)):
            if i in hmap:
                result = result + hmap.get(i)
                del hmap[i]
            else:
                result = result + stack.pop()
        return result

print(Solution().reverseOnlyLetters(input))
