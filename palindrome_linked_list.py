# Benjamin Wiens
# Palindrome Linked List (https://leetcode.com/problems/palindrome-linked-list/)
# Leetcode Accepted

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        #print(vals)
        if vals[::-1] != vals:
            return False
        return True
