# Benjamin Wiens 
# Remove Linked List Elements (https://leetcode.com/problems/remove-linked-list-elements/)
# Leetcode Accepted

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        #skip elements that are == val
        while head and head.val == val:
            head = head.next
        dummy = head
        #traverse linked list
        while head and head.next:
            if head.next.val == val:
                #print("hit")
                head.next = head.next.next
            else:
                head = head.next
        return dummy
