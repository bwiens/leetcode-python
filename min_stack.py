#!/usr/bin/python
#Benjamin Wiens
#Min Stack (https://leetcode.com/problems/min-stack/description/)
#Leetcode Accepted

class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        self.stack.pop(-1)

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None
    def getMin(self):
        """
        :rtype: int
        """
        if len(self.stack) > 0:
            mins = min(self.stack)
            return mins
        else:
            return None

minStack = MinStack()
minStack.push(-1)
print(minStack.top())
print(minStack.getMin())
