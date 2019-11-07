# Benjamin Wiens
# Odd Even Linked List (https://leetcode.com/problems/odd-even-linked-list)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 1->2->3->4
# first node is odd
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return
        odds = head
        evens = head.next
        evens_head = evens
        while evens and evens.next:
            #assign simultaneously
            odds.next = evens.next
            odds = evens.next
            evens.next = odds.next
            evens = evens.next
        #connect evens tail with odds head
        odds.next = evens_head
        return head
            
