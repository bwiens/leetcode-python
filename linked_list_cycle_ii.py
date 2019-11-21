# Benjamin Wiens
# Linked List Cycle II (https://leetcode.com/problems/linked-list-cycle-ii/)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        while head:
            if head.val == None:
                return head
            else:
                head.val = None
            head = head.next
