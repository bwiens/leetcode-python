# Benjamin Wiens
# Flatten a Multilevel Doubly Linked List (https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/)

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        current = head
        stack = []
        while current:
            #print(current.val)
            if current.child:
                # if current has both a child and a next, save the next to 
                # process later
                if current.next:
                    stack.append(current.next)
                current.next = current.child
                current.child.prev = current
                current.child = None
            if not current.next and stack:
                # current node is a child without a next (end of a sub-chain)
                node = stack.pop()
                node.prev = current
                current.next = node
            current = current.next
        return head
