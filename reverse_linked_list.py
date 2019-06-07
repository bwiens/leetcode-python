# Benjamin Wiens
# Reverse Linked List (https://leetcode.com/problems/reverse-linked-list/)
# Leetcode Accepted

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#to reverse a linked list, you need to reverse the curr to prev connection first but also know how to get to the original "next" before

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        previous, current = None, None
        while head:
            current = head
            head = head.next
            current.next = previous
            previous = current
        return previous
