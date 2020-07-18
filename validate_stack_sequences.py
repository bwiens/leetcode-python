#!/usr/bin/python

pushed = [1,2,3,4,5]
popped = [4,5,3,2,1]

class Solution:
    def validateStackSequences(self, pushed, popped) -> bool:
        # simulate the stack
        stack = []
        i = 0
        for push in pushed:
            stack.append(push)
            while stack and stack[-1] == popped[i]:
                i += 1
                stack.pop()
        return i == len(popped)
    
print(Solution().validateStackSequences(pushed, popped))
