#!/usr/bin/python
#Benjamin Wiens
#Min Stack (https://leetcode.com/problems/min-stack/description/)

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        stack.pop(-1)

    def top(self):
        """
        :rtype: int
        """
        return stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        min = stack[0]
        for i in range(len(stack)):
            if min > stack[i]:
                min = stack[i]
        return min

minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())   #--> Returns -3.
minStack.pop()
print(minStack.top())      #--> Returns 0.
print(minStack.getMin())   #--> Returns -2.
