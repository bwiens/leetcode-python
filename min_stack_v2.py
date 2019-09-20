#!/usr/bin/python
#Benjamin Wiens
#Min Stack (https://leetcode.com/problems/min-stack/ -- Better Performance)

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        if self.stack:
            self.stack.append(min(x, self.stack[-2]))
        else:
            self.stack.append(x)          
        #append now the most recent number
        self.stack.append(x)

    def pop(self) -> None:
        if self.stack:
            #pop twice to remove min
            self.stack.pop()
            self.stack.pop()
            
    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        # minimum element is always 2nd last!
        if self.stack:
            return self.stack[-2]
