#!/usr/bin/python
# Benjamin Wiens
# Remove All Adjacent Duplicates in String II (https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/)

s = "pbbcggttciiippooaais"
k = 2
class Solution:
    def removeDuplicates(self, s, k):
        stack, result = [], ''
        for char in s:
            # if stack is empty
            if not stack:
                stack.append([(char), (1)])
            else:
                if stack[-1][0] == char:
                    stack[-1][1] += 1
                    # if last item of stack count equals k, pop item
                    if stack[-1][1] == k:
                        stack.pop()
                else:
                    stack.append([(char), (1)])
        # create result string from stack 
        for item in stack:
            for i in range(item[1]):
                result += item[0]
        return result
print(Solution().removeDuplicates(s,k))
