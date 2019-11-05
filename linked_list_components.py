# Benjamin Wiens
# Linked List Components (https://leetcode.com/problems/linked-list-components/)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        components = 0
        Gset = set(G)
        while head:
            if head.val in Gset:
                if not head.next or head.next.val not in Gset:
                    components += 1
            head = head.next
        return components
