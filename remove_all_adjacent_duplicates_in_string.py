#!/usr/bin/python
# Benjamin Wiens
# Remove All Adjacent Duplicates in String (https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/)

string = "abbaca"
class Solution:
    def removeDuplicates(self, S):
        stack = []
        for char in S:
            #discard duplicate
            if len(stack) > 0 and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)

print(Solution().removeDuplicates(string))
