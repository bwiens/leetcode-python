#!/usr/bin/python
# Benjamin Wiens
# Linked List
# Leetcode Accepted (https://leetcode.com/problems/middle-of-the-linked-list/)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        result = []
        i = 1
        while head:
            result.append(head)
            i += 1
            head = head.next
        if len(result) < 3: 
            return result[-1]
        else:
            return result[(len(result)//2)]
