#!/usr/bin/python
#Benjamin Wiens
#Stack Implementation + Stack Sorting

#Stack Exercise
#class Stack:
#    def __init__(self):
#        self.items = []

#    def isEmpty(self):
#        return self.items == []

#    def push(self, item):
#        self.items.append(item)

#    def pop(self):
#        return self.items.pop()

#    def peek(self):
#        return self.items[len(self.items) - 1]

#    def size(self):
#        return len(self.items)

def create_stack():
    stack = []
    return stack

def is_empty(stack):
    if len(stack) == 0:
        return True
    else:
        return False

def pop(stack):
    if not is_empty(stack):
        stack.pop()
        return stack.pop()

def top(stack):
    if not is_empty(stack):
        return stack.pop()

def push(stack, item):
    stack.append(item)

def print_stack(stack):
    print(stack)

def stack_sort(stack):
    curr = 0
    helper = []
    while len(stack) != 0:
        curr = stack.pop()
        #put smaller elements at the bottom of helper
        while len(helper) != 0 and helper[-1] > curr:
            #push back on original stack
            stack.append(helper.pop())
        #last element
        helper.append(curr)
    return helper

newStack = create_stack()
push(newStack, -1)
push(newStack, 3)
push(newStack, 2)
push(newStack, -4)
push(newStack, -10)
push(newStack, 30)
print_stack(newStack)
print(stack_sort(newStack))
