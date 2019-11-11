# Benjamin Wiens
# Add Two Numbers (https://leetcode.com/problems/add-two-numbers/)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry, sum = 0, 0
        new = ListNode(0)
        dummy = new
        while l1 or l2:
            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            sum += carry
            carry = sum // 10
            new.val = sum % 10
            if l1 or l2:
                new.next = ListNode(None)
                new = new.next
        if carry:
            new.next = ListNode(carry)
        return dummy
