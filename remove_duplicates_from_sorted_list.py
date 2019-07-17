# Benjamin Wiens
# Remove Duplicates From Sorted List (https://leetcode.com/problems/remove-duplicates-from-sorted-list/)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = head
        while head:
            while head.next and head.val == head.next.val:
                head.next = head.next.next
            head = head.next
        return dummy
